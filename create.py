# -*- coding: utf-8 -*-
# @Time    : 2023/11/20 下午9:17
# @Author  : sudoskys
# @File    : create.py
# @Software: PyCharm

if __name__ == '__main__':
    project_name = input("Project Name: ")
    if not project_name:
        raise ValueError("Project Name Cant Be Empty")
    project_name = project_name.lower()
    project_name = project_name.replace(" ", "_")
    project_name = project_name.replace(".", "_")
    project_name = project_name.replace("__", "_")
    project_name = "_" + project_name
    import pathlib
    import pprint

    cwd = pathlib.Path(__file__).parent.absolute().__str__()
    pathlib.Path(cwd + "/" + "python" + "/" + project_name).mkdir(parents=True, exist_ok=True)
    pathlib.Path(cwd + "/" + "python" + "/" + project_name + "/" + "test_solution.py").touch()
    pathlib.Path(cwd + "/" + "python" + "/" + project_name + "/" + "README.md").touch()
    pprint.pprint(f"Project {project_name} Created")
    pprint.pprint(f"Files: ")
    pprint.pprint(f"  test_solution.py")
    pprint.pprint(f"  README.md")
    pprint.pprint("README.md Content: ")
    contents = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        contents.append(line)
    readme_input = "\n".join(contents)
    readme_content = (
        f"""# {project_name}\n"""
        f"""{readme_input}"""
    )
    with open(cwd + "/" + "python" + "/" + project_name + "/" + "README.md", "w") as f:
        f.write(readme_content)
