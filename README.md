# PyOops language user manual

## Table of Contents
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Getting Started](#getting-started)
4. [Language Syntax](#language-syntax)
5. [Command-Line Usage](#command-line-usage)
6. [Interactive Mode](#interactive-mode)
7. [Examples](#examples)
8. [Error Handling](#error-handling)
9. [Summary](#summary)

## Introduction
PyOops is a statically-typed programming language designed for simplicity and clarity while maintaining powerful features. It offers a robust syntax, error handling, and custom types, making it suitable for learning programming concepts and building small applications.

## Installation
PyOops requires Python 3 and the ANTLR4 runtime.

1. Ensure you have Python 3 installed:
   ```bash
   python --version
   ```
   ```bash
   python3 --version
   ```

2. Install ANTLR4 Python runtime:
   ```bash
   pip install antlr4-python3-runtime
   ```
   Command to run ANTLR g4:
   ```bash
   antlr4 -Dlanguage=Python3 -visitor
   ```

4. Download the PyOops files to a directory of your choice.

## Getting Started
Pyoops programs use the `.bibi` extension. Create a file called `hello.bibi` with the following content:

```
print("Hello, PyOops!");
```

Run the program:
```bash
python pyoops-cmd.py test/hello.bibi
```
```bash
python3 pyoops-cmd.py test/hello.bibi
```

## Language Syntax

### Basic Types
Pyoops supports the following data types:
- `int` - Integer numbers
- `float` - Floating-point numbers
- `str` - String of characters
- `char` - Single character
- Arrays: `int[]`, `float[]`, `str[]`, `char[]`

### Variables
Variables must be declared with their type before use:

```
int age = 25;
float pi = 3.14159;
str name = "Alice";
char grade = 'A';
int[] numbers = [1, 2, 3, 4, 5];
str[] names = ["Alice", "Bob", "Charlie"];
```

### Operators
- Arithmetic: `+`, `-`, `*`, `/`
- Comparison: `<`, `<=`, `>`, `>=`, `==`, `!=`
- Logical: `and`, `or`, `!`
- Assignment: `=`

### Control Structures

#### If-Else Statement
```
if (condition) {
    // statements
} else if (another_condition) {
    // statements
} else {
    // statements
}
```

#### While Loop
```
while (condition) {
    // statements
    
    // Optional break and continue
    if (some_condition) {
        break;
    }
    if (another_condition) {
        continue;
    }
}
```

### Functions
Functions are defined using the `func` keyword:
- With return statement(s): `func` + data or string array (`int`, `float`, `str`, `char`, `int[]`, `float[]`, `str[]`, `char[]`)
- Without return statement: `func void`

```
func int add(int a, int b) {
    return a + b;
}

func void greet(str name) {
    print("Hello, " + name + "!");
}
```

Call functions like this:
```
int result = add(5, 3);
greet("World");
```

### Custom Types
Create custom types (similar to structs) using the `type` keyword:
- Declaring a variable with a custom type inside another custom type is not allowed.

```
type Person {
    str name;
    int age;
}

// Create an instance
Person john;

// Access fields with dot notation
john.name = "John Doe";
john.age = 30;

// Use in expressions
print("Name: " + john.name + ", Age: " + john.age);
```

### Error Handling
Use try-except blocks to handle runtime errors:

```
try {
    // Code that might cause an error
    int result = 10 / 0;
} except {
    // Error handling code
    print("Error occurred: " + get_error());
}
```

The `get_error()` function returns the error message as a string and is only available inside an except block.


### Comments
PyOops supports line and block comments:

```
// This is a line comment

---
This is a 
block comment
---
```

## Command-Line Usage
The PyOops language can be used in several ways:

```bash
python3 pyoops-cmd.py [options] [file]

python3 pyoops.py [file]

```

I also create my own such that I can run

```bash

pyoops [file]

```

Options:
- `-i, --interactive`: Start interactive mode
- `-d, --debug`: Enable debug output (shows symbol table)
- `-v, --version`: Show version information

Examples:
- Run a file: `python pyoops-cmd.py program.bibi`
- Interactive mode: `python pyoops-cmd.py -i`
- Run a file and enter interactive mode: `python pyoops-cmd.py program.bibi -i`
- Debug mode: `python pyoops-cmd.py -d program.bibi`

## Interactive Mode
Enter interactive mode with:
```bash
python pyoops-cmd.py -i
```

In interactive mode, you can:
- Type PyOops code directly and execute it immediately
- Use special commands:
  - `exit()` - Exit interactive mode
  - `help()` - Show available commands
  - `clear()` - Clear the symbol table (reset variables)
  - `symbols()` - Print current symbol table contents
  - `run("filename.pi")` - Execute a file
  - `load("filename.pi")` - Load a file (without executing)
  - `run_loaded()` - Execute previously loaded code

## Examples

### Basic Calculator
```
// calculator.bibi
func float add(float a, float b) {
    return a + b;
}

func float subtract(float a, float b) {
    return a - b;
}

func float multiply(float a, float b) {
    return a * b;
}

func float divide(float a, float b) {
    // Handle division by zero
    try {
        return a / b;
    } except {
        print("Error: " + get_error());
        return 0.0;
    }
}

// Simple calculator demo
float num1 = 15.0;
float num2 = 5.0;

print("Addition: " + add(num1, num2));
print("Subtraction: " + subtract(num1, num2));
print("Multiplication: " + multiply(num1, num2));
print("Division: " + divide(num1, num2));
print("Division by zero: " + divide(num1, 0.0));
```

### Custom Type Example
```
// person.bibi
type Person {
    str name;
    int age;
    str occupation;
}

Person alice;
alice.name = "Alice Johnson";
alice.age = 28;
alice.occupation = "Software Engineer";

Person bob;
bob.name = "Bob Smith";
bob.age = 35;
bob.occupation = "Teacher";

func void display_person(Person p) {
    print("Name: " + p.name);
    print("Age: " + p.age);
    print("Occupation: " + p.occupation);
    print("---");
}

display_person(alice);
display_person(bob);
```

### Array Operations
```
// arrays.bibi
int[] numbers = [10, 20, 30, 40, 50];

// Calculate sum
func int sum_array(int[] arr) {
    int total = 0;
    int i = 0;
    while (i < 5) {
        total = total + arr[i];
        i = i + 1;
    }
    return total;
}

print("Sum of array: " + sum_array(numbers));

// Find maximum
func int max_array(int[] arr) {
    int max_val = arr[0];
    int i = 1;
    while (i < 5) {
        if (arr[i] > max_val) {
            max_val = arr[i];
        }
        i = i + 1;
    }
    return max_val;
}

print("Maximum value: " + max_array(numbers));
```

## Error Handling
PyOops provides detailed error messages for different types of errors, for example:


### Type Mismatch Errors

```
int age = "twenty"; // Error: String cannot be assigned to int
float price = true; // Error: Boolean cannot be assigned to float
```


### Array Index Errors
```
int[] numbers = [10, 20, 30];
print(numbers[5]); // Error: Index 5 out of bounds for array 'numbers'
print(numbers[-1]); // Error: Index -1 out of bounds for array 'numbers'
```

### Arithmetic Errors

```
int x = 10 / 0; // Error: Division by zero
Undefined Variable Errors
print(undefinedVar); // Error: Variable 'undefinedVar' not defined
```


###  Function-related Errors


```
func int add(int a, int b) {
    return a + b;
}
```

```
add("hello", 5); // Error: Mismatched types in parameter
add(1, 2, 3); // Error: Too many arguments
print(unknownFunction()); // Error: Function 'unknownFunction' not defined
```

###  Control Flow Errors

```
return 5; // Error: Return statement outside function

while (true) {
    // ...
}
// Error: Loop exceeded 1000 iterations. Possible infinite loop.

break; // Error: Break statement outside of loop
continue; // Error: Continue statement outside of loop
Custom Type Errors
type Person {
    str name;
    int age;
}
```

```
Person p;
print(p.address); // Error: Field 'address' not found in new-type instance 'p'
Infinite Loop Protection
Pyoops has built-in protection against infinite loops. It limits:
```
Maximum number of iterations (default: 1000)

Maximum execution time (default: 5 seconds)

```
int i = 0;
while (true) {
    i = i + 1;
    // Will automatically terminate with error after 1000 iterations:
    // [Runtime Error] Loop exceeded 1000 iterations. Possible infinite loop.
}
```

### Syntax Errors
Detected during parsing, with line and column information:
```
[Syntax Error] Line 5:10 - Mismatched input 'end' expecting ';'
int x = 10 end
         ^
Offending symbol: 'end'
Expected one of: SEMI
```

### Type Errors
Detected during semantic analysis:
```
[Type Error] Line 3:10 - Mismatched types in assignment of 'age': expected 'int', got 'str'
```

### Runtime Errors
Detected during execution:
```
[Runtime Error] Division by zero.
```

Use try-except blocks to handle runtime errors gracefully:
```
try {
    int result = 10 / 0;
} except {
    print("Error occurred: " + get_error());
}
```

### Division by zero:


```
func float divide(float a, float b) {
    try {
        return a / b;
    } except {
        print("Cannot divide by zero. Using default value.");
        return 0.0;
    }
}
```

Array bounds checking:

```
func int get_element(int[] arr, int index) {
    try {
        return arr[index];
    } except {
        print("Invalid index: " + get_error());
        return -1; // Default error value
    }
}
```

### General error logging:

```
try {
    // Complex operation that might fail
    result = complex_calculation();
} except {
    print("Operation failed: " + get_error());
    // Perform cleanup or fallback operations
}
```

## Summary

### Keywords
- `if`, `else` - Conditional statements
- `while` - Loops
- `func` - Function declaration
- `return` - Function return
- `print` - Output to console
- `try`, `except` - Error handling
- `true`, `false` - Boolean literals
- `continue`, `break` - Loop control
- `void` - Function return type
- `type` - Custom type definition

### Data Types
- `int` - Integer numbers
- `float` - Floating-point numbers
- `str` - String of characters
- `char` - Single character
- `int[]`, `float[]`, `str[]`, `char[]` - Arrays
- Custom types created with `type`

### Operators
- Arithmetic: `+`, `-`, `*`, `/`
- Comparison: `<`, `<=`, `>`, `>=`, `==`, `!=`
- Logical: `and`, `or`, `!`
- Assignment: `=`

---

For more information or help with specific issues, please contact the language developers or create an issue on the project repository.
