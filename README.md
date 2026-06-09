# AI-Driven Automated Log Analyzer & Threat Detector

An automated threat intelligence tool designed to parse web server access logs, isolate malicious activity patterns, and leverage Generative AI to classify attack vectors and provide actionable remediation steps.

## 🚀 Features

- **Automated Log Parsing:** Systematically scans server logs to identify anomalous behavior and signature patterns.
- **AI-Powered Triaging:** Integrates the OpenAI API to categorize sophisticated attacks (e.g., SQL Injection, Cross-Site Scripting, Brute Force).
- **Remediation Output:** Generates clear, contextual defensive steps for blue team response operations.
- **Secure Credential Management:** Implements strict security policies using environment variables (`python-dotenv`) to prevent API key exposure.

## 🛠️ Technical Stack

- **Language:** Python 3
- **AI Integration:** OpenAI API
- **Environment Management:** Python Virtual Environment (`venv`)
- **Version Control:** Git

## 💻 Local Installation & Setup

Follow the steps below to set up the environment and run the analyzer locally.

### 1. Clone the Repository
```bash
git clone https://github.com
cd ai-driven-automated-log-analyzer-threat-detector
```

### 2. Initialize and Activate a Virtual Environment

Choose the command block that matches your operating system:

#### 🐧 Linux / macOS
```bash
python3 -m venv venv
source venv/bin/activate
```

#### 🪟 Windows (PowerShell)
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```
*(Note: If a script execution policy error occurs on Windows, run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process` first.)*

---

### 3. Install Dependencies
Ensure your virtual environment is active `(venv)` and run the package manager to pull the verified dependencies from `requirements.txt`:

```bash
# On Linux/macOS
pip install --upgrade pip
pip install -r requirements.txt

# On Windows
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 4. Secure Environment Configuration
Create a local environment file in the root directory to store your API credentials securely:

```bash
# On Linux/macOS
touch .env

# On Windows
New-Item .env
```

Open the freshly created `.env` file in your editor and add your secret key:
```env
OPENAI_API_KEY=your_actual_openai_api_key_here
```
*(Note: The `venv/` directory and `.env` file are explicitly blocked via `.gitignore` to prevent accidental public credential exposures.)*

### 5. Run the Analyzer
Execute the main script to parse local server logs and generate threat intelligence metrics:
```bash
python analyzer.py
```

## 📊 Expected Output Example

When `analyzer.py` runs against a suspicious log source, it tracks metrics and prints a structured triage report directly to the terminal:

```text
Opening local log source: logs.json...
Total entries found: 3
Entries flagged for AI analysis: 2

Requesting AI incident response breakdown...

--- AI Threat Intelligence Report ---
### Analysis of Suspicious Logs

#### Log Entry 1:
{
    "timestamp": "2026-06-08T10:01:22Z",
    "src_ip": "10.0.0.15",
    "request": "POST /login HTTP/1.1",
    "status": 401,
    "user_agent": "Hydra/7.5"
}
**Attack Vector: Brute Force Attack**
- **Explanation**: The request is a POST to the /login endpoint using Hydra/7.5. This suggests that the source IP is attempting to guess user credentials.

#### Log Entry 2:
{
    "timestamp": "2026-06-08T10:02:45Z",
    "src_ip": "192.168.1.100",
    "request": "GET /admin/select+*+from+users HTTP/1.1",
    "status": 404,
    "user_agent": "sqlmap/1.4"
}
**Attack Vector: SQL Injection Attempt**
- **Explanation**: The request contains a SQL injection payload attempting to extract database tables using sqlmap/1.4.

### Technical Remediation Steps
1. For Brute Force: Implement account lockout policies, rate limiting, and MFA.
2. For SQLi: Implement input validation, use prepared queries, and deploy a Web Application Firewall (WAF).
```

## 🛡️ Secure Development Best Practices

- **Zero-Trust Hardcoded Keys:** Secrets are loaded dynamically via runtime environment parsing rather than source code injection.
- **Environment Isolation:** Utilizing Python virtual environments ensures supply-chain dependency tracking remains strict and isolated.
