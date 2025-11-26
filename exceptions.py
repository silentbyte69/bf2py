class BythonError(Exception):
    """Base exception for Bython library"""
    pass

class BythonSyntaxError(BythonError):
    """Raised when there's a syntax error in Brainfuck code"""
    pass

class BythonRuntimeError(BythonError):
    """Raised when there's a runtime error during execution"""
    pass
