# AI-Driven Automated Log Analyzer & Threat Detector

## Project Overview
This project is an automated incident response script designed to optimize threat detection pipelines and minimize cloud API token consumption. Built with Python and integrated with the OpenAI API, the tool leverages a two-tier analysis approach: a lightweight local pre-filtering system to catch common attack signatures, followed by advanced LLM-driven incident classification for flagged traffic.

## Architectural Flow
1. **Ingestion:** Reads raw JSON web server logs.
2. **Local Pre-filtering:** Isolates suspicious activity based on specific HTTP response statuses (401, 403, 404, 500), attack strings (`../`, `etc/passwd`), and known malicious user-agents (`sqlmap`, `nmap`, `hydra`).
3. **AI Triaging:** Transmits only the high-risk filtered anomalies to the `gpt-4o-mini` model.
4. **Threat Intelligence Output:** Outputs structured incident response reports detailing specific attack classifications, threat impacts, and operational remediation steps.

## Technical Skills Demonstrated
* **Security Frameworks:** Threat Vector Classification, Input Parsing Validation
* **Secure Coding Practices:** Decoupled Credential Management, Local Data Pre-processing, Robust Pathing
* **Tooling & Environments:** Python, Linux/Bash environment execution, OpenAI SDK, Python-Dotenv

## Prerequisites
* Python 3.8 or higher installed on your machine.
* A valid OpenAI API key with available credits.

## Local Installation & Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com
   cd ai-driven-automated-log-analyzer-threat-detector
   ```

2. **Install Required Dependencies:**
   ```bash
   pip install openai python-dotenv
   ```

3. **Secure Environment Configuration:**
   This project strictly enforces decoupled credential handling policies to prevent secret key exposure. 
   * Create a file named `.env` in the root folder.
   * Add your private OpenAI credentials to it:
     ```env
     OPENAI_API_KEY=your_actual_api_key_here
     ```
   * *Note: The system leverages Python's `pathlib` library to dynamically locate the `.env` file relative to the execution script directory, preventing path failures across different Linux/Windows folder environments. The `.env` file is explicitly included in our `.gitignore` to prevent public version control exposure.*

## Running the Application
1. Place your target web server log file named `logs.json` into the root directory.
2. Execute the python pipeline from your terminal:
   ```bash
   python analyzer.py
   ```

## Sample Input vs. AI Threat Report Output

### Sample Input Log Entry (`logs.json` snippet):
```json
{
  "timestamp": "2026-06-08T10:01:22Z",
  "src_ip": "10.0.0.15",
  "request": "POST /login HTTP/1.1",
  "status": 401,
  "user_agent": "Hydra/7.5"
}
```

### Sample Output Threat Intelligence Report:
#### Log Entry 1:
**Attack Vector: Brute Force Attack**

* **Explanation**: The `POST /login` request with a `401` status code indicates that the authentication attempt failed. The user agent "Hydra/7.5" is a well-known password-cracking tool used for brute-force attacks. This suggests that the attacker is trying to guess user credentials by repeatedly attempting to log in.
* **Danger**: Brute force attacks can lead to unauthorized access if the attacker successfully guesses valid credentials. This can result in data breaches, unauthorized actions, and compromise of sensitive information.
