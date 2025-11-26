#!/usr/bin/env python3
"""
Basic smoke tests for BrainPy
"""

import sys
import os

# Add the brainpy package to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import brainpy
from brainpy import BrainPy, BrainPySyntaxError

def run_basic_tests():
    """Run basic functionality tests"""
    
    print("Running BrainPy basic tests...")
    
    # Test 1: Basic increment
    try:
        result = brainpy.execute("+.", "")
        assert result == chr(1), f"Expected chr(1), got {repr(result)}"
        print("✅ Basic increment test passed")
    except Exception as e:
        print(f"❌ Basic increment test failed: {e}")
        return False
    
    # Test 2: Input/output
    try:
        result = brainpy.execute(",.", "A")
        assert result == "A", f"Expected 'A', got {repr(result)}"
        print("✅ Input/output test passed")
    except Exception as e:
        print(f"❌ Input/output test failed: {e}")
        return False
    
    # Test 3: Compilation
    try:
        python_code = brainpy.compile_to_python("+++.")
        assert "def brainpy_program()" in python_code
        assert "memory[pointer]" in python_code
        print("✅ Compilation test passed")
    except Exception as e:
        print(f"❌ Compilation test failed: {e}")
        return False
    
    # Test 4: Error handling
    try:
        brainpy.execute("+++[--", "")  # Missing bracket
        print("❌ Syntax error test failed - should have raised an exception")
        return False
    except BrainPySyntaxError:
        print("✅ Syntax error test passed")
    except Exception as e:
        print(f"❌ Syntax error test failed: {e}")
        return False
    
    print("🎉 All basic tests passed!")
    return True

if __name__ == "__main__":
    success = run_basic_tests()
    sys.exit(0 if success else 1)
