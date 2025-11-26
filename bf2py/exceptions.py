class BF2PyError(Exception):
    """Base exception for bf2py library"""
    pass

class BF2PySyntaxError(BF2PyError):
    """Raised when there's a syntax error in Brainfuck code"""
    pass

class BF2PyRuntimeError(BF2PyError):
    """Raised when there's a runtime error during execution"""
    pass
