class RemediationAgent:

    def generate_fix(self, vulnerability):
        vuln_type = vulnerability.get("type")

        if vuln_type == "Hardcoded Secret":
            return {
                "recommendation": "Move secret to environment variable",
                "example_fix": "os.getenv('AWS_SECRET_ACCESS_KEY')"
            }

        return {
            "recommendation": "Manual review required"
        }
