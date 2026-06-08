import os
import json
from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI()

def load_json_logs(file_path):
    """Safely opens and reads the JSON log file."""
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

def pre_filter_suspicious_logs(log_data):
    """Filters logs locally to isolate potential security threats."""
    filtered_logs = []
    
    for entry in log_data:
        status = entry.get("status")
        request = entry.get("request", "").lower()
        user_agent = entry.get("user_agent", "").lower()
        
        # Flag 1: Failed logins or unauthorized access attempts
        if status in [401, 403, 404, 500]:
            filtered_logs.append(entry)
            continue
            
        # Flag 2: Common attack signatures in the request path
        attack_keywords = ["select", "union", "drop", "alter", "../", "etc/passwd", "bin/sh"]
        if any(keyword in request for keyword in attack_keywords):
            filtered_logs.append(entry)
            continue
            
        # Flag 3: Known automated scanning tools in User-Agent header
        scanner_keywords = ["sqlmap", "hydra", "nmap", "nikto"]
        if any(keyword in user_agent for keyword in scanner_keywords):
            filtered_logs.append(entry)
            continue
            
    return filtered_logs

def analyze_logs_with_ai(filtered_data):
    """Sends only the filtered suspicious traffic to the AI for analysis."""
    if not filtered_data:
        return "No suspicious logs detected by local pre-filter. API call skipped."
        
    formatted_logs = json.dumps(filtered_data, indent=2)
    
    prompt = (
        "You are an expert Cybersecurity Incident Response AI.\n"
        "Analyze these pre-filtered suspicious JSON web server logs. "
        "Classify the specific attack vectors, explain why they are dangerous, "
        "and provide technical remediation steps.\n\n"
        f"Suspicious Logs:\n{formatted_logs}"
    )
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error connecting to API: {e}"

if __name__ == "__main__":
    log_file = "logs.json"
    print(f"Opening local log source: {log_file}...")
    
    all_logs = load_json_logs(log_file)
    
    if all_logs:
        print(f"Total entries found: {len(all_logs)}")
        
        # Run local preprocessing
        suspicious_logs = pre_filter_suspicious_logs(all_logs)
        print(f"Entries flagged for AI analysis: {len(suspicious_logs)}")
        
        print("\nRequesting AI incident response breakdown...")
        analysis_report = analyze_logs_with_ai(suspicious_logs)
        print("\n--- AI Threat Intelligence Report ---")
        print(analysis_report)
