# print_hello
- This is simple python package to demonstrate how to upload package to PyPl
## file structure 
```
foo_package/
|-- build
|   |-- bdist.linux-x86_64
|   `-- lib
|       `-- hello_print_hanlin
|           |-- __init__.py
|           `-- print_hello.py
|-- dist
|   |-- hello_print_hanlin-0.0.1-py3-none-any.whl
|   `-- hello_print_hanlin-0.0.1.tar.gz
|-- hello_print_hanlin
|   |-- __pycache__
|   |   |-- __init__.cpython-36.pyc
|   |   `-- print_hello.cpython-36.pyc
|   |-- __init__.py
|   `-- print_hello.py
|-- hello_print_hanlin.egg-info
|   |-- PKG-INFO
|   |-- SOURCES.txt
|   |-- dependency_links.txt
|   `-- top_level.txt
|-- LICENSE.txt
|-- README.md
`-- setup.py
```
## build package
```bash
$: python3 setup.py  sdist bdist_wheel
 
```
## upload package to pypi.org
```bash
$: python3  -m twine upload  dist/*
 
```
