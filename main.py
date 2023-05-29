from utils import get_python_files
from python_code_parser import parse_python_file
from gpt_api import GPTAPI
from markdown_generator import MarkdownGenerator
import re
import time
    
# 配置
dir_path = "*/explain_your_code"
output_md_path = "*/explain_your_code/output.md"
api_key = "your-api-key"
prompt = "按以下格式解释下面的python代码：输入、输出以及函数的功能："

# 初始化
print("\n\n")
print("*****************************")
print("**** Initializing... ****")
print("*****************************")
gpt = GPTAPI(api_key, prompt)
# md = MarkdownGenerator(output_md_path)

# 创建Markdown文件
file_name = re.split(r"/", dir_path)[-1]
md_name = f"{file_name}.md"
with open(md_name, "w") as f:
    f.write(f"# {file_name}\n\n")

print(f"Created file: {file_name}")
md = MarkdownGenerator(md_name)

# 获取所有Python文件
print("\n\n")
print("*****************************")
print(f"**** Getting Python files from {dir_path}... ****")
print("*****************************")
python_files = get_python_files(dir_path)
print(f"Found {len(python_files)} Python files.")

for file_path in python_files:
    # 解析每个Python文件
    print("\n\n")
    print("*****************************")
    print(f"**** Parsing file {file_path}... ****")
    print("*****************************")
    functions = parse_python_file(file_path)
    print(f"Found {len(functions)} functions.")

    for function in functions:
        # 获取每个函数的描述
        print("\n\n")
        print("*****************************")
        print(f"**** Getting description for function:\n{function} ****")
        print("*****************************")
        description = gpt.get_function_description(function)
        print(f"Description: {description}")

        # 将函数和其描述添加到Markdown文件
        print("\n\n")
        print("*****************************")
        print(f"**** Adding function and description to Markdown file... ****")
        print("*****************************")
        md.add_header(f"File: {file_path}", level=2)
        md.add_code_block(function)
        md.add_paragraph(description)
        md.save
        time.sleep(4)# openai api限制每3秒钟一个请求

# 保存Markdown文件
print("\n\n")
print("*****************************")
print("**** Saving Markdown file... ****")
print("*****************************")
md.save()
print("Done!")
print("\n\n")