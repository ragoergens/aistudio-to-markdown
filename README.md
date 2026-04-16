# aistudio-to-markdown

JSON to Markdown Converter for Google AI Studio exports

## Overview

Would you like to use your Google AI Studio prompt results in another tool?
* **Problem**: native Markdown export is missing in AI Studio, e.g. for importing into Google NotebookLM.
* **Solution**: a quick Python script does the job: [aistudio-to-markdown / json_to_md.py](https://github.com/ragoergens/aistudio-to-markdown/blob/main/json_to_md.py)

## Usage

### 1. Export from Google AI Studio

To download your prompt as JSON:
* Open [Google AI Studio](https://aistudio.google.com/prompts/)
* Select the prompt you want to export
* Click **Get Code** and select **REST**
* Click **Download**

You'll get `ai_studio_code.txt` as local file.

### 2. Rename your local file

Copy the **prompt name** from AI Studio and apply it to the local **file name**.

You'll get `<prompt_name>.txt` as resulting name.

### 3. Download the script

To download the script, either **clone the repo** or simply **download the script**.
* **Clone repo**: `git clone https://github.com/ragoergens/aistudio-to-markdown.git`
* **Download script**: [aistudio-to-markdown / json_to_md.py](https://github.com/ragoergens/aistudio-to-markdown/blob/main/json_to_md.py)

### 4. Run the Markdown conversion

To run the Markdown conversion, either **use your shell** or **drag and drop**.
* **Use shell**: `py json_to_md.py <prompt_name>.txt`
* **Use drag and drop**: Drop `<prompt_name>.txt` onto `json_to_md.py`

You'll get `<prompt_name>.md` as resulting file 🎉

Note: This step requires a working [Python install](https://www.python.org/).

### 5. Enjoy the resulting Markdown

#### 5.1 View or edit the Markdown

To view or edit the Markdown, use an appropriate tool. Some common options:
* [Visual Studio Code](https://code.visualstudio.com/)
* [IntelliJ Community Edition](https://www.jetbrains.com/idea/)

#### 5.2 Use the Markdown

Use the Markdown in your favorite context such as other AI tools.
* For example, upload it to [Google NotebookLM](https://notebooklm.google.com/) (the use case for which I wrote this script)

## Background

The JSON exported from Google AI Studio using the **REST** option is actually wrapped in a bash shell script.
Thus, it cannot be loaded directly into a Markdown converter.

[json_to_md.py](https://github.com/ragoergens/aistudio-to-markdown/blob/main/json_to_md.py) isolates the JSON block from the bash script, converts it to Markdown, and saves it.

### Frequently Asked Questions

#### Q: Does the script also work with the pure JSON block of AI Studio?
A: Yes it does.

#### Q: Does the script work as a generic JSON to Markdown converter?
A: No, it is bound the specific JSON schema of **Google AI Studio**.
It might work with other AI tools if they use the same JSON structure for prompt exports.
