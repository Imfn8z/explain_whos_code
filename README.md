# python函数批量解释器

这个项目是为了解析给定文件夹中的所有Python代码文件，并为每个函数或代码片段提供解释。这个解释是通过调用 OpenAI GPT-3.5 的 API 来生成的。所有的解释都会以Markdown格式保存到一个文件中，方便后续查看和分享。

## 运行环境

- Python 3.7+
- OpenAI Python Client v0.27.0

## 如何使用

1. 克隆或下载此项目到本地。
2. 安装必要的依赖：`pip install -r requirements.txt`
3. 替换 `main.py` 文件中的配置参数，包括代码文件的路径、输出Markdown文件的路径，以及你的OpenAI API key。
4. 运行 `main.py`：`python main.py`

## 文件结构

- `main.py`: 主文件，用于运行整个项目。同时包括配置项，如文件路径和api key请在此设置。
- `utils.py`: 包含工具函数，用于获取指定文件夹下的所有Python文件。
- `python_code_parser.py`: 解析Python代码，提取出函数和代码片段。
- `gpt_api.py`: 调用 OpenAI GPT-3.5 的 API，获取代码的解释。
- `markdown_generator.py`: 生成 Markdown 文件，保存代码和对应的解释。

## 开源协议

该软件是免费的开源软件，根据GNU通用公共许可证第3版(GPLv3)的条款发布。
您可以在本软件附带的许可证文件中找到GPLv3许可证文本的副本，或在线访问https://www.gnu.org/licenses/gpl-3.0.en.html.
分发此软件的目的是希望它有用，但没有任何担保；甚至没有对适销性或特定用途的适用性的默示担保。有关更多详细信息，请参阅GPLv3许可证。
如果您修改或分发本软件或其任何部分，则必须在相同的许可条款下提供源代码，并在软件中附带GPLv3许可文本的副本。
如果您对本软件或GPLv3许可证有任何疑问，请联系作者或访问GNU网站https://www.gnu.org/licenses/gpl-3.0.en.html.

---

# Python function batch interpreter

This project aims to parse all Python code files in a given directory and generate explanations for each function or code snippet. The explanations are generated by calling the API of OpenAI GPT-3.5. All the explanations will be saved to a file in Markdown format, making it easy to review and share.

## Environment

- Python 3.7+
- OpenAI Python Client v0.27.0

## How to Use

1. Clone or download this project to your local machine.
2. Install the necessary dependencies: `pip install -r requirements.txt`
3. Replace the configuration parameters in `main.py`, including the path to your code files, the path to your output Markdown file, and your OpenAI API key.
4. Run `main.py`: `python main.py`

## File Structure

- `main.py`: The main file, responsible for running the entire project.Also include configuration items, such as file path and api key, please set here.
- `utils.py`: Contains utility functions for getting all Python files in a specified directory.
- `python_code_parser.py`: Parses Python code, extracting functions and code snippets.
- `gpt_api.py`: Calls the API of OpenAI GPT-3.5 to get explanations for the code.
- `markdown_generator.py`: Generates a Markdown file to save the code and its corresponding explanations.

## LICENSE

This software is free and open source software, released under the terms of the GNU General Public License, version 3 (GPLv3).

You can find a copy of the GPLv3 license text in the LICENSE file included with this software, or online at https://www.gnu.org/licenses/gpl-3.0.en.html.

This software is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GPLv3 license for more details.

If you modify or distribute this software, or any part of it, you must make the source code available under the same license terms, and include a copy of the GPLv3 license text with the software.

If you have any questions about this software or the GPLv3 license, please contact the author or visit the GNU website at https://www.gnu.org/licenses/gpl-3.0.en.html.
