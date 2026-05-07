import json
from agent.llm_agent import LLMAgent

def load_scan(file_path):
    with open(file_path, "r") as f:
        return json.load(f)

def apply_fix(file_path, fixed_code):
    with open(file_path, "w") as f:
        f.write(fixed_code)

def main(scan_file):
    scan_data = load_scan(scan_file)
    agent = LLMAgent()

    for issue in scan_data.get("issues", []):
        file_path = issue["file"]
        code_snippet = issue["code"]

        fixed_code = agent.suggest_fix(code_snippet)
        apply_fix(file_path, fixed_code)

        print(f"[FIXED] {file_path}")

if __name__ == "__main__":
    import sys
    main(sys.argv[1])
