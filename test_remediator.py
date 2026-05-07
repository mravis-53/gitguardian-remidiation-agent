from remediation_agent.remediator import RemediationAgent

def test_generate_fix():
    agent = RemediationAgent()

    vuln = {
        "type": "Hardcoded Secret"
    }

    result = agent.generate_fix(vuln)

    assert "recommendation" in result
