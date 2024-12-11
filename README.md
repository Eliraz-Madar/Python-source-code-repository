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
   git clone https://github.com/your-username/repository-name.git
   ```
2. Navigate to the project directory:
   ```bash
   cd repository-name
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
Currently, `.lambda` scripts cannot be executed due to unresolved issues. You can still experiment with the language interactively using the REPL.

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

## Known Issues
- The interpreter does not check if variables passed to functions are initialized.
- Lambda functions are currently not executable.
- Script execution for `.lambda` files is non-functional.

## Contributing
We welcome contributions! To contribute:
1. Fork this repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a detailed explanation of your changes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---
We hope you enjoy using this interpreter and exploring its capabilities!

