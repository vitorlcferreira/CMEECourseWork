#!/usr/bin/env python3

"""A script to illustrate the global and local variables"""

__appname__ = ['Global and Local variables']
__author__ = 'Vitor Ferreira (f.ferreira22@imperial.ac.uk)'


# Variable scope

# GLOBAL and LOCAL variables

# 1st Example
i = 1
x = 0
for i in range(10):
    x += 1
print(x)
print(i)

# 2nd Example
i = 1
x = 0


def a_function(y):
    x = 0
    for i in range(y):
        x += 1
    return x, y


x = a_function(10)
print(x)
print(i)


# Let's work with GLOBAL VARIABLES
_a_global = 10

if _a_global >= 5:
    _b_global = _a_global +5  # Also global variable


print("Before calling a function, outside the function, the value of "
      "_a_global is", _a_global)
print("Before calling a function, outside the function, the value of "
      "_b_global is", _b_global)

def a_function():
    _a_global = 4  # a local variable

    if _a_global >= 4:
        _b_global = _a_global + 5  # also local variable

        _a_local = 3

        print("Inside the function, the value of _a_global is", _a_global)
        print("Inside the function, the value of _b_global is", _b_global)
        print("Inside the function, the value of _a_local is", _a_local)


a_function()


print("After calling a_function, outside the function, the value of "
      "_a_global is (still)", _a_global)
print("After calling a_function, outside the function, the value of "
      "_b_global is (still)", _b_global)
try:
    print("After calling a_function, outside the function, the value of "
      "_a_local is ", _a_local)
except:
    print("*** No 'local_variable' outside the function available! ***")


# Another Example 1
_a_global = 10


def a_function():
    _a_local = 4

    print("Inside the function, the value _a_local is", _a_local)
    print("Inside the function, the value of _a_global is", _a_global)


a_function

print("Outside the function, the value of _a_global is", _a_global)


# Another Example 2
_a_global = 10

print("Before calling a_function, outside the function, the value of "
      "_a_global is", _a_global)


def a_function():
    global _a_global
    _a_global = 5
    _a_local = 4
    
    print("Inside the function, the value of _a_global is", _a_global)
    print("Inside the function, the value _a_local is", _a_local)


a_function()

print("After calling a_function, outside the function, the value of "
      "_a_global now is", _a_global)


# Compare following examples:
# Another Example 3
def a_function():
    _a_global = 10

    def _a_function2():
        global _a_global
        _a_global = 20
    
    print("Before calling a_function2, value of _a_global is", _a_global)

    _a_function2()
    
    print("After calling a_function2, value of _a_global is", _a_global)


a_function()

print("The value of a_global in main workspace / namespace now is", _a_global)

# Another Example 4
_a_global = 10


def a_function():

    def _a_function2():
        global _a_global
        _a_global = 20
    
    print("Before calling a_function2, value of _a_global is", _a_global)

    _a_function2()
    
    print("After calling a_function2, value of _a_global is", _a_global)


a_function()

print("The value of a_global in main workspace / namespace is", _a_global)
