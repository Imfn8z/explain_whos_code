import os

def get_python_files(dir_path):
    """递归获取给定目录及其子目录中的所有Python文件"""
    python_files = []

    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file.endswith(".py"):
                python_files.append(os.path.join(root, file))
                print(f"Identified Python files: {python_files}")            

    return python_files
