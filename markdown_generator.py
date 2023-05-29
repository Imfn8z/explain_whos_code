import markdown

class MarkdownGenerator:
    def __init__(self, file_path):
        self.file_path = file_path
        self.markdown_text = ''

    def add_header(self, text, level=1):
        self.markdown_text += f"{'#' * level} {text}\n\n"

    def add_code_block(self, text, language="python"):
        self.markdown_text += f"```{language}\n{text}\n```\n\n"

    def add_paragraph(self, text):
        self.markdown_text += f"{text}\n\n"

    def save(self):
        with open(self.file_path, 'w') as md_file:
            md_file.write(self.markdown_text)
