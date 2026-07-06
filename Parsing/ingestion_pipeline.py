import os
import json
from pathlib import Path

# Import parsers from separate modules
from yaml_parsers import parse_openapi, parse_deployment
from csv_parsers import parse_metrics, parse_infra, parse_workload
from text_parsers import parse_markdown_as_text


# =========================
# CONFIG
# =========================
# Use absolute path relative to this script's location
DATA_DIR = str(Path(__file__).parent.parent / "ProjectSampleDocs")
OUTPUT_DIR = str(Path(__file__).parent.parent / "output")
OUTPUT_FILE = str(Path(OUTPUT_DIR) / "parsed_documents.json")



# =========================
# 8. MASTER PIPELINE
# =========================
def build_context():
    data = {}

    for file in os.listdir(DATA_DIR):
        path = os.path.join(DATA_DIR, file)

        if file.lower().endswith(".yaml"):
            if "openapi" in file.lower():
                data["api"] = parse_openapi(path)
            else:
                data["deployment"] = parse_deployment(path)

        elif file.lower().endswith(".csv"):
            if "metrics" in file.lower() and "infra" not in file.lower():
                data["metrics"] = parse_metrics(path)
            elif "infra" in file.lower():
                data["infrastructure"] = parse_infra(path)
            elif "workload" in file.lower():
                data["workload"] = parse_workload(path)

        elif file.lower().endswith(".md"):
            if "architecture" in file.lower():
                data["architecture_raw"] = parse_markdown_as_text(path)
            elif "nfr" in file.lower():
                data["nfr_raw"] = parse_markdown_as_text(path)
            elif "guidelines" in file.lower():
                data["guidelines_raw"] = parse_markdown_as_text(path)
            elif "previous" in file.lower():
                data["previous_report_raw"] = parse_markdown_as_text(path)

    return data


# =========================
# 9. RUN
# =========================
if __name__ == "__main__":
    # Create output directory if it doesn't exist
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Build the context
    context = build_context()

    # Print to console
    print(json.dumps(context, indent=2))

    # Save to file
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(context, f, indent=2, ensure_ascii=False)

    print(f"\n✓ Output saved to: {OUTPUT_FILE}")
