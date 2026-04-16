"""
JSON to Markdown Converter for Google AI Studio exports
Prerequisite: Get Code > REST > Download
Usage: python json_to_md.py <your_file.txt>
Author: René Görgens <rene@goergens.org>
Date: 2026-04-16
Description: Specifically handles Google AI Studio REST exports wrapped in 'cat << EOF' blocks.
"""

import json
import sys
from pathlib import Path


def isolate(input_path):
    """
    Extracts JSON content from a shell-wrapped file.
    Skips everything before the first '{' and stops at 'EOF'.
    """
    if not input_path.exists():
        raise FileNotFoundError(f"Could not find file: {input_path}")

    with open(input_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    json_content = ""
    found_start = False

    for line in lines:
        clean_line = line.strip()

        # Look for the start of the JSON
        if not found_start and clean_line.startswith('{'):
            found_start = True

        # Look for the end of the JSON
        if found_start and clean_line == "EOF":
            break

        if found_start:
            json_content += line

    if not json_content:
        raise ValueError("No valid JSON block found in the file.")

    return json.loads(json_content)


def convert(data, title):
    """
    Transforms Gemini API JSON structure into a Markdown string.
    """
    markdown_lines = f"# {title}\n\n"
    markdown_lines += "### AI Studio Conversation Export\n\n"

    # Navigate the Gemini JSON structure: contents -> role/parts -> text
    content_list = data.get("contents", [])

    for entry in content_list:
        role = entry.get('role', 'unknown').capitalize()
        # Parts can be a list of text objects
        parts = entry.get('parts', [])
        text_content = ""
        for p in parts:
            if 'text' in p:
                text_content += p['text']
        markdown_lines += f"### {role}\n{text_content}\n\n---\n\n"

    return markdown_lines


def main():
    if len(sys.argv) < 2:
        print("Usage: python json_to_md.py \"your_file.txt\"")
        return

    try:
        # 1. Setup paths
        input_file = Path(sys.argv[1])
        input_path = Path(input_file)
        output_file = input_path.stem + ".md"
        output_title = input_path.stem

        # 2. Isolate and parse JSON
        raw_data = isolate(input_file)

        # 3. Convert to Markdown
        md_result = convert(raw_data, output_title)

        # 4. Save
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(md_result)

        print(f"Success! Markdown saved to: {output_file}")

    except Exception as e:
        print(f"Error: {e}")


# Use for debugging
def peek(input_file, num):
    input_path = Path(input_file)

    with open(input_path, 'r', encoding='utf-8') as f:
        # Read the first (num) characters to see what's inside
        content_peek = f.read(num)
        print(f"DEBUG: First {num} chars of file: '{content_peek}'")

        if not content_peek.strip():
            print("ERROR: The file appears to be empty!")
            return


if __name__ == "__main__":
    main()
