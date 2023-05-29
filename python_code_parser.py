import ast
import os

class FunctionParser(ast.NodeVisitor):
    def __init__(self):
        self.functions = []

    def visit_FunctionDef(self, node):
        function_content = ast.unparse(node)
        self.functions.append(remove_comments(function_content))

def remove_comments(function_content):
    return "\n".join([line for line in function_content.split('\n') if not line.strip().startswith('#')])

def parse_python_file(file_path):
    with open(file_path, "r") as file:
        content = file.read()
        

    tree = ast.parse(content)
    parser = FunctionParser()
    parser.visit(tree)
    
    return parser.functions
