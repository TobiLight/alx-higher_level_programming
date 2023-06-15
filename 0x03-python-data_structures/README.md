# 0x03. Python - Data Structures: Lists, Tuples
This repository contains solutions to the assignments and projects of the 0x03. Python - Data Structures: Lists, Tuples module in the curriculum of the ALX.

## Description
This module focuses on the fundamental concepts of working with lists and tuples in Python. It covers various topics such as creating and manipulating lists, accessing list elements, slicing lists, iterating over lists, modifying lists, working with tuples, list comprehensions, and more. The module provides a comprehensive understanding of data structures and their operations, enhancing the knowledge and skills required for Python programming.

## Requirements

The Python scripts are written using Python 3. They may have dependencies on other modules or libraries, which are mentioned in each script's header comment.

## Usage

To run any of the Python scripts, use the following command:

```
python3 filename.py
```

For VSCode (assuming you have python installed):

```
python filename.py
```

## Tasks & Files
* **[tests](./tests)** - Contains all the test files for the project.
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

* **[2-replace_in_list.py](./2-replace_in_list.py)** - Write a function that replaces an element of a list at a specific position (like in C).
  * Prototype: `def replace_in_list(my_list, idx, element):`
  * If `idx` is negative, the function should not modify anything, and returns the original list
  * If `idx` is out of range (> of number of element in `my_list`), the function should not modify anything, and returns the original list
  * You are not allowed to import any module
  * You are not allowed to use `try/except`

* **[3-print_reversed_list_integer.py](./3-print_reversed_list_integer.py)** - Write a function that prints all integers of a list, in reverse order.
  * Prototype: `def print_reversed_list_integer(my_list=[]):`
  * Format: one integer per line. See example
  * You are not allowed to import any module
  * You can assume that the list only contains integers
  * You are not allowed to cast integers into strings
  * You have to use `str.format()` to print integers

* **[4-new_in_list.py](./4-new_in_list.py)** - Write a function that replaces an element in a list at a specific position without modifying the original list (like in C).
  * Prototype: `def new_in_list(my_list, idx, element):`
  * If `idx` is negative, the function should return a copy of the original list`
  * If `idx` is out of range (> of number of element in `my_list`), the function should return a copy of the original `list`
  * You are not allowed to import any module
  * You are not allowed to use `try/except`

* **[5-no_c.py](./5-no_c.py)** - Write a function that removes all characters `c` and `C` from a string.
  * Prototype: `def no_c(my_string):`
  * The function should return the new string
  * You are not allowed to import any module
  * You are not allowed to use `str.replace()`

* **[6-print_matrix_integer.py](./6-print_matrix_integer.py)** - Write a function that prints a matrix of integers.
  * Prototype: `def print_matrix_integer(matrix=[[]]):`
  * Format: see example
  * You are not allowed to import any module
  * You can assume that the list only contains integers
  * You are not allowed to cast integers into strings
  * You have to use `str.format()` to print integers

* **[7-add_tuple.py](./7-add_tuple.py)** - Write a function that adds 2 tuples.
  * Prototype: `def add_tuple(tuple_a=(), tuple_b=()):`
  * Returns a tuple with 2 integers:
    * The first element should be the addition of the first element of each argument
    * The second element should be the addition of the second element of each argument
  * You are not allowed to import any module
  * You can assume that the two tuples will only contain integers
  * If a tuple is smaller than 2, use the value `0` for each missing integer
  * If a tuple is bigger than 2, use only the first 2 integers

* **[8-multiple_returns.py](./8-multiple_returns.py)** - Write a function that returns a tuple with the length of a string and its first character.
  * Prototype: `def multiple_returns(sentence):`
  * If the sentence is empty, the first character should be equal to `None`
  * You are not allowed to import any module

* **[9-max_integer.py](./9-max_integer.py)** - Write a function that finds the biggest integer of a list.
  * Prototype: `def max_integer(my_list=[]):`
  * If the list is empty, return `None`
  * You can assume that the list only contains integers
  * You are not allowed to import any module
  * You are not allowed to use the builtin `max()`

* **[10-divisible_by_2.py](./10-divisible_by_2.py)** - Write a function that finds all multiples of 2 in a list.
  * Prototype: `def divisible_by_2(my_list=[]):`
  * Return a new list with `True` or `False`, depending on whether the integer at the same position in the original list is a multiple of 2
  * The new list should have the same size as the original list
  * You are not allowed to import any module

* **[11-delete_at.py](./11-delete_at.py)** - Write a function that deletes the item at a specific position in a list.
  * Prototype: `def delete_at(my_list=[], idx=0):`
  * If `idx` is negative or out of range, nothing change (returns the same list)
  * You are not allowed to use `pop()`
  * You are not allowed to import any module

* **[12-switch.py](./12-switch.py)** - Complete the source code in order to switch value of `a` and `b`
  * You can find the source code [here](https://intranet.alxswe.com/rltoken/9kg8R2hfPSN5pClcVAeGlA)
  * Your code should be inserted where the comment is (line 4)
  * Your program should be exactly 5 lines long

* **[13-is_palindrome.c](./13-is_palindrome.c)**, **[lists.h](./lists.h)**  
**Technical interview preparation:**
  * You are not allowed to google anything
  * Whiteboard first
  #### Write a function in C that checks if a singly linked list is a palindrome.
  * Prototype: `int is_palindrome(listint_t **head);`
  * Return: `0` if it is not a palindrome, `1` if it is a palindrome
  * An empty list is considered a palindrome

* **[100-print_python_list_info.c](./100-print_python_list_info.c)**
  #### CPython is the reference implementation of the Python programming language. Written in C, CPython is the default and most widely used implementation of the language. Since we now know a bit of C, we can look at what is happening under the hood of Python. Let’s have fun with Python and C, and let’s look at what makes Python so easy to use.
  * All your files will be interpreted/compiled on Ubuntu 14.04 LTS

  ![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/7e7834b535261d05532fb80a9304f7051c4ad7ac.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230615%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230615T110354Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=915fa45896ca1bb3d4748b932e2a968ab3fbea4b7fb433923b603b138344de8f)

  #### Create a C function that prints some basic info about Python lists.
  * Prototype: `void print_python_list_info(PyObject *p);`
  * Format: see example
  * Python version: 3.4
  * Your shared library will be compiled with this command line: `gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,PyList -o libPyList.so -fPIC -I/usr/include/python3.4 100-print_python_list_info.c`
  * OS: `Ubuntu 14.04 LTS`
  * Start by reading:
    * listobject.h
    * object.h
    * [Common Object Structures](https://intranet.alxswe.com/rltoken/jmRTk4m1VSzjsu3QTGaC6w)
    * [List Objects](https://intranet.alxswe.com/rltoken/7V1HlQRESjCqrKrw_O_Urw)

## Author
This project is authored by **Oluwatobiloba Light**. Feel free to reach out with any questions or suggestions. :)