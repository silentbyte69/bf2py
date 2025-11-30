# bf2py

[![PyPI version](https://img.shields.io/pypi/v/bf2py.svg)](https://pypi.org/project/bf2py/)

bf2py is a powerful Python library that converts Brainfuck code to Python and executes it seamlessly.

## Installation

```bash
pip install bf2py
```

or

```bash
pip install git+https://github.com/silentbyte69/bf2py
```

but make sure that you have git installed.


# Quick Start

```python
import bf2py

# Execute Brainfuck code directly
result = bf2py.execute("++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.")
print(result)  # Output: "Hello World!\n"

# Convert Brainfuck to Python code
python_code = bf2py.compile_to_python("+++>++<[->+<]>.")
print(python_code)
```

Command Line Usage

```bash
# Execute a Brainfuck file
bf2py hello_world.bf

# Execute Brainfuck code from string  
bf2py -c "++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++."

# Compile to Python without executing
bf2py --compile-only program.bf
```

# License

MIT License
