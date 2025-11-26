"""
BrainPy - Brainfuck to Python converter and executor

A library that converts Brainfuck code to Python and executes it.
"""

__version__ = "0.1.0"
__author__ = "Dmitry Seksov"

# Import core functionality
try:
    from .core import BrainPy
    from .exceptions import BrainPyError, BrainPySyntaxError, BrainPyRuntimeError
except ImportError as e:
    print(f"Import error: {e}")
    # Define fallbacks if import fails
    class BrainPyError(Exception):
        pass
    
    class BrainPySyntaxError(BrainPyError):
        pass
    
    class BrainPyRuntimeError(BrainPyError):
        pass
    
    class BrainPy:
        def __init__(self, memory_size=30000):
            self.memory_size = memory_size

__all__ = [
    "BrainPy",
    "BrainPyError", 
    "BrainPySyntaxError",
    "BrainPyRuntimeError",
    "execute",
    "compile_to_python"
]

def execute(brainfuck_code, input_data="", memory_size=30000):
    """
    Execute Brainfuck code directly.
    """
    interpreter = BrainPy(memory_size=memory_size)
    return interpreter.execute(brainfuck_code, input_data)

def compile_to_python(brainfuck_code, memory_size=30000):
    """
    Convert Brainfuck code to Python code.
    """
    interpreter = BrainPy(memory_size=memory_size)
    return interpreter.compile(brainfuck_code)
