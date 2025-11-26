# Bython

https://img.shields.io/pypi/v/bython.svg
https://img.shields.io/pypi/pyversions/bython.svg
https://img.shields.io/badge/License-MIT-yellow.svg

Bython is a powerful Python library that converts Brainfuck code to Python and executes it seamlessly. Whether you want to run Brainfuck programs in Python, convert them to readable Python code, or integrate Brainfuck execution into your projects, Bython makes it simple and efficient.

Features

· 🚀 Direct Execution: Run Brainfuck code directly in Python
· 📝 Code Conversion: Convert Brainfuck code to human-readable Python
· 🔧 Flexible Configuration: Customizable memory size and input handling
· 🛡️ Error Handling: Comprehensive syntax validation and runtime error reporting
· 💻 CLI Support: Command-line interface for easy file execution
· 📦 Lightweight: No dependencies, pure Python implementation

Installation

```bash
pip install bython
```

Quick Start

Basic Usage

```python
import bython

# Execute Brainfuck code directly
result = bython.execute("++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.")
print(result)  # Output: "Hello World!\n"

# Convert Brainfuck to Python code
python_code = bython.compile_to_python("+++>++<[->+<]>.")
print(python_code)
```

Using the Class Interface

```python
from bython import Bython

# Create an interpreter
interpreter = Bython(memory_size=30000)

# Execute with input
result = interpreter.execute(",.", "A")  # Reads input and outputs it
print(result)  # Output: "A"

# Or use direct execution (more efficient)
result = interpreter.execute_direct("+++[>++<-]>.")
print(result)
```

Command Line Usage

Bython comes with a convenient command-line interface:

```bash
# Execute a Brainfuck file
bython hello_world.bf

# Execute Brainfuck code from string
bython -c "++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++."

# Compile to Python without executing
bython --compile-only -o output.py program.bf

# Execute with input data
bython -i "input data" program.bf

# Set custom memory size
bython -m 50000 program.bf
```

API Reference

Functions

execute(brainfuck_code, input_data="", memory_size=30000)

Execute Brainfuck code directly and return the output.

Parameters:

· brainfuck_code (str): Brainfuck code to execute
· input_data (str): Input data for the program (default: "")
· memory_size (int): Size of the memory tape (default: 30000)

Returns: str - Output of the Brainfuck program

compile_to_python(brainfuck_code, memory_size=30000)

Convert Brainfuck code to Python code.

Parameters:

· brainfuck_code (str): Brainfuck code to convert
· memory_size (int): Size of the memory tape (default: 30000)

Returns: str - Generated Python code

Bython Class

Bython(memory_size=30000)

Main interpreter class.

Parameters:

· memory_size (int): Size of the memory tape

Methods

· compile(brainfuck_code): Convert Brainfuck to Python code
· execute(brainfuck_code, input_data=""): Execute via Python code generation
· execute_direct(brainfuck_code, input_data=""): Direct execution (more efficient)

Examples

Hello World

```python
import bython

hello_world_bf = """
++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.
"""

result = bython.execute(hello_world_bf)
print(result)  # Hello World!
```

Fibonacci Sequence

```python
from bython import Bython

fibonacci_bf = """
>++++++++++>+>+[
    [+++++[>++++++++<-]>.<++++++[>--------<-]+<<<]>.>>[
        [-]<[>+<-]>>[<<+>+>-]<[>+<-[>+<-[>+<-[>+<-[>+<-[>+<-
            [>+<-[>+<-[>+<-[>[-]>+>+<<<-[>+<-]]]]]]]]]]]
        >>>+
    ]<<<
]
"""

interpreter = Bython()
result = interpreter.execute_direct(fibonacci_bf)
print(result)  # 1, 1, 2, 3, 5, 8, 13, 21, 34, 55...
```

Rot13 Example

```python
import bython

rot13_bf = """
-,+[                         
    -[                       
        >>[>]+>+[<]<-        
    ]>>[<]<[                 
        >-[>>>]>>>>[-<+>]<[<+>-]<[<+>-]<[<+>-]<[<+>-]<[<+>-]
        <[<+>-]<[<+>-]<[<+>-]<[<+>-]<[<+>-]<[<+>-]<[<+>-]<<<
    ]<                        
]>>>[>]                      
+++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++
++++++++++.                  
"""

# Test with input
input_text = "hello"
result = bython.execute(rot13_bf, input_text)
print(f"ROT13 of '{input_text}': {result}")  # uryyb
```

Error Handling

Bython provides detailed error information:

```python
from bython import Bython, BythonSyntaxError, BythonRuntimeError

interpreter = Bython()

try:
    result = interpreter.execute("+++[--->++<]>.>")  # Missing bracket
except BythonSyntaxError as e:
    print(f"Syntax error: {e}")

try:
    result = interpreter.execute("+" * 100000)  # Potential memory issues
except BythonRuntimeError as e:
    print(f"Runtime error: {e}")
```

Brainfuck Language Reference

Bython supports the complete Brainfuck language:

Command Description
> Move pointer right
< Move pointer left
+ Increment current cell
- Decrement current cell
. Output character from current cell
, Input character to current cell
[ Start loop while current cell != 0
] End loop

Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (git checkout -b feature/amazing-feature)
3. Commit your changes (git commit -m 'Add some amazing feature')
4. Push to the branch (git push origin feature/amazing-feature)
5. Open a Pull Request

License

This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments

· Brainfuck language designed by Urban Müller
· Inspired by various Brainfuck implementations in different languages

---

Bython - Making Brainfuck accessible in Python! 🐍
