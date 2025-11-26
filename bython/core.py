import sys
from .exceptions import BythonSyntaxError, BythonRuntimeError

class Bython:
    """
    Bython - Brainfuck to Python converter and executor
    """
    
    def __init__(self, memory_size=30000):
        """
        Initialize the Bython interpreter.
        
        Args:
            memory_size (int): Size of the memory tape
        """
        self.memory_size = memory_size
        self.brainfuck_commands = set('><+-.,[]')
    
    def _validate_code(self, code):
        """
        Validate Brainfuck code for balanced brackets.
        
        Args:
            code (str): Brainfuck code to validate
            
        Raises:
            BythonSyntaxError: If brackets are unbalanced
        """
        stack = []
        for i, char in enumerate(code):
            if char == '[':
                stack.append(i)
            elif char == ']':
                if not stack:
                    raise BythonSyntaxError(f"Unmatched ']' at position {i}")
                stack.pop()
        
        if stack:
            raise BythonSyntaxError(f"Unmatched '[' at position {stack[0]}")
    
    def _find_matching_brackets(self, code):
        """
        Find matching brackets in Brainfuck code.
        
        Args:
            code (str): Brainfuck code
            
        Returns:
            dict: Mapping from open bracket positions to close bracket positions
        """
        bracket_map = {}
        stack = []
        
        for i, char in enumerate(code):
            if char == '[':
                stack.append(i)
            elif char == ']':
                if not stack:
                    raise BythonSyntaxError(f"Unmatched ']' at position {i}")
                open_pos = stack.pop()
                bracket_map[open_pos] = i
                bracket_map[i] = open_pos
        
        return bracket_map
    
    def compile(self, brainfuck_code):
        """
        Convert Brainfuck code to Python code.
        
        Args:
            brainfuck_code (str): Brainfuck code to convert
            
        Returns:
            str: Generated Python code
            
        Raises:
            BythonSyntaxError: If the Brainfuck code has syntax errors
        """
        # Clean the code - remove non-Brainfuck characters
        code = ''.join(char for char in brainfuck_code if char in self.brainfuck_commands)
        
        # Validate code
        self._validate_code(code)
        
        # Find matching brackets
        bracket_map = self._find_matching_brackets(code)
        
        # Generate Python code
        python_lines = [
            "def bython_program():",
            f"    memory = [0] * {self.memory_size}",
            "    pointer = 0",
            "    output = []",
            "    input_data = iter(input_data) if input_data else iter([])",
            "",
        ]
        
        indent_level = 1
        i = 0
        
        while i < len(code):
            char = code[i]
            
            if char == '>':
                python_lines.append("    " * indent_level + "pointer = (pointer + 1) % memory_size")
            elif char == '<':
                python_lines.append("    " * indent_level + "pointer = (pointer - 1) % memory_size")
            elif char == '+':
                python_lines.append("    " * indent_level + "memory[pointer] = (memory[pointer] + 1) % 256")
            elif char == '-':
                python_lines.append("    " * indent_level + "memory[pointer] = (memory[pointer] - 1) % 256")
            elif char == '.':
                python_lines.append("    " * indent_level + "output.append(chr(memory[pointer]))")
            elif char == ',':
                python_lines.extend([
                    "    " * indent_level + "try:",
                    "    " * (indent_level + 1) + "char = next(input_data)",
                    "    " * (indent_level + 1) + "memory[pointer] = ord(char) % 256",
                    "    " * indent_level + "except StopIteration:",
                    "    " * (indent_level + 1) + "memory[pointer] = 0"
                ])
            elif char == '[':
                python_lines.append("    " * indent_level + "while memory[pointer] != 0:")
                indent_level += 1
            elif char == ']':
                indent_level -= 1
            
            i += 1
        
        python_lines.extend([
            "",
            "    return ''.join(output)",
            "",
            "result = bython_program()",
            "print(result, end='')"
        ])
        
        return '\n'.join(python_lines)
    
    def execute(self, brainfuck_code, input_data=""):
        """
        Execute Brainfuck code directly.
        
        Args:
            brainfuck_code (str): Brainfuck code to execute
            input_data (str): Input data for the program
            
        Returns:
            str: Output of the Brainfuck program
            
        Raises:
            BythonSyntaxError: If the Brainfuck code has syntax errors
            BythonRuntimeError: If there's a runtime error during execution
        """
        try:
            python_code = self.compile(brainfuck_code)
            
            # Create a namespace for execution
            namespace = {
                'input_data': input_data,
                'print': lambda x, **kwargs: None  # Override print to capture output
            }
            
            # Redirect stdout to capture output
            import io
            from contextlib import redirect_stdout
            
            output_capture = io.StringIO()
            
            with redirect_stdout(output_capture):
                exec(python_code, namespace)
            
            return output_capture.getvalue()
            
        except BythonSyntaxError:
            raise
        except Exception as e:
            raise BythonRuntimeError(f"Runtime error: {str(e)}")
    
    def execute_direct(self, brainfuck_code, input_data=""):
        """
        Execute Brainfuck code directly without converting to Python first.
        This is more efficient for simple execution.
        
        Args:
            brainfuck_code (str): Brainfuck code to execute
            input_data (str): Input data for the program
            
        Returns:
            str: Output of the Brainfuck program
        """
        # Clean the code
        code = ''.join(char for char in brainfuck_code if char in self.brainfuck_commands)
        
        # Validate code
        self._validate_code(code)
        
        # Find matching brackets
        bracket_map = self._find_matching_brackets(code)
        
        # Initialize state
        memory = [0] * self.memory_size
        pointer = 0
        output = []
        input_iter = iter(input_data)
        
        # Execute
        i = 0
        while i < len(code):
            char = code[i]
            
            if char == '>':
                pointer = (pointer + 1) % self.memory_size
            elif char == '<':
                pointer = (pointer - 1) % self.memory_size
            elif char == '+':
                memory[pointer] = (memory[pointer] + 1) % 256
            elif char == '-':
                memory[pointer] = (memory[pointer] - 1) % 256
            elif char == '.':
                output.append(chr(memory[pointer]))
            elif char == ',':
                try:
                    char = next(input_iter)
                    memory[pointer] = ord(char) % 256
                except StopIteration:
                    memory[pointer] = 0
            elif char == '[':
                if memory[pointer] == 0:
                    i = bracket_map[i]
            elif char == ']':
                if memory[pointer] != 0:
                    i = bracket_map[i]
            
            i += 1
        
        return ''.join(output)
