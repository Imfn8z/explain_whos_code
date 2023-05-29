## File: /Users/huangbo/Library/Mobile Documents/com~apple~CloudDocs/代码/explain_your_code/markdown_generator.py

```python
def __init__(self, file_path):
    self.file_path = file_path
    self.markdown_text = ''
```

输入：file_path（文件路径）
输出：无
功能：构造函数，用于初始化文件路径和markdown_text变量。

## File: /Users/huangbo/Library/Mobile Documents/com~apple~CloudDocs/代码/explain_your_code/markdown_generator.py

```python
def add_header(self, text, level=1):
    self.markdown_text += f"{'#' * level} {text}\n\n"
```

输入：self，text，level（可选）
输出：无
功能：将文本添加到markdown_text中，并在文本前添加一个由level决定的标题等级（默认为1）

## File: /Users/huangbo/Library/Mobile Documents/com~apple~CloudDocs/代码/explain_your_code/markdown_generator.py

```python
def add_code_block(self, text, language='python'):
    self.markdown_text += f'```{language}\n{text}\n```\n\n'
```

# 输入：一段文本和一个可选的语言（默认为python）
# 输出：无
# 功能：将文本添加到markdown_text中，并使用语言标记（默认为python）

## File: /Users/huangbo/Library/Mobile Documents/com~apple~CloudDocs/代码/explain_your_code/markdown_generator.py

```python
def add_paragraph(self, text):
    self.markdown_text += f'{text}\n\n'
```

# 输入：一个字符串参数text
# 输出：无
# 功能：将参数text添加到self.markdown_text变量中，并在末尾添加换行符号。

## File: /Users/huangbo/Library/Mobile Documents/com~apple~CloudDocs/代码/explain_your_code/markdown_generator.py

```python
def save(self):
    with open(self.file_path, 'w') as md_file:
        md_file.write(self.markdown_text)
```

# 输入：self，self.file_path，self.markdown_text
# 输出：无
# 功能：将self.markdown_text写入self.file_path文件中

## File: /Users/huangbo/Library/Mobile Documents/com~apple~CloudDocs/代码/explain_your_code/utils.py

```python
def get_python_files(dir_path):
    """递归获取给定目录及其子目录中的所有Python文件"""
    python_files = []
    for (root, dirs, files) in os.walk(dir_path):
        for file in files:
            if file.endswith('.py'):
                python_files.append(os.path.join(root, file))
                print(f'Identified Python files: {python_files}')
    return python_files
```

输入：dir_path（目录路径）
输出：python_files（Python文件列表）
功能：递归获取给定目录及其子目录中的所有Python文件

## File: /Users/huangbo/Library/Mobile Documents/com~apple~CloudDocs/代码/explain_your_code/gpt_api.py

```python
def __init__(self, api_key, prompt):
    openai.api_key = api_key
    self.prompt = prompt
```

输入：api_key，prompt
输出：无
函数功能：该函数用于初始化openai对象，将api_key赋值给openai.api_key，将prompt赋值给self.prompt。

## File: /Users/huangbo/Library/Mobile Documents/com~apple~CloudDocs/代码/explain_your_code/gpt_api.py

```python
def get_function_description(self, function_code):
    response = openai.Completion.create(model='text-davinci-003', prompt=f'{self.prompt}\n{function_code}', temperature=0, max_tokens=150, top_p=1.0, frequency_penalty=0.0, presence_penalty=0.0)
    return response.choices[0].text.strip()
```

输入：function_code（函数代码）
输出：函数描述
功能：该函数使用OpenAI的文本生成模型，根据函数代码生成函数描述。

## File: /Users/huangbo/Library/Mobile Documents/com~apple~CloudDocs/代码/explain_your_code/python_code_parser.py

```python
def __init__(self):
    self.functions = []
```

输入：无
输出：无
函数功能：该函数是一个构造函数，用于初始化一个类的实例，在该函数中，创建一个空列表，用于存储函数。

## File: /Users/huangbo/Library/Mobile Documents/com~apple~CloudDocs/代码/explain_your_code/python_code_parser.py

```python
def visit_FunctionDef(self, node):
    function_content = ast.unparse(node)
    self.functions.append(remove_comments(function_content))
```

输入：node，一个ast节点
输出：无
函数功能：将node节点转换为字符串，并将字符串中的注释去除，最后将字符串添加到self.functions列表中。

## File: /Users/huangbo/Library/Mobile Documents/com~apple~CloudDocs/代码/explain_your_code/python_code_parser.py

```python
def remove_comments(function_content):
    return '\n'.join([line for line in function_content.split('\n') if not line.strip().startswith('#')])
```

输入：function_content（字符串）
输出：字符串
函数功能：从function_content中移除以#开头的行，并返回一个新的字符串。

## File: /Users/huangbo/Library/Mobile Documents/com~apple~CloudDocs/代码/explain_your_code/python_code_parser.py

```python
def parse_python_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    tree = ast.parse(content)
    parser = FunctionParser()
    parser.visit(tree)
    return parser.functions
```

# 输入：文件路径
# 输出：函数列表
# 功能：该函数用于解析python文件，读取文件内容，使用ast模块解析文件，然后使用FunctionParser类解析函数，最后返回函数列

