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


def convert(input_file):
    input_path = Path(input_file)

    # Determine output name (e.g., input.json -> input.md)
    output_file = input_path.stem + ".md"
    output_title = input_path.stem

    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        # Find the starting point of the JSON
        json_content = ""
        found_start = False

        for line in lines:
            clean_line = line.strip()

            # 1. Look for the start of the actual JSON
            if not found_start and clean_line.startswith('{'):
                found_start = True

            # 2. Check for the END marker
            # We check this BEFORE adding the line to json_content
            if found_start and clean_line == "EOF":
                break  # Exit the loop immediately

            # 3. If we are currently "inside" the JSON, accumulate the line
            if found_start:
                json_content += line

        if not json_content:
            print("Error: No JSON content found between markers.")
            return

        # Parse the extracted string
        data = json.loads(json_content)
        print("Successfully parsed JSON after skipping surrounding text.")

        markdown_output = f"# {output_title}\n\n"
        markdown_output += "### AI Studio Conversation Export\n\n"

        # AI Studio JSON structure typically has a 'contents' list
        # Adjust the key if your specific export uses a different name
        content_list = data if isinstance(data, list) else data.get('contents', [])

        for entry in content_list:
            role = entry.get('role', 'unknown').capitalize()
            # Parts can be a list of text objects
            parts = entry.get('parts', [])
            text_content = ""
            for p in parts:
                if 'text' in p:
                    text_content += p['text']
            markdown_output += f"### {role}\n{text_content}\n\n---\n\n"

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(markdown_output)

        print(f"Success! Converted to {output_file}")

    except json.JSONDecodeError as e:
        print(f"JSON Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


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
    # Check if the user provided a filename
    if len(sys.argv) > 1:
        # peek(sys.argv[1], 100)
        convert(sys.argv[1])
    else:
        print('Usage: python convert.py <your_file.json>')
