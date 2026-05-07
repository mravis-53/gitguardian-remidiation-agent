import json

def mock_scan():
    return {
        "issues": [
            {
                "file": "samples/vulnerable_code.py",
                "type": "hardcoded_secret",
                "code": "API_KEY = '123456789'"
            }
        ]
    }

if __name__ == "__main__":
    result = mock_scan()
    with open("scan_results.json", "w") as f:
        json.dump(result, f, indent=2)

    print(json.dumps(result, indent=2))
