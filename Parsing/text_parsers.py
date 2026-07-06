# =========================
# SIMPLE MD FILE READER
# =========================
def read_text(file_path):
    """Read and return raw text content from a file."""
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


# =========================
# MARKDOWN PARSER
# =========================
def parse_markdown_as_text(file_path):
    """Parse markdown file and return as raw text.

    This is a placeholder for future LLM-based parsing using LangChain.
    Currently returns the raw markdown content.
    """
    return read_text(file_path)

