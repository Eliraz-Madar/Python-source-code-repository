# Functional Programming Language Interpreter

Welcome to the **Functional Programming Language Interpreter**! This repository provides an interpreter for a custom functional programming language with an intuitive syntax and useful features.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Interactive Mode (REPL)](#interactive-mode-repl)
  - [Running Scripts](#running-scripts)
- [Language Syntax](#language-syntax)
  - [Comments](#comments)
  - [Variable Assignment](#variable-assignment)
  - [Functions](#functions)
  - [Conditionals](#conditionals)
- [Known Issues](#known-issues)
- [Contributing](#contributing)
- [License](#license)

## Features
- **Interactive REPL**: Experiment with the language directly in your terminal.
- **Script Execution**: Execute `.lambda` script files following the language's syntax.
- **Basic Functional Programming**: Define and call functions with a clean and simple syntax.
- **Support for Arithmetic and Logical Operations**: Includes built-in support for mathematical and logical expressions.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/Eliraz-Madar/Python-source-code-repository.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Python-source-code-repository
   ```
3. Ensure Python 3.x is installed on your system.

## Usage
### Interactive Mode (REPL)
To enter interactive mode, run the following command:
```bash
python main.py
```
In this mode, you can type expressions or statements, and the interpreter will evaluate them immediately.

### Running Scripts
Run a `.lambda` file directly:
```bash
python main.py my_script.lambda
```
Each line is executed in turn; results are printed as they're produced, and any error is reported with the correct line number.

## Language Syntax
### Comments
Use `#` for comments. For example:
```lambda
# This is a comment
```

### Variable Assignment
Assign values to variables using the `VAR` keyword:
```lambda
VAR x = 10
```

### Functions
Define functions with the `FUN` keyword. Syntax:
```lambda
FUN function_name(parameters) -> expression
```
Example:
```lambda
FUN add(a, b) -> a + b
```

### Conditionals
Write conditional statements using `IF`, `THEN`, `ELSE`:
```lambda
IF condition THEN do_something ELSE do_something_else
```
Example:
```lambda
IF x > 0 THEN VAR y = 1 ELSE VAR y = -1
```

### Anonymous Functions (lambda)
Create a function value without naming it, using `lambda`:
```lambda
lambda(params): expression
```
Example:
```lambda
(lambda(x): x + 1)(5)          # 6
VAR square = lambda(n): n * n
square(4)                      # 16
```

### Named Function Values (def) and Recursion (rec)
`def` creates a named function value (usable anywhere an expression is), but on its own it can't call itself:
```lambda
def name(params): expression
```
To make a function genuinely recursive without binding its name anywhere else, wrap it in `rec`:
```lambda
VAR fact = rec(def fact(n): IF (n == 0) THEN 1 ELSE n * fact(n - 1))
fact(5)                         # 120
```
Note: `FUN name(params) -> expression` (see [Functions](#functions)) already supports recursion on its own, since it binds its name as a side effect. `rec` is for cases where you don't want that side effect — e.g. an inline recursive function passed straight into another call.

## Known Issues
None currently known. Previously reported issues have been resolved:
- Errors (including a variable being undefined/uninitialized) are now always reported, with the correct line number, instead of being silently swallowed.
- Anonymous (`lambda`) and explicitly recursive (`rec`) functions are now supported, matching the language grammar.

## Contributing
We welcome contributions! To contribute:
1. Fork this repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a detailed explanation of your changes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---
We hope you enjoy using this interpreter and exploring its capabilities!