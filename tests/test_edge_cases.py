"""
Edge case tests for Bython
"""

import pytest
import bython
from bython import Bython, BythonSyntaxError


class TestEdgeCases:
    """Test edge cases and boundary conditions"""
    
    def test_very_long_program(self):
        """Test with very long Brainfuck program"""
        long_code = "+" * 1000 + "." + "-" * 500 + "." + ">" * 100 + "+."
        result = bython.execute(long_code, "")
        # Should execute without errors
        assert len(result) == 3
    
    def test_only_brackets(self):
        """Test program with only brackets"""
        # This should be valid syntax (though meaningless)
        result = bython.execute("[][]", "")
        assert result == ""
    
    def test_deeply_nested_loops(self):
        """Test very deeply nested loops"""
        # Create deeply nested loops: [[[[[]]]]]
        nested_loops = "+" + "[" * 10 + "-" + "]" * 10 + "."
        result = bython.execute(nested_loops, "")
        assert result == chr(1)
    
    def test_memory_tape_boundaries(self):
        """Test operations at memory tape boundaries"""
        # Test moving beyond both ends of tape
        code = "<" * 10 + "+" * 5 + ">" * 10 + "."  # Move left, increment, move right, output
        result = bython.execute(code, "")
        assert result == chr(5)
    
    def test_unicode_input(self):
        """Test with Unicode input characters"""
        result = bython.execute(",.", "😊")
        # Brainfuck typically uses ASCII, but should handle Unicode input
        assert result == "😊"[0]  # First byte of the emoji
    
    def test_special_ascii_characters(self):
        """Test with special ASCII characters"""
        for char in ["\n", "\t", "\r", "\x00"]:
            result = bython.execute(",.", char)
            assert result == char
    
    def test_concurrent_instances(self):
        """Test multiple concurrent Bython instances"""
        interpreter1 = Bython(memory_size=100)
        interpreter2 = Bython(memory_size=200)
        
        result1 = interpreter1.execute_direct("+++.", "")
        result2 = interpreter2.execute_direct("---.", "")
        
        assert result1 == chr(3)
        assert result2 == chr(253)  # 256 - 3
    
    def test_repeated_execution(self):
        """Test repeated execution with same interpreter"""
        interpreter = Bython()
        
        results = []
        for i in range(5):
            result = interpreter.execute_direct("+.", "")
            results.append(result)
        
        # Each execution should be independent
        assert all(r == chr(1) for r in results)
    
    def test_large_output(self):
        """Test program that produces large output"""
        # Program that outputs many characters
        code = "+++[.>]"  # Output 3, then move and output (will hit zero and stop)
        result = bython.execute(code, "")
        assert len(result) == 4  # 3 plus the zero at the end
    
    def test_no_operations(self):
        """Test programs with no operations between brackets"""
        result = bython.execute("[[]]", "")
        assert result == ""
    
    def test_immediate_loop_exit(self):
        """Test loops that exit immediately"""
        result = bython.execute("[]+.", "")
        assert result == chr(1)
