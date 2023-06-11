# 0x03. Python - Data Structures: Lists, Tuples
This repository contains solutions to the assignments and projects of the 0x03. Python - Data Structures: Lists, Tuples module in the curriculum of the ALX.

## Description
This module focuses on the fundamental concepts of working with lists and tuples in Python. It covers various topics such as creating and manipulating lists, accessing list elements, slicing lists, iterating over lists, modifying lists, working with tuples, list comprehensions, and more. The module provides a comprehensive understanding of data structures and their operations, enhancing the knowledge and skills required for Python programming.

* **[0-print_list_integer.py](./0-print_list_integer.py)** - Write a function that prints all integers of a list.
	* Prototype: `def print_list_integer(my_list=[]):`
	* Format: one integer per line. See example
	* You are not allowed to import any module
	* You can assume that the list only contains integers
	* You are not allowed to cast integers into strings
	* You have to use `str.format()` to print integers

* **[1-element_at.py](./1-element_at.py)** - Write a function that retrieves an element from a list like in C.
	* Prototype: `def element_at(my_list, idx):`
	* If `idx` is negative, the function should return `None`
	* If `idx` is out of range (> of number of element in `my_list`), the function should return `None`
	* You are not allowed to import any module
	* You are not allowed to use `try/except`