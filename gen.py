import os
import pathlib

CURRENT = pathlib.Path(__file__).resolve().parent
INDEX_DIR = CURRENT.joinpath("source")
index_template_file = CURRENT.joinpath("index.rst")
index_dest_file = INDEX_DIR.joinpath("index.rst")

def count_indent(line: str)->int:
    indent = 0
    for i in line:
        if i==' ':
            indent+=1
        else:
            break
    return indent

def add_indent(indent: int, names: list[str])-> list[str]:
    for i,v in enumerate(names):
        names[i] = " "*indent+v
    return names

if __name__=="__main__":
    with open(str(index_template_file), encoding='utf-8', mode='r') as file:
        content = file.read()
    blogs = os.listdir(str(INDEX_DIR))
    def is_blog(filename: str) -> bool:
        if filename.endswith(".ipynb"):
            page_name = filename.replace(".ipynb", "")
            if page_name!="about":
                return True
        return False
    blogs = list(reversed(list(
        filter(
            is_blog, blogs
        )
    )))
    print(blogs)
    lines = content.split("\n")
    for i, line in enumerate(lines):
        if "ls_file" in line:
            indented_names = add_indent(count_indent(line), blogs)
            lines[i] = '\n'.join(indented_names)
            break
    with open(str(index_dest_file), encoding='utf-8', mode='w') as file:
        file.write('\n'.join(lines))
