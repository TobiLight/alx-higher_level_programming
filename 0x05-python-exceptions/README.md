# 0x05. Python - Exceptions
This repository contains exercises and examples related to handling exceptions in Python. It covers various concepts and techniques for managing and responding to exceptions in Python programming.

## Table of Contents
- [Description](#description)
- [Topics Covered](#topics-covered)
- [Requirements](#requirements)
- [Getting Started](#getting-started)
- [Tasks & Files](#tasks--files)
- [Contributing](#contributing)
- [Author](#author)

## Description
Python provides a robust mechanism for handling errors and exceptions. Understanding how to handle exceptions effectively is crucial for writing reliable and robust Python code. This repository aims to help you learn and practice exception handling techniques in Python. The exercises and examples in this repository cover various topics related to exceptions, including:

## Topics Covered
The repository covers the following topics:
1. Introduction to exceptions
2. Handling exceptions with try-except
3. Multiple except blocks
4. Raising exceptions with raise
5. Custom exceptions
6. Exception chaining
7. The `finally` block
8. Exception handling best practices

## Requirements
Ensure that you have Python installed on your system. You can download the latest version of Python from the official Python website: 
```https://www.python.org/downloads/```
Code Editor or IDE: Choose a code editor or Integrated Development Environment (IDE) for writing and running your Python code. Some popular choices include Vim, Emacs, Visual Studio Code, PyCharm, Atom, Sublime Text, or Jupyter Notebook.

## Getting Started
To get started with the exercises and examples in this repository, follow these steps:
1. Clone the repository to your local machine:

   ```
   git clone https://github.com/your-username/0x05-python-exceptions.git
   ```
2. Navigate to the cloned repository:
   ```
   cd 0x05-python-exceptions
   ```
3. Explore the files and directories related to different topics and exercises.
4. Open the files in your preferred Python editor or IDE.
5. Follow the instructions provided in each file to complete the exercises and learn about exception handling in Python.

## Task & Files
* **[0-safe_print_list.py](./0-safe_print_list.py)** - Write a function that prints `x` elements of a list.
   * Prototype: `def safe_print_list(my_list=[], x=0):`
   * `my_list` can contain any type (integer, string, etc.)
   * All elements must be printed on the same line followed by a new line.
   * `x` represents the number of elements to print
   * `x` can be bigger than the length of my_list
   * Returns the real number of elements printed
   * You have to use `try: / except:`
   * You are not allowed to import any module
   * You are not allowed to use `len()`

* **[1-safe_print_integer.py](./1-safe_print_integer.py)** - Write a function that prints an integer with `"{:d}".format()`.
   * Prototype: `def safe_print_integer(value):`
   * `value` can be any type (integer, string, etc.)
   * The integer should be printed followed by a new line
   * Returns `True` if `value` has been correctly printed (it means the `value` is an integer)
   * Otherwise, returns `False`
   * You have to use `try: / except:`
   * You have to use `"{:d}".format()` to print as integer
   * You are not allowed to import any module
   * You are not allowed to use `type()`

* **[2-safe_print_list_integers](./2-safe_print_list_integers.py)** - Write a function that prints the first `x` elements of a list and only integers.
   * Prototype: `def safe_print_list_integers(my_list=[], x=0):`
   * `my_list` can contain any type (integer, string, etc.)
   * All integers have to be printed on the same line followed by a new line - other type of value in the list must be skipped (in silence).
   * `x` represents the number of elements to access in `my_list`
   * `x` can be bigger than the length of `my_list` - if it’s the case, an exception is expected to occur
   * Returns the real number of integers printed
   * You have to use `try: / except:`
   * You have to use `"{:d}".format()` to print an integer
   * You are not allowed to import any module
   * You are not allowed to use `len()`

## Contributing
Contributions to this repository are welcome! If you have any suggestions, improvements, or additional exercises related to exception handling in Python, please feel free to submit a pull request.

To contribute to this repository, follow these steps:

1. Fork the repository.
2. Create a new branch for your contribution:
   ```
   git checkout -b your-branch-name
   ```
3. Make your changes and additions.
4. Commit your changes:
   ```
   git commit -m "Your commit message"
   ```
5. Push your changes to your forked repository:
   ```
   git push origin your-branch-name
   ```
6. Open a pull request from your forked repository to this repository. Your contribution will be reviewed, and once accepted, it will be merged into the main branch of this repository.

## Authors
This project is authored by **Oluwatobiloba Light**. Feel free to reach out with any questions or suggestions. :)