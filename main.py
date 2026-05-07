import json
from remediation_agent.remediator import RemediationAgent

def main():
    sample_vulnerability = {
        "type": "Hardcoded Secret",
        "file": "app.py",
        "line": 12,
        "description": "AWS Secret Key detected"
    }

    agent = RemediationAgent()
    fix = agent.generate_fix(sample_vulnerability)

    print("Suggested Fix:")
    print(json.dumps(fix, indent=2))

if __name__ == "__main__":
    main()
