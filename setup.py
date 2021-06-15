import setuptools

with open("README.md", "r") as file:
    description = file.read()
    file.close()

setuptools.setup(
    name = "foo",
    version = "0.0.1",
    author = "hanlin chen",
    description = "A simple foo libary",
    long_description = description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/HarryChen1995/print_hello.git",
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operationg System :: OS Independent"
    ],
    python_requires = ">=3.5"
)
