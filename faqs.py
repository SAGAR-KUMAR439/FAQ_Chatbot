import string
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS


def preprocess(text):
    text = text.lower()

    text = text.translate(
        str.maketrans("", "", string.punctuation)
    )

    words = text.split()

    python_keywords = {
        "for",
        "while",
        "if",
        "else",
        "elif",
        "in",
        "is",
        "not",
        "and",
        "or",
        "class",
        "from",
        "as",
        "with",
        "try",
        "except",
        "finally",
        "return",
        "pass",
        "break",
        "continue"
    }

    words = [
        word for word in words
        if word not in ENGLISH_STOP_WORDS
        or word in python_keywords
    ]

    stemmer = PorterStemmer()

    stemmed_words = []

    for word in words:
        stemmed_words.append(stemmer.stem(word))

    return " ".join(stemmed_words)
faqs = [
    {
    "question": "What is Python?",
    "answer": "Python is a high-level programming language."
    },
    {
    "question": "Can you tell me about Python?",
    "answer": "Python is a high-level programming language."
    },
    {
    "question": "Tell me about Python",
    "answer": "Python is a high-level programming language."
    },
    {
    "question": "Explain Python",
    "answer": "Python is a high-level programming language."
    },
    {
    "question": "How can I install Python?",
    "answer": "You can install Python from the official Python website and follow the installation instructions for your operating system."
    },
    {
    "question": "How do I install Python?",
    "answer": "You can install Python from the official Python website and follow the installation instructions for your operating system."
    },
    {
        "question": "What is a variable in Python?",
        "answer": "A variable is a name used to store a value in Python."
    },
    {
    "question": "What are functions in Python?",
    "answer": "A function is a reusable block of code that performs a specific task."
    },
    {
        "question": "What is a list in Python?",
        "answer": "A list is a collection used to store multiple values in Python."
    },
    {
        "question": "What is a tuple in Python?",
        "answer": "A tuple is an ordered collection of values that cannot be changed after creation."
    },
    {
        "question": "What is a dictionary in Python?",
        "answer": "A dictionary stores data in key-value pairs."
    },
    {
        "question": "What is a loop in Python?",
        "answer": "A loop is used to repeatedly execute a block of code."
    },
    {
        "question": "What is an if statement in Python?",
        "answer": "An if statement is used to execute code when a specified condition is true."
    },
        {
        "question": "What are data types in Python?",
        "answer": "Data types define the kind of value that a variable can store, such as integer, float, string, and boolean."
    },
    {
        "question": "What is a string in Python?",
        "answer": "A string is a sequence of characters enclosed in quotes."
    },
    {
        "question": "What is an integer in Python?",
        "answer": "An integer is a whole number without a decimal point."
    },
    {
        "question": "What is a float in Python?",
        "answer": "A float is a number that contains a decimal point."
    },
    {
        "question": "What is a boolean in Python?",
        "answer": "A boolean represents one of two values: True or False."
    },
    {
        "question": "What are operators in Python?",
        "answer": "Operators are symbols used to perform operations on values and variables."
    },
    {
        "question": "What is a for loop in Python?",
        "answer": "A for loop is used to iterate over items in a sequence or other iterable."
    },
    {
        "question": "What is a while loop in Python?",
        "answer": "A while loop repeatedly executes a block of code while a condition is true."
    },
    {
        "question": "What is a module in Python?",
        "answer": "A module is a Python file containing code such as functions, classes, and variables that can be reused."
    },
    {
        "question": "What is an exception in Python?",
        "answer": "An exception is an error or unexpected event that occurs while a program is running."
    },
        {
        "question": "What is a comment in Python?",
        "answer": "A comment is text written in a Python program to explain code and is ignored by the Python interpreter."
    },
    {
        "question": "What is indentation in Python?",
        "answer": "Indentation is the whitespace at the beginning of a line that Python uses to define blocks of code."
    },
    {
        "question": "What are keywords in Python?",
        "answer": "Keywords are reserved words in Python that have special meanings and cannot normally be used as variable names."
    },
    {
        "question": "What is a constant in Python?",
        "answer": "A constant is a value that is intended to remain unchanged throughout a program. Python does not enforce constants, but uppercase names are commonly used to represent them."
    },
    {
        "question": "What is type casting in Python?",
        "answer": "Type casting is the process of converting a value from one data type to another."
    },
    {
        "question": "What is input in Python?",
        "answer": "The input function is used to receive data from the user through the keyboard."
    },
    {
        "question": "What is print in Python?",
        "answer": "The print function is used to display text, values, or other output on the screen."
    },
    {
        "question": "What is None in Python?",
        "answer": "None is a special Python value that represents the absence of a value or no value."
    },
        {
        "question": "What is a set in Python?",
        "answer": "A set is an unordered collection of unique values in Python."
    },
    {
        "question": "What is a dictionary in Python?",
        "answer": "A dictionary is a collection of key-value pairs."
    },
    {
        "question": "What is a mutable object in Python?",
        "answer": "A mutable object can be changed after it is created."
    },
    {
        "question": "What is an immutable object in Python?",
        "answer": "An immutable object cannot be changed after it is created."
    },
    {
        "question": "What is a sequence in Python?",
        "answer": "A sequence is an ordered collection of elements, such as a string, list, or tuple."
    },
    {
        "question": "How do you check the type of a value in Python?",
        "answer": "The type function is used to determine the data type of a value."
    },
    {
        "question": "What is a list in Python used for?",
        "answer": "A list is used to store multiple values in an ordered and changeable collection."
    },
    {
        "question": "What is a tuple in Python used for?",
        "answer": "A tuple is used to store multiple values in an ordered collection that cannot be changed."
    },
        {
        "question": "What is an arithmetic operator in Python?",
        "answer": "Arithmetic operators are used to perform mathematical operations such as addition, subtraction, multiplication, and division."
    },
    {
        "question": "What is a comparison operator in Python?",
        "answer": "Comparison operators are used to compare two values and return a Boolean result."
    },
    {
        "question": "What is a logical operator in Python?",
        "answer": "Logical operators are used to combine or modify conditions. Python provides and, or, and not."
    },
    {
        "question": "What is the assignment operator in Python?",
        "answer": "The assignment operator is used to assign a value to a variable."
    },
    {
        "question": "What does the plus operator do in Python?",
        "answer": "The plus operator is used for addition with numbers and can also concatenate strings."
    },
    {
        "question": "What does the modulus operator do in Python?",
        "answer": "The modulus operator returns the remainder after dividing one number by another."
    },
    {
        "question": "What does the equality operator do in Python?",
        "answer": "The equality operator checks whether two values are equal and returns True or False."
    },
    {
        "question": "What does the not operator do in Python?",
        "answer": "The not operator reverses a Boolean condition. True becomes False and False becomes True."
    },
        {
        "question": "What is an if statement in Python?",
        "answer": "An if statement is used to execute code when a specified condition is true."
    },
    {
        "question": "What is an elif statement in Python?",
        "answer": "An elif statement checks another condition when the previous if or elif conditions are false."
    },
    {
        "question": "What is an else statement in Python?",
        "answer": "An else statement executes a block of code when all preceding if and elif conditions are false."
    },
    {
        "question": "What is a for loop in Python?",
        "answer": "A for loop is used to iterate over items in a sequence or other iterable."
    },
    {
        "question": "What is a while loop in Python?",
        "answer": "A while loop repeatedly executes a block of code while a condition is true."
    },
    {
        "question": "What does break do in Python?",
        "answer": "The break statement immediately terminates the nearest loop."
    },
    {
        "question": "What does continue do in Python?",
        "answer": "The continue statement skips the remaining code in the current loop iteration and moves to the next iteration."
    },
    {
        "question": "What does pass do in Python?",
        "answer": "The pass statement does nothing and is used as a placeholder where a statement is required."
    },
    {
    "question": "What is a function in Python?",
    "answer": "A function is a reusable block of code that performs a specific task."
    },
   {
    "question": "What is a parameter in Python?",
    "answer": "A parameter is a variable listed in a function definition that receives a value when the function is called."
    },
    {
    "question": "What is an argument in Python?",
    "answer": "An argument is a value passed to a function when the function is called."
    },
    {
    "question": "What is a return statement in Python?",
    "answer": "A return statement is used to send a value back from a function."
    },
    {
    "question": "What is a default parameter in Python?",
    "answer": "A default parameter is a parameter that has a predefined value used when no argument is provided."
    },
    {
    "question": "What is a function call in Python?",
    "answer": "A function call is the process of executing a function by writing its name followed by parentheses."
    },
    {
    "question": "What is a positional argument in Python?",
    "answer": "A positional argument is an argument passed to a function based on the position of the parameter."
    },
    {
    "question": "What is a keyword argument in Python?",
    "answer": "A keyword argument is an argument passed to a function by explicitly specifying the parameter name."
    },
    {
    "question": "What is a local variable in Python?",
    "answer": "A local variable is a variable created inside a function and normally accessible only within that function."
    },
    {
    "question": "What is a global variable in Python?",
    "answer": "A global variable is a variable defined outside functions and can be accessed from different parts of a program."
    },
    {
    "question": "What is recursion in Python?",
    "answer": "Recursion is a technique where a function calls itself to solve a problem."
    },
    {
    "question": "What is a lambda function in Python?",
    "answer": "A lambda function is a small anonymous function that can be defined using the lambda keyword."
    },
    {
    "question": "What is a nested function in Python?",
    "answer": "A nested function is a function defined inside another function."
    },
    {
    "question": "What is a docstring in Python?",
    "answer": "A docstring is a string used to document a function, class, or module."
    },
    {
    "question": "What is a higher-order function in Python?",
    "answer": "A higher-order function is a function that takes another function as an argument or returns a function."
    },
    {
    "question": "What are *args in Python?",
    "answer": "*args allows a function to accept a variable number of positional arguments."
    },
    {
    "question": "What are **kwargs in Python?",
    "answer": "**kwargs allows a function to accept a variable number of keyword arguments."
    },
    {
    "question": "What is variable scope in Python?",
    "answer": "Variable scope defines the part of a program where a variable can be accessed."
    },
    {
    "question": "What is the scope of a local variable in Python?",
    "answer": "A local variable can normally be accessed only inside the function where it is defined."
    },
    {
    "question": "What is the scope of a global variable in Python?",
    "answer": "A global variable can be accessed from different parts of the program, including inside functions."
    },
        # =========================
    # PYTHON BASICS
    # =========================

    {
        "question": "What is Python used for?",
        "answer": "Python is used for web development, automation, data analysis, artificial intelligence, machine learning, scripting, and many other applications."
    },
    {
        "question": "Why is Python popular?",
        "answer": "Python is popular because it has simple syntax, a large ecosystem of libraries, and is useful for many areas of software development."
    },
    {
        "question": "Why should I learn Python?",
        "answer": "Python is beginner-friendly and widely used in software development, automation, data science, artificial intelligence, and machine learning."
    },
    {
        "question": "What are the advantages of Python?",
        "answer": "Python has readable syntax, a large standard library, many third-party packages, and supports many areas of programming."
    },
    {
        "question": "Is Python easy to learn?",
        "answer": "Python is generally considered beginner-friendly because its syntax is relatively simple and readable."
    },
    {
        "question": "What is Python syntax?",
        "answer": "Python syntax is the set of rules used to write valid Python programs."
    },
    {
        "question": "What is a Python program?",
        "answer": "A Python program is a collection of Python statements that are executed by the Python interpreter."
    },
    {
        "question": "What is the Python interpreter?",
        "answer": "The Python interpreter executes Python code and converts it into instructions that the computer can execute."
    },
    {
        "question": "What is a comment in Python?",
        "answer": "A comment is text written in source code to explain the code and is ignored during program execution."
    },
    {
        "question": "How do you write a comment in Python?",
        "answer": "A single-line Python comment starts with the # symbol."
    },

    # =========================
    # VARIABLES
    # =========================

    {
        "question": "What is a variable in Python?",
        "answer": "A variable is a name used to store or reference a value in Python."
    },
    {
        "question": "How do you create a variable in Python?",
        "answer": "You create a variable by assigning a value to a name using the assignment operator."
    },
    {
        "question": "What is variable assignment?",
        "answer": "Variable assignment means giving a value to a variable using the assignment operator."
    },
    {
        "question": "Can a Python variable change its value?",
        "answer": "Yes. A variable can be assigned a different value during program execution."
    },
    {
        "question": "What are variable naming rules in Python?",
        "answer": "Python variable names can contain letters, digits, and underscores, cannot start with a digit, and should not use reserved keywords."
    },
    {
        "question": "What is multiple assignment in Python?",
        "answer": "Multiple assignment allows several variables to be assigned values in a single statement."
    },

    # =========================
    # DATA TYPES
    # =========================

    {
        "question": "What are data types in Python?",
        "answer": "Python data types describe the kind of value stored or referenced by an object, such as integers, strings, lists, tuples, sets, and dictionaries."
    },
    {
        "question": "What is an integer in Python?",
        "answer": "An integer is a whole number without a fractional part, such as 10, -5, or 0."
    },
    {
        "question": "What is a float in Python?",
        "answer": "A float is a number that contains a decimal or fractional part."
    },
    {
        "question": "What is a boolean in Python?",
        "answer": "A boolean represents one of two values: True or False."
    },
    {
        "question": "What is None in Python?",
        "answer": "None is a special Python value that represents the absence of a value."
    },
    {
        "question": "How do you check the type of a value in Python?",
        "answer": "You can use the type() function to determine the type of a value."
    },
    {
        "question": "What does type do in Python?",
        "answer": "The type() function returns the type or class of an object."
    },

    # =========================
    # TYPE CASTING
    # =========================

    {
        "question": "What is type casting in Python?",
        "answer": "Type casting means converting a value from one data type to another."
    },
    {
        "question": "How do you convert a string to an integer?",
        "answer": "You can use the int() function to convert a suitable string into an integer."
    },
    {
        "question": "How do you convert an integer to a string?",
        "answer": "You can use the str() function to convert an integer into a string."
    },
    {
        "question": "How do you convert a number to a float?",
        "answer": "You can use the float() function to convert a suitable number or string into a floating-point value."
    },

    # =========================
    # STRINGS
    # =========================

    {
        "question": "What is a string in Python?",
        "answer": "A string is a sequence of characters represented by text enclosed in quotes."
    },
    {
        "question": "How do you create a string in Python?",
        "answer": "You can create a string by placing text inside single quotes, double quotes, or triple quotes."
    },
    {
        "question": "What is string indexing?",
        "answer": "String indexing is the process of accessing individual characters using their position."
    },
    {
        "question": "What is string slicing?",
        "answer": "String slicing extracts a portion of a string using a range of indexes."
    },
    {
        "question": "Are Python strings mutable?",
        "answer": "No. Python strings are immutable, meaning their contents cannot be changed in place."
    },
    {
        "question": "How do you convert a string to lowercase?",
        "answer": "You can use the lower() method."
    },
    {
        "question": "How do you convert a string to uppercase?",
        "answer": "You can use the upper() method."
    },
    {
        "question": "How do you remove whitespace from a string?",
        "answer": "You can use the strip() method to remove leading and trailing whitespace."
    },
    {
        "question": "What does split do in Python?",
        "answer": "The split() method divides a string into a list of substrings."
    },
    {
        "question": "What does join do in Python?",
        "answer": "The join() method combines elements of an iterable into a string using a separator."
    },

    # =========================
    # LISTS
    # =========================

    {
        "question": "What is a list in Python?",
        "answer": "A list is an ordered and mutable collection that can store multiple values."
    },
    {
        "question": "What is a Python list used for?",
        "answer": "A list is used to store multiple values in an ordered and changeable collection."
    },
    {
        "question": "Are Python lists mutable?",
        "answer": "Yes. Python lists are mutable, so their elements can be changed after creation."
    },
    {
        "question": "How do you add an item to a list?",
        "answer": "You can use the append() method to add an item to the end of a list."
    },
    {
        "question": "What does append do in Python?",
        "answer": "The append() method adds one item to the end of a list."
    },
    {
        "question": "What does remove do in a list?",
        "answer": "The remove() method removes the first matching value from a list."
    },
    {
        "question": "What does pop do in a list?",
        "answer": "The pop() method removes and returns an item from a list, usually the last item by default."
    },
    {
        "question": "How do you sort a list?",
        "answer": "You can use the sort() method to sort a list in place."
    },
    {
        "question": "How do you find the length of a list?",
        "answer": "You can use the len() function to find the number of items in a list."
    },

    # =========================
    # TUPLES
    # =========================

    {
        "question": "What is a tuple in Python?",
        "answer": "A tuple is an ordered collection that is immutable after creation."
    },
    {
        "question": "What is a tuple used for?",
        "answer": "A tuple is useful for storing an ordered collection of values that should not be changed."
    },
    {
        "question": "Are tuples mutable?",
        "answer": "No. Tuples are immutable."
    },
    {
        "question": "What is the difference between a list and a tuple?",
        "answer": "Lists are mutable, while tuples are immutable."
    },

    # =========================
    # SETS
    # =========================

    {
        "question": "What is a set in Python?",
        "answer": "A set is an unordered collection of unique elements."
    },
    {
        "question": "What is a set used for?",
        "answer": "Sets are useful for storing unique values and performing mathematical set operations."
    },
    {
        "question": "Can a set contain duplicate values?",
        "answer": "No. A set automatically stores only unique values."
    },
    {
        "question": "How do you add an item to a set?",
        "answer": "You can use the add() method to add an item to a set."
    },

    # =========================
    # DICTIONARIES
    # =========================

    {
        "question": "What is a dictionary in Python?",
        "answer": "A dictionary is a collection that stores data as key-value pairs."
    },
    {
        "question": "What is a dictionary used for?",
        "answer": "Dictionaries are useful for storing and retrieving values using keys."
    },
    {
        "question": "How do you access a dictionary value?",
        "answer": "You can access a dictionary value using its key."
    },
    {
        "question": "Can dictionary keys be duplicated?",
        "answer": "Dictionary keys must be unique within a dictionary."
    },
    {
        "question": "How do you add an item to a dictionary?",
        "answer": "You can assign a value to a new key or use dictionary methods such as update()."
    },

    # =========================
    # OPERATORS
    # =========================

    {
        "question": "What are operators in Python?",
        "answer": "Operators are symbols or keywords used to perform operations on values and variables."
    },
    {
        "question": "What is an arithmetic operator in Python?",
        "answer": "Arithmetic operators perform mathematical operations such as addition, subtraction, multiplication, division, and modulus."
    },
    {
        "question": "What is a comparison operator in Python?",
        "answer": "Comparison operators compare values and produce a Boolean result."
    },
    {
        "question": "What is a logical operator in Python?",
        "answer": "Logical operators such as and, or, and not are used to combine or negate Boolean conditions."
    },
    {
        "question": "What does the modulus operator do in Python?",
        "answer": "The modulus operator returns the remainder after division."
    },
    {
        "question": "What does the exponent operator do?",
        "answer": "The exponentiation operator ** raises one number to the power of another."
    },
    {
        "question": "What is the assignment operator?",
        "answer": "The assignment operator = assigns a value to a variable."
    },

    # =========================
    # CONDITIONALS
    # =========================

    {
        "question": "What is an if statement in Python?",
        "answer": "An if statement executes a block of code when a specified condition is true."
    },
    {
        "question": "What is an elif statement in Python?",
        "answer": "An elif statement checks another condition when previous if or elif conditions were false."
    },
    {
        "question": "What is an else statement in Python?",
        "answer": "An else block executes when none of the preceding conditions are true."
    },
    {
        "question": "What is conditional logic?",
        "answer": "Conditional logic allows a program to execute different code depending on whether conditions are true or false."
    },

    # =========================
    # LOOPS
    # =========================

    {
        "question": "What is a loop in Python?",
        "answer": "A loop repeatedly executes a block of code."
    },
    {
        "question": "What is looping in Python?",
        "answer": "Looping is the process of repeatedly executing code using constructs such as for and while loops."
    },
    {
        "question": "What is a for loop?",
        "answer": "A for loop iterates over items in an iterable such as a list, string, tuple, or range."
    },
    {
        "question": "What is a while loop?",
        "answer": "A while loop repeatedly executes code while a condition remains true."
    },
    {
        "question": "What does break do in Python?",
        "answer": "The break statement immediately exits the nearest loop."
    },
    {
        "question": "What does continue do in Python?",
        "answer": "The continue statement skips the remaining code in the current loop iteration and moves to the next iteration."
    },
    {
        "question": "What does pass do in Python?",
        "answer": "The pass statement does nothing and is commonly used as a placeholder."
    },
    {
        "question": "What is range in Python?",
        "answer": "The range() function produces a sequence of numbers commonly used for iteration."
    },

    # =========================
    # FUNCTIONS
    # =========================

    {
        "question": "What is a function in Python?",
        "answer": "A function is a reusable block of code that performs a specific task."
    },
    {
        "question": "Why are functions useful in Python?",
        "answer": "Functions make programs easier to organize, reuse, test, and maintain."
    },
    {
        "question": "Why do we use functions in Python?",
        "answer": "Functions allow code to be organized into reusable blocks that perform specific tasks."
    },
    {
        "question": "What does a function do?",
        "answer": "A function performs a specific task when it is called."
    },
    {
        "question": "What is a function parameter?",
        "answer": "A parameter is a variable defined in a function that receives a value when the function is called."
    },
    {
        "question": "What is a function argument?",
        "answer": "An argument is a value passed to a function when the function is called."
    },
    {
        "question": "What is a return statement?",
        "answer": "A return statement sends a value back from a function to the code that called it."
    },
    {
        "question": "What is a function call?",
        "answer": "A function call is an expression that executes a function."
    },
    {
        "question": "What is a default parameter?",
        "answer": "A default parameter has a predefined value that is used when the caller does not provide an argument."
    },
    {
        "question": "What are positional arguments?",
        "answer": "Positional arguments are matched to function parameters based on their position."
    },
    {
        "question": "What are keyword arguments?",
        "answer": "Keyword arguments pass values to function parameters by explicitly naming the parameters."
    },
    {
        "question": "What is recursion in Python?",
        "answer": "Recursion is a technique in which a function calls itself to solve a problem."
    },
    {
        "question": "What is a lambda function?",
        "answer": "A lambda function is a small anonymous function created using the lambda keyword."
    },
    {
        "question": "What is a nested function?",
        "answer": "A nested function is a function defined inside another function."
    },
    {
        "question": "What is a docstring?",
        "answer": "A docstring is a string used to document a function, class, or module."
    },
    {
        "question": "What is a higher-order function?",
        "answer": "A higher-order function is a function that takes another function as an argument or returns a function."
    },

    # =========================
    # MODULES AND PACKAGES
    # =========================

    {
        "question": "What is a module in Python?",
        "answer": "A module is a Python file containing code such as functions, classes, and variables that can be imported."
    },
    {
        "question": "What is a package in Python?",
        "answer": "A package is a collection of related Python modules organized in a directory."
    },
    {
        "question": "What is the import statement?",
        "answer": "The import statement allows a Python program to use code from another module."
    },
    {
        "question": "What is the difference between a module and a package?",
        "answer": "A module is typically a single Python file, while a package organizes multiple modules into a directory structure."
    },
    {
        "question": "What is pip?",
        "answer": "pip is the package installer commonly used to install and manage Python packages."
    },
    {
        "question": "How do you install a Python package?",
        "answer": "You can commonly install a Python package using pip from the command line."
    },

    # =========================
    # FILE HANDLING
    # =========================

    {
        "question": "What is file handling in Python?",
        "answer": "File handling allows Python programs to create, read, write, append, and manage files."
    },
    {
        "question": "How do you open a file in Python?",
        "answer": "You can use the open() function to open a file."
    },
    {
        "question": "What is the open function?",
        "answer": "The open() function opens a file and returns a file object."
    },
    {
        "question": "How do you read a file in Python?",
        "answer": "You can use methods such as read(), readline(), or readlines() on a file object."
    },
    {
        "question": "How do you write to a file in Python?",
        "answer": "You can open a file in an appropriate write mode and use the write() method."
    },
    {
        "question": "What is the with statement used for with files?",
        "answer": "The with statement automatically manages the file resource and helps ensure the file is properly closed."
    },

    # =========================
    # EXCEPTIONS
    # =========================

    {
        "question": "What is an exception in Python?",
        "answer": "An exception is an event that occurs during program execution and interrupts the normal flow of the program."
    },
    {
        "question": "What is exception handling?",
        "answer": "Exception handling is the process of detecting and handling runtime errors using constructs such as try and except."
    },
    {
        "question": "What is try except in Python?",
        "answer": "try and except are used to handle exceptions that may occur during execution."
    },
    {
        "question": "What is finally in Python?",
        "answer": "The finally block runs after the try and except processing, whether or not an exception occurred."
    },
    {
        "question": "What does raise do in Python?",
        "answer": "The raise statement is used to explicitly raise an exception."
    },
    {
        "question": "What is a syntax error?",
        "answer": "A syntax error occurs when Python code does not follow the language's syntax rules."
    },
    {
        "question": "What is a runtime error?",
        "answer": "A runtime error occurs while a program is executing."
    },

    # =========================
    # OBJECT ORIENTED PROGRAMMING
    # =========================

    {
        "question": "What is object oriented programming?",
        "answer": "Object-oriented programming is a programming paradigm that organizes software around objects and classes."
    },
    {
        "question": "What is a class in Python?",
        "answer": "A class is a blueprint for creating objects and defining their data and behavior."
    },
    {
        "question": "What is an object in Python?",
        "answer": "An object is an instance of a class that contains data and behavior."
    },
    {
        "question": "What is a constructor in Python?",
        "answer": "The __init__ method is commonly used to initialize an object's attributes when an object is created."
    },
    {
        "question": "What is inheritance in Python?",
        "answer": "Inheritance allows a class to derive attributes and methods from another class."
    },
    {
        "question": "What is encapsulation?",
        "answer": "Encapsulation is the practice of bundling data and methods together and controlling how they are accessed."
    },
    {
        "question": "What is polymorphism?",
        "answer": "Polymorphism allows different objects to provide different implementations of a common interface or operation."
    },
    {
        "question": "What is abstraction?",
        "answer": "Abstraction focuses on exposing essential functionality while hiding unnecessary implementation details."
    },
    {
        "question": "What is method overriding?",
        "answer": "Method overriding occurs when a subclass provides its own implementation of a method inherited from a parent class."
    },

    # =========================
    # ITERATORS AND GENERATORS
    # =========================

    {
        "question": "What is an iterator in Python?",
        "answer": "An iterator is an object that produces values one at a time and implements the iterator protocol."
    },
    {
        "question": "What is an iterable in Python?",
        "answer": "An iterable is an object that can return its elements one at a time, usually through an iterator."
    },
    {
        "question": "What is a generator in Python?",
        "answer": "A generator is a special type of iterator that produces values lazily, often using the yield statement."
    },
    {
        "question": "What does yield do in Python?",
        "answer": "The yield statement produces a value from a generator and pauses its execution until the next value is requested."
    },

    # =========================
    # DECORATORS
    # =========================

    {
        "question": "What is a decorator in Python?",
        "answer": "A decorator is a function that modifies or extends the behavior of another function or callable."
    },
    {
        "question": "Why are decorators used?",
        "answer": "Decorators are used to add reusable behavior to functions or classes without changing their core implementation."
    },

    # =========================
    # SCOPE
    # =========================

    {
        "question": "What is variable scope?",
        "answer": "Variable scope determines where a variable can be accessed in a program."
    },
    {
        "question": "What is local scope?",
        "answer": "Local scope refers to variables that are accessible within the function where they are defined."
    },
    {
        "question": "What is global scope?",
        "answer": "Global scope refers to variables defined outside functions that can generally be accessed throughout the module."
    },
    {
        "question": "What does the global keyword do?",
        "answer": "The global keyword allows a function to refer to and modify a global variable."
    },

    # =========================
    # COMPREHENSIONS
    # =========================

    {
        "question": "What is a list comprehension?",
        "answer": "A list comprehension is a concise way to create a list from an iterable, optionally applying a condition."
    },
    {
        "question": "What is dictionary comprehension?",
        "answer": "A dictionary comprehension is a concise way to create a dictionary from an iterable."
    },
    {
        "question": "What is set comprehension?",
        "answer": "A set comprehension is a concise way to create a set from an iterable."
    },

    # =========================
    # DEBUGGING AND TESTING
    # =========================

    {
        "question": "What is debugging?",
        "answer": "Debugging is the process of finding and fixing errors or unexpected behavior in a program."
    },
    {
        "question": "What is a bug in programming?",
        "answer": "A bug is an error or defect in a program that causes incorrect or unexpected behavior."
    },
    {
        "question": "What is unit testing?",
        "answer": "Unit testing checks individual functions or components of a program to verify that they work correctly."
    },
    {
        "question": "What is pytest?",
        "answer": "pytest is a popular Python testing framework used to write and run automated tests."
    },

    # =========================
    # VIRTUAL ENVIRONMENTS
    # =========================

    {
        "question": "What is a virtual environment in Python?",
        "answer": "A virtual environment is an isolated Python environment used to manage project-specific packages and dependencies."
    },
    {
        "question": "Why use a virtual environment?",
        "answer": "Virtual environments help keep project dependencies isolated and prevent conflicts between projects."
    },
    {
        "question": "How do you create a virtual environment?",
        "answer": "You can create one using Python's built-in venv module."
    },

    # =========================
    # APIS AND WEB
    # =========================

    {
        "question": "What is an API?",
        "answer": "An API is an interface that allows different software systems to communicate with each other."
    },
    {
        "question": "What is HTTP?",
        "answer": "HTTP is a protocol used for communication between clients and web servers."
    },
    {
        "question": "What is a REST API?",
        "answer": "A REST API is a web API that commonly uses HTTP methods to work with resources."
    },
    {
        "question": "What is JSON?",
        "answer": "JSON is a lightweight text format commonly used for exchanging structured data between applications."
    },
    {
        "question": "What is a GET request?",
        "answer": "A GET request is commonly used to retrieve data from a server."
    },
    {
        "question": "What is a POST request?",
        "answer": "A POST request is commonly used to send data to a server for processing or resource creation."
    },

    # =========================
    # NUMPY
    # =========================

    {
        "question": "What is NumPy?",
        "answer": "NumPy is a Python library used for numerical computing and efficient operations on arrays."
    },
    {
        "question": "What is a NumPy array?",
        "answer": "A NumPy array is a multidimensional data structure designed for efficient numerical operations."
    },
    {
        "question": "Why is NumPy used?",
        "answer": "NumPy is used for efficient numerical computation, array operations, linear algebra, and scientific computing."
    },

    # =========================
    # PANDAS
    # =========================

    {
        "question": "What is Pandas?",
        "answer": "Pandas is a Python library used for data manipulation and analysis."
    },
    {
        "question": "What is a DataFrame?",
        "answer": "A DataFrame is a two-dimensional labeled data structure provided by Pandas."
    },
    {
        "question": "What is a Pandas Series?",
        "answer": "A Series is a one-dimensional labeled data structure in Pandas."
    },

    # =========================
    # AI AND MACHINE LEARNING BASICS
    # =========================

    {
        "question": "What is artificial intelligence?",
        "answer": "Artificial intelligence is the field of computing focused on building systems that can perform tasks that normally require aspects of human intelligence."
    },
    {
        "question": "What is machine learning?",
        "answer": "Machine learning is a field of artificial intelligence in which systems learn patterns from data to make predictions or decisions."
    },
    {
        "question": "What is deep learning?",
        "answer": "Deep learning is a branch of machine learning that uses neural networks with multiple layers to learn complex patterns."
    },
    {
        "question": "What is a neural network?",
        "answer": "A neural network is a machine learning model composed of interconnected computational units that learn patterns from data."
    },
    {
        "question": "What is supervised learning?",
        "answer": "Supervised learning trains a model using labeled examples where the expected output is known."
    },
    {
        "question": "What is unsupervised learning?",
        "answer": "Unsupervised learning finds patterns or structures in data without labeled target outputs."
    },
    {
        "question": "What is a training dataset?",
        "answer": "A training dataset is the data used by a machine learning model to learn patterns."
    },
    {
        "question": "What is a test dataset?",
        "answer": "A test dataset is used to evaluate how well a trained machine learning model performs on unseen data."
    },
    {
        "question": "What is a machine learning model?",
        "answer": "A machine learning model is a mathematical or computational representation learned from data to make predictions or decisions."
    },
        # =========================
    # Python Basics
    # =========================

    {
        "question": "What is a Python program?",
        "answer": "A Python program is a set of instructions written in Python that a Python interpreter executes."
    },
    {
        "question": "What is Python syntax?",
        "answer": "Python syntax is the set of rules that define how Python code should be written."
    },
    {
        "question": "Why is Python easy to learn?",
        "answer": "Python has simple, readable syntax and allows beginners to focus on programming concepts without excessive syntax."
    },
    {
        "question": "What are the advantages of Python?",
        "answer": "Python is readable, versatile, open source, supported by many libraries, and useful in web development, automation, data science, AI, and many other areas."
    },
    {
        "question": "What is an interpreter in Python?",
        "answer": "A Python interpreter executes Python code and translates it into instructions that the computer can run."
    },
    {
        "question": "What are comments in Python?",
        "answer": "Comments are notes written in code that are ignored by Python. A single-line comment starts with #."
    },
    {
        "question": "Why are comments used in Python?",
        "answer": "Comments help explain code and make programs easier to understand and maintain."
    },


    # =========================
    # Variables
    # =========================

    {
        "question": "How do you create a variable in Python?",
        "answer": "A variable is created by assigning a value to a name using the assignment operator."
    },
    {
        "question": "How do you assign a value to a variable?",
        "answer": "Use the equals sign to assign a value, such as x = 10."
    },
    {
        "question": "Can a Python variable change its value?",
        "answer": "Yes. A variable can be reassigned to another value during program execution."
    },
    {
        "question": "Can a Python variable store different types of values?",
        "answer": "Yes. Python variables can refer to values of different data types at different times."
    },
    {
        "question": "What are variable naming rules in Python?",
        "answer": "A variable name can contain letters, digits, and underscores, cannot start with a digit, and should not be a Python keyword."
    },
    {
        "question": "What is variable assignment?",
        "answer": "Variable assignment means giving a value to a variable using the assignment operator."
    },


    # =========================
    # Data Types
    # =========================

    {
        "question": "What are the main data types in Python?",
        "answer": "Common Python data types include int, float, str, bool, list, tuple, set, dictionary, and NoneType."
    },
    {
        "question": "What is an integer in Python?",
        "answer": "An integer is a whole number without a decimal part, such as 10, 0, or -5."
    },
    {
        "question": "What is a float in Python?",
        "answer": "A float is a number that contains a decimal value, such as 3.14 or 10.5."
    },
    {
        "question": "What is a boolean in Python?",
        "answer": "A boolean represents one of two values: True or False."
    },
    {
        "question": "What is None in Python?",
        "answer": "None represents the absence of a value or a value that has not been assigned."
    },
    {
        "question": "How can I check the type of a value in Python?",
        "answer": "You can use the type() function to determine the type of a value."
    },
    {
        "question": "What does type() do in Python?",
        "answer": "The type() function returns the data type of an object."
    },
    {
        "question": "What is isinstance in Python?",
        "answer": "isinstance() checks whether an object belongs to a specified type or class."
    },


    # =========================
    # Type Conversion
    # =========================

    {
        "question": "What is type casting in Python?",
        "answer": "Type casting is the process of converting a value from one data type to another."
    },
    {
        "question": "How do I convert a string to an integer?",
        "answer": "Use the int() function to convert a suitable string into an integer."
    },
    {
        "question": "How do I convert an integer to a string?",
        "answer": "Use the str() function to convert an integer into a string."
    },
    {
        "question": "How do I convert a number to a float?",
        "answer": "Use the float() function to convert a compatible number or string into a floating-point value."
    },
    {
        "question": "What is implicit type conversion?",
        "answer": "Implicit type conversion happens automatically when Python converts a value to a compatible type during an operation."
    },
    {
        "question": "What is explicit type conversion?",
        "answer": "Explicit type conversion happens when the programmer manually converts a value using functions such as int(), float(), or str()."
    },


    # =========================
    # Strings
    # =========================

    {
        "question": "How do you create a string in Python?",
        "answer": "A string can be created by placing text inside single quotes, double quotes, or triple quotes."
    },
    {
        "question": "Are Python strings mutable?",
        "answer": "No. Python strings are immutable, which means their characters cannot be changed directly after creation."
    },
    {
        "question": "How do you find the length of a string?",
        "answer": "Use the len() function to find the number of characters in a string."
    },
    {
        "question": "What is string concatenation?",
        "answer": "String concatenation means joining two or more strings together, commonly using the + operator."
    },
    {
        "question": "What is string slicing?",
        "answer": "String slicing extracts a portion of a string using a start, stop, and optional step."
    },
    {
        "question": "How do you convert a string to lowercase?",
        "answer": "Use the lower() method."
    },
    {
        "question": "How do you convert a string to uppercase?",
        "answer": "Use the upper() method."
    },
    {
        "question": "What is an f-string?",
        "answer": "An f-string is a formatted string literal that allows expressions to be embedded directly inside a string."
    },


    # =========================
    # Lists
    # =========================

    {
        "question": "How do you create a list in Python?",
        "answer": "A list is created by placing comma-separated values inside square brackets."
    },
    {
        "question": "Are Python lists mutable?",
        "answer": "Yes. Lists are mutable, so their elements can be changed after creation."
    },
    {
        "question": "How do you add an item to a list?",
        "answer": "You can use the append() method to add an item to the end of a list."
    },
    {
        "question": "How do you remove an item from a list?",
        "answer": "You can use methods such as remove(), pop(), or del to remove list elements."
    },
    {
        "question": "What is list indexing?",
        "answer": "List indexing is accessing an individual list element using its position."
    },
    {
        "question": "What is list slicing?",
        "answer": "List slicing extracts a portion of a list using start, stop, and optional step positions."
    },
    {
        "question": "How do you sort a list in Python?",
        "answer": "You can use the sort() method to sort a list in place or sorted() to create a sorted result."
    },


    # =========================
    # Tuples
    # =========================

    {
        "question": "How do you create a tuple in Python?",
        "answer": "A tuple is commonly created by placing comma-separated values inside parentheses."
    },
    {
        "question": "Are tuples mutable?",
        "answer": "No. Tuples are immutable, so their elements cannot be changed directly after creation."
    },
    {
        "question": "Why use a tuple instead of a list?",
        "answer": "Tuples are useful when data should remain unchanged and can communicate that the collection is intended to be immutable."
    },
    {
        "question": "Can a tuple contain different data types?",
        "answer": "Yes. A tuple can contain values of different data types."
    },


    # =========================
    # Sets
    # =========================

    {
        "question": "How do you create a set in Python?",
        "answer": "A set can be created using curly braces with values or by using the set() function."
    },
    {
        "question": "Can a set contain duplicate values?",
        "answer": "No. A set stores unique elements and automatically removes duplicate values."
    },
    {
        "question": "What is set union?",
        "answer": "Set union combines the elements of two sets and keeps only unique values."
    },
    {
        "question": "What is set intersection?",
        "answer": "Set intersection returns the elements that are common to both sets."
    },
    {
        "question": "Why are sets useful in Python?",
        "answer": "Sets are useful for storing unique values and performing mathematical set operations efficiently."
    },


    # =========================
    # Dictionaries
    # =========================

    {
        "question": "How do you create a dictionary in Python?",
        "answer": "A dictionary is created using key-value pairs inside curly braces."
    },
    {
        "question": "What is a key in a Python dictionary?",
        "answer": "A key is an identifier used to access its corresponding value in a dictionary."
    },
    {
        "question": "How do you access a dictionary value?",
        "answer": "You can access a value using its key, such as dictionary[key]."
    },
    {
        "question": "How do you add an item to a dictionary?",
        "answer": "Assign a value to a new key using dictionary[key] = value."
    },
    {
        "question": "Can dictionary values be duplicated?",
        "answer": "Yes. Multiple dictionary keys can have the same value."
    },
    {
        "question": "Can dictionary keys be duplicated?",
        "answer": "No. Dictionary keys must be unique."
    },


    # =========================
    # Operators
    # =========================

    {
        "question": "What are operators in Python?",
        "answer": "Operators are symbols or keywords used to perform operations on values and variables."
    },
    {
        "question": "What are arithmetic operators?",
        "answer": "Arithmetic operators perform mathematical operations such as addition, subtraction, multiplication, division, modulus, exponentiation, and floor division."
    },
    {
        "question": "What are comparison operators?",
        "answer": "Comparison operators compare values and produce a boolean result such as True or False."
    },
    {
        "question": "What are logical operators?",
        "answer": "Logical operators such as and, or, and not combine or modify boolean conditions."
    },
    {
        "question": "What is the difference between == and = in Python?",
        "answer": "The = operator assigns a value, while == checks whether two values are equal."
    },
    {
        "question": "What does the modulus operator do?",
        "answer": "The modulus operator % returns the remainder after division."
    },
    {
        "question": "What does the exponent operator do?",
        "answer": "The ** operator performs exponentiation, raising one value to the power of another."
    },


    # =========================
    # Conditional Statements
    # =========================

    {
        "question": "What is a conditional statement?",
        "answer": "A conditional statement allows a program to execute different code depending on whether a condition is true or false."
    },
    {
        "question": "How does an if statement work?",
        "answer": "An if statement executes its block of code when its condition evaluates to True."
    },
    {
        "question": "What is an elif statement?",
        "answer": "elif allows a program to check another condition when the previous if or elif condition was false."
    },
    {
        "question": "What is an else statement?",
        "answer": "An else block runs when all preceding conditions in the conditional structure are false."
    },
    {
        "question": "Can Python have multiple elif statements?",
        "answer": "Yes. A conditional structure can contain multiple elif branches."
    },
    {
        "question": "Can an if statement exist without else?",
        "answer": "Yes. An if statement does not require an else block."
    },


    # =========================
    # Loops
    # =========================

    {
        "question": "What is a loop in Python?",
        "answer": "A loop repeatedly executes a block of code while iterating over data or while a condition remains true."
    },
    {
        "question": "What is a for loop used for?",
        "answer": "A for loop is used to iterate over items in an iterable such as a list, string, tuple, or range."
    },
    {
        "question": "What is a while loop used for?",
        "answer": "A while loop repeatedly executes code as long as its condition remains true."
    },
    {
        "question": "What is the difference between for and while loops?",
        "answer": "A for loop is commonly used to iterate over an iterable, while a while loop continues as long as a condition remains true."
    },
    {
        "question": "What does break do in a loop?",
        "answer": "The break statement immediately exits the current loop."
    },
    {
        "question": "What does continue do in a loop?",
        "answer": "The continue statement skips the remaining code in the current iteration and moves to the next iteration."
    },
    {
        "question": "What does pass do in Python?",
        "answer": "The pass statement does nothing and is used as a placeholder where a statement is syntactically required."
    },
    {
        "question": "What is a nested loop?",
        "answer": "A nested loop is a loop placed inside another loop."
    },
    {
        "question": "What does range do in Python?",
        "answer": "The range() function produces a sequence of numbers commonly used for iteration."
    },


    # =========================
    # Functions
    # =========================

    {
        "question": "Why are functions useful in Python?",
        "answer": "Functions make programs easier to organize, reuse, test, and maintain."
    },
    {
        "question": "What is a function parameter?",
        "answer": "A parameter is a variable listed in a function definition that receives a value when the function is called."
    },
    {
        "question": "What is a function argument?",
        "answer": "An argument is a value passed to a function when the function is called."
    },
    {
        "question": "What is a return statement?",
        "answer": "The return statement sends a value back from a function and ends that function's execution."
    },
    {
        "question": "What is a default parameter?",
        "answer": "A default parameter has a predefined value that is used when the caller does not provide an argument."
    },
    {
        "question": "What is a function call?",
        "answer": "A function call is the act of executing a function by writing its name followed by parentheses."
    },
    {
        "question": "What are positional arguments?",
        "answer": "Positional arguments are matched to function parameters according to their order."
    },
    {
        "question": "What are keyword arguments?",
        "answer": "Keyword arguments pass values to function parameters by explicitly specifying the parameter name."
    },
    {
        "question": "What is recursion in Python?",
        "answer": "Recursion occurs when a function calls itself to solve a problem in smaller steps."
    },
    {
        "question": "What is a lambda function?",
        "answer": "A lambda function is a small anonymous function written using the lambda keyword."
    },
    {
        "question": "What is a nested function?",
        "answer": "A nested function is a function defined inside another function."
    },
    {
        "question": "What is a docstring?",
        "answer": "A docstring is a string used to document a module, class, or function."
    },
    {
        "question": "What are *args in Python?",
        "answer": "*args allows a function to accept a variable number of positional arguments."
    },
    {
        "question": "What are **kwargs in Python?",
        "answer": "**kwargs allows a function to accept a variable number of keyword arguments."
    },


    # =========================
    # Scope
    # =========================

    {
        "question": "What is variable scope?",
        "answer": "Variable scope determines where a variable can be accessed in a Python program."
    },
    {
        "question": "What is a local variable?",
        "answer": "A local variable is defined inside a function and is normally accessible only within that function."
    },
    {
        "question": "What is a global variable?",
        "answer": "A global variable is defined outside functions and can generally be accessed throughout the module."
    },
    {
        "question": "What is the global keyword?",
        "answer": "The global keyword allows a function to modify a global variable."
    },
    {
        "question": "What is the nonlocal keyword?",
        "answer": "The nonlocal keyword allows a nested function to modify a variable from its enclosing function scope."
    },


    # =========================
    # Modules and Packages
    # =========================

    {
        "question": "What is a module in Python?",
        "answer": "A module is a Python file containing code such as functions, classes, and variables that can be imported into another program."
    },
    {
        "question": "What is a package in Python?",
        "answer": "A package is a collection of related Python modules organized in a directory."
    },
    {
        "question": "What is import in Python?",
        "answer": "The import statement allows you to use code from another module or package."
    },
    {
        "question": "What is the difference between a module and a package?",
        "answer": "A module is generally a single Python file, while a package organizes multiple related modules."
    },
    {
        "question": "What is pip in Python?",
        "answer": "pip is Python's package installer and is commonly used to install and manage Python packages."
    },
    {
        "question": "How do I install a Python package?",
        "answer": "A package can commonly be installed using pip from the command line."
    },


    # =========================
    # File Handling
    # =========================

    {
        "question": "What is file handling in Python?",
        "answer": "File handling allows Python programs to create, read, write, append, and manage files."
    },
    {
        "question": "How do you open a file in Python?",
        "answer": "Use the open() function to open a file."
    },
    {
        "question": "What is the read mode in Python?",
        "answer": "Read mode opens a file for reading its contents."
    },
    {
        "question": "What is write mode in Python?",
        "answer": "Write mode opens a file for writing and can overwrite existing contents."
    },
    {
        "question": "What is append mode in Python?",
        "answer": "Append mode opens a file so new content can be added to the end without replacing existing content."
    },
    {
        "question": "Why should files be closed?",
        "answer": "Closing files releases system resources and ensures that pending data is properly written."
    },
    {
        "question": "What is the with statement used for in file handling?",
        "answer": "The with statement manages a file context and automatically closes the file when the block finishes."
    },


    # =========================
    # Exceptions
    # =========================

    {
        "question": "What is an exception in Python?",
        "answer": "An exception is an error or unusual event that occurs during program execution."
    },
    {
        "question": "What is exception handling?",
        "answer": "Exception handling allows a program to detect and handle runtime errors without crashing unexpectedly."
    },
    {
        "question": "What is try in Python?",
        "answer": "The try block contains code that may raise an exception."
    },
    {
        "question": "What is except in Python?",
        "answer": "The except block handles an exception raised by code inside the try block."
    },
    {
        "question": "What is finally in Python?",
        "answer": "The finally block executes after the try and except processing, whether or not an exception occurred."
    },
    {
        "question": "What does raise do in Python?",
        "answer": "The raise statement is used to explicitly raise an exception."
    },


    # =========================
    # Object Oriented Programming
    # =========================

    {
        "question": "What is object oriented programming?",
        "answer": "Object oriented programming is a programming approach that organizes software around objects containing data and behavior."
    },
    {
        "question": "What is a class in Python?",
        "answer": "A class is a blueprint used to create objects with attributes and methods."
    },
    {
        "question": "What is an object in Python?",
        "answer": "An object is an instance of a class."
    },
    {
        "question": "What is a constructor in Python?",
        "answer": "The __init__ method is commonly used as a constructor to initialize an object's attributes when it is created."
    },
    {
        "question": "What is self in Python?",
        "answer": "self refers to the current instance of a class and is used to access its attributes and methods."
    },
    {
        "question": "What is inheritance in Python?",
        "answer": "Inheritance allows a class to derive attributes and methods from another class."
    },
    {
        "question": "What is polymorphism?",
        "answer": "Polymorphism allows different objects or classes to provide different implementations of the same interface or method."
    },
    {
        "question": "What is encapsulation?",
        "answer": "Encapsulation means organizing data and methods together while controlling how internal implementation details are accessed."
    },
    {
        "question": "What is abstraction?",
        "answer": "Abstraction means exposing important functionality while hiding unnecessary implementation details."
    },


    # =========================
    # Comprehensions
    # =========================

    {
        "question": "What is a list comprehension?",
        "answer": "A list comprehension is a concise way to create a list by applying an expression to items in an iterable."
    },
    {
        "question": "What is a dictionary comprehension?",
        "answer": "A dictionary comprehension is a concise way to create dictionaries from an iterable."
    },
    {
        "question": "What is a set comprehension?",
        "answer": "A set comprehension is a concise way to create a set from an iterable."
    },


    # =========================
    # Iterators and Generators
    # =========================

    {
        "question": "What is an iterator in Python?",
        "answer": "An iterator is an object that produces values one at a time and implements the iterator protocol."
    },
    {
        "question": "What is an iterable?",
        "answer": "An iterable is an object that can be iterated over, such as a list, tuple, string, or dictionary."
    },
    {
        "question": "What is a generator in Python?",
        "answer": "A generator is a special type of iterator that produces values lazily, usually using the yield statement."
    },
    {
        "question": "What is yield in Python?",
        "answer": "The yield statement produces a value from a generator while preserving its state so execution can continue later."
    },
    {
        "question": "What is the difference between an iterator and an iterable?",
        "answer": "An iterable can provide an iterator, while an iterator is the object that produces values during iteration."
    },


    # =========================
    # Decorators
    # =========================

    {
        "question": "What is a decorator in Python?",
        "answer": "A decorator is a function that modifies or extends the behavior of another function or class without changing its original code."
    },
    {
        "question": "Why are decorators useful?",
        "answer": "Decorators are useful for adding reusable behavior such as logging, authentication, timing, or validation."
    },


    # =========================
    # Lambda and Functional Programming
    # =========================

    {
        "question": "Why use lambda functions?",
        "answer": "Lambda functions are useful for short operations where defining a full named function would be unnecessary."
    },
    {
        "question": "What does map do in Python?",
        "answer": "map() applies a function to each item of an iterable and returns an iterator."
    },
    {
        "question": "What does filter do in Python?",
        "answer": "filter() returns an iterator containing items from an iterable for which a condition is true."
    },
    {
        "question": "What does reduce do in Python?",
        "answer": "reduce() repeatedly applies a function to items in an iterable to produce a single accumulated result."
    },


    # =========================
    # Input and Output
    # =========================

    {
        "question": "How do you take input in Python?",
        "answer": "Use the input() function to receive text input from the user."
    },
    {
        "question": "What does input return in Python?",
        "answer": "The input() function returns the user's input as a string."
    },
    {
        "question": "How do you print output in Python?",
        "answer": "Use the print() function to display output."
    },
    {
        "question": "What does print do in Python?",
        "answer": "The print() function displays values or text on the output."
    },


    # =========================
    # Debugging and Testing
    # =========================

    {
        "question": "What is debugging?",
        "answer": "Debugging is the process of finding and fixing errors in a program."
    },
    {
        "question": "What is a syntax error?",
        "answer": "A syntax error occurs when Python code does not follow the language's syntax rules."
    },
    {
        "question": "What is a runtime error?",
        "answer": "A runtime error occurs while a program is executing."
    },
    {
        "question": "What is a logical error?",
        "answer": "A logical error occurs when a program runs but produces an incorrect result because the logic is wrong."
    },
    {
        "question": "What is testing in programming?",
        "answer": "Testing is the process of checking software to determine whether it behaves as expected."
    },
    {
        "question": "What is unit testing?",
        "answer": "Unit testing checks individual functions or components of a program in isolation."
    },


    # =========================
    # Virtual Environments
    # =========================

    {
        "question": "What is a virtual environment in Python?",
        "answer": "A virtual environment is an isolated Python environment that keeps project dependencies separate from other projects."
    },
    {
        "question": "Why use a virtual environment?",
        "answer": "Virtual environments prevent dependency conflicts and allow each project to use its own package versions."
    },
    {
        "question": "What is venv in Python?",
        "answer": "venv is Python's built-in module for creating lightweight virtual environments."
    },


    # =========================
    # APIs and Web
    # =========================

    {
        "question": "What is an API?",
        "answer": "An API is an interface that allows different software systems to communicate and exchange data or functionality."
    },
    {
        "question": "What is HTTP?",
        "answer": "HTTP is a protocol used for communication between clients and servers on the web."
    },
    {
        "question": "What is a REST API?",
        "answer": "A REST API is a web API that follows REST principles and commonly uses HTTP methods to work with resources."
    },
    {
        "question": "What is JSON?",
        "answer": "JSON is a lightweight text-based data format commonly used for exchanging structured data between applications."
    },


    # =========================
    # NumPy
    # =========================

    {
        "question": "What is NumPy?",
        "answer": "NumPy is a Python library used for numerical computing and efficient operations on multidimensional arrays."
    },
    {
        "question": "Why is NumPy used?",
        "answer": "NumPy is used for fast numerical calculations, arrays, matrices, and mathematical operations."
    },
    {
        "question": "What is a NumPy array?",
        "answer": "A NumPy array is a multidimensional data structure designed for efficient numerical computation."
    },


    # =========================
    # Pandas
    # =========================

    {
        "question": "What is Pandas?",
        "answer": "Pandas is a Python library used for data manipulation and analysis."
    },
    {
        "question": "What is a Pandas DataFrame?",
        "answer": "A DataFrame is a two-dimensional tabular data structure in Pandas with rows and columns."
    },
    {
        "question": "What is a Pandas Series?",
        "answer": "A Series is a one-dimensional labeled data structure in Pandas."
    },


    # =========================
    # AI and Machine Learning
    # =========================

    {
        "question": "What is artificial intelligence?",
        "answer": "Artificial intelligence is the field of creating systems that can perform tasks that normally require aspects of human intelligence."
    },
    {
        "question": "What is machine learning?",
        "answer": "Machine learning is a branch of AI where models learn patterns from data to make predictions or decisions."
    },
    {
        "question": "What is deep learning?",
        "answer": "Deep learning is a type of machine learning that uses neural networks with multiple layers."
    },
    {
        "question": "What is a machine learning model?",
        "answer": "A machine learning model is a mathematical or computational system trained to identify patterns in data and make predictions or decisions."
    },
    {
        "question": "What is training data?",
        "answer": "Training data is the data used to teach a machine learning model how to identify patterns."
    },
    {
        "question": "What is a neural network?",
        "answer": "A neural network is a computational model inspired by interconnected neurons and is commonly used in machine learning and deep learning."
    },
    {
        "question": "What is supervised learning?",
        "answer": "Supervised learning trains a model using labeled examples where the desired output is known."
    },
    {
        "question": "What is unsupervised learning?",
        "answer": "Unsupervised learning finds patterns or structures in data without labeled target outputs."
    },
    {
        "question": "What is natural language processing?",
        "answer": "Natural language processing, or NLP, is a field of AI focused on enabling computers to process and understand human language."
    },


]


def preprocess(text):
    text = text.lower()

    text = text.translate(
        str.maketrans("", "", string.punctuation)
    )

    words = text.split()

    python_keywords = {
        "for",
        "while",
        "if",
        "else",
        "elif",
        "in",
        "is",
        "not",
        "and",
        "or",
        "class",
        "from",
        "as",
        "with",
        "try",
        "except",
        "finally",
        "return",
        "pass",
        "break",
        "continue"
    }

    words = [
        word for word in words
        if word not in ENGLISH_STOP_WORDS
        or word in python_keywords
    ]

    stemmer = PorterStemmer()

    stemmed_words = []

    for word in words:
        stemmed_words.append(stemmer.stem(word))

    return " ".join(stemmed_words)
for faq in faqs:
    faq["processed_question"] = preprocess(faq["question"])
