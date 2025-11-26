#!/usr/bin/env python3
"""
Command-line interface for Bython
"""

import argparse
import sys
import os
from .core import Bython
from .exceptions import BythonError

def main():
    parser = argparse.ArgumentParser(description='Bython - Brainfuck to Python converter and executor')
    parser.add_argument('file', nargs='?', help='Brainfuck file to execute')
    parser.add_argument('-c', '--code', help='Brainfuck code string to execute')
    parser.add_argument('-o', '--output', help='Output file for Python code')
    parser.add_argument('-i', '--input', help='Input data for the Brainfuck program')
    parser.add_argument('-m', '--memory', type=int, default=30000, help='Memory size (default: 30000)')
    parser.add_argument('--compile-only', action='store_true', help='Only compile to Python, do not execute')
    
    args = parser.parse_args()
    
    if not args.file and not args.code:
        parser.error("Either file or --code must be provided")
    
    try:
        # Read Brainfuck code
        if args.code:
            brainfuck_code = args.code
        else:
            with open(args.file, 'r') as f:
                brainfuck_code = f.read()
        
        # Create interpreter
        interpreter = Bython(memory_size=args.memory)
        
        if args.compile_only:
            # Compile to Python
            python_code = interpreter.compile(brainfuck_code)
            
            if args.output:
                with open(args.output, 'w') as f:
                    f.write(python_code)
                print(f"Python code written to {args.output}")
            else:
                print(python_code)
        else:
            # Execute directly
            input_data = args.input or ""
            result = interpreter.execute_direct(brainfuck_code, input_data)
            print(result, end='')
            
    except BythonError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
