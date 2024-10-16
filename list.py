#Homogenous list

integers = [1, 2, 3, 8, 33]

animals = ["dog", "cat", "goat"]

names = ["Roger", "Mafanfrefed", "alehli"]

floats = [2.2, 4.5, 9.8, 10.8]

#Heterogenous list

numbers_animals_names = [2, "cat", 34.33, "Nico"]

list_lists = [[1, 2, 3],["cat", "dog", "rooster"]]

#How to access an element in a list

list = [3, 22, 30, 5, 3, 20]

print(list[2])
print(list[0])
print(list[1])
print(list[4])
print(list[-1])

word_gpt_list = [
    
    "def", "return", "if", "else", "elif", "for", "while", "break", "continue",
    "import", "from", "as", "class", "self", "init", "in", "not", "and", "or",
    "lambda", "map", "filter", "reduce", "zip", "list", "dict", "set", "tuple",
    "str", "int", "float", "bool", "None", "True", "False", "pass", "try", 
    "except", "finally", "raise", "with", "open", "read", "write", "append", 
    "close", "readline", "readlines", "split", "join", "format", "f-string", 
    "len", "range", "enumerate", "index", "count", "slice", "sort", "reverse", 
    "copy", "clear", "extend", "insert", "remove", "pop", "keys", "values", 
    "items", "get", "setdefault", "update", "isinstance", "issubclass", "all", 
    "any", "sum", "min", "max", "round", "abs", "divmod", "pow", "sqrt", 
    "importlib", "sys", "os", "json", "re", "random", "datetime", "time", 
    "threading", "multiprocessing", "asyncio", "requests", "urllib", 
    "BeautifulSoup", "pandas", "numpy", "matplotlib", "seaborn", "scikit-learn", 
    "tensorflow", "keras", "flask", "django", "pytest", "unittest", "coverage", 
    "pylint", "black", "mypy", "logging", "config", "environment", "virtualenv", 
    "pip", "requirements", "setup", "wheel", "tar", "zipfile", "shutil", 
    "pathlib", "subprocess", "signal", "socket", "csv", "xml", "html", 
    "markdown", "configparser", "sqlite3", "pymysql", "psycopg2", "urllib2", 
    "base64", "hashlib", "itertools", "functools", "collections", "Counter", 
    "defaultdict", "deque", "namedtuple", "OrderedDict", "ChainMap", 
    "UserDict", "UserList", "UserString", "Thread", "Event", "Lock", "RLock", 
    "Condition", "Semaphore", "Queue", "Process", "Future", "Task", "EventLoop", 
    "Coroutine", "Async", "Await", "Yield", "Generator", "ContextManager", 
    "Property", "Descriptor", "Metaclass", "Abstract", "Interface", "Module", 
    "Package", "Namespace", "ImportError", "AttributeError", "KeyError", 
    "IndexError", "ValueError", "TypeError", "SyntaxError", "IOError", 
    "RuntimeError", "StopIteration", "FileNotFoundError", "OSError", 
    "AssertionError", "MemoryError", "Exception", "Warning", "DeprecationWarning", 
    "ImportWarning", "FutureWarning", "UnicodeError", "OverflowError", 
    "ZeroDivisionError", "NotImplementedError", "Assertion"
]

print(word_gpt_list[-1])

#List slicing 

list = [1, 2, 3, 4, 5]

print(list[:])
print(list[1:3])
print(list[2:-1])

list = [3, 22, 30, 5.3, 20]

#Update a list

science = ["art", "chemistry", "math"]
science [0] = "biology"
science [2] = "geology"
print(science)

#Delete an element
integers = [2, 4, 9, 20, 27]
integers.remove(4)
print(integers)

integers.pop(3)
print(integers)

#Append new elements to the list
list_names = ["Messi","Suarez","Neymar"]
list_names.append("Nico")
print(list_names)

list_of_squares = []
for int in range (1,10):
    square = int **2
    list_of_squares.append(square)
print(list_of_squares)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#[expression for int in list if condition]
squared2 = [item**2 for item in range(1,10)]
print(squared2)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:
    print(number**3)
    
cubic = [num**3 for num in numbers]
print(cubic)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
doubled_numbers = [num*2 for num in numbers if num%3 == 0]
print(doubled_numbers)