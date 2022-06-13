from rich.console import Console
from rich.syntax import Syntax
import time
import os

MAIN_PATH = "D:\\Works\\UYGULAMA\\ERDEM_VERSION\\lib"
_file_list = []

for root, dirs, files in os.walk(MAIN_PATH):
    for file in files:
        _file_list.append(os.path.join(root, file))

console = Console()

while True:
    for _file in _file_list:
        syntax = Syntax.from_path(_file)
        console.print(syntax, justify="center")
        time.sleep(0.15)
