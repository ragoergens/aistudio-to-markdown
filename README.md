# aistudio-to-markdown
JSON to Markdown Converter for Google AI Studio exports

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
* For example, upload to [Google NotebookLM](https://notebooklm.google.com/) (the use case for which I wrote this script)
