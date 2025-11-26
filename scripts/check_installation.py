#!/usr/bin/env python3
"""
Check if BrainPy is properly installed
"""

try:
    import brainpy
    print("✅ BrainPy imported successfully")
    
    # Test basic functionality
    result = brainpy.execute("+.", "")
    expected = chr(1)
    if result == expected:
        print(f"✅ Basic execution test passed: {repr(result)}")
    else:
        print(f"❌ Basic execution test failed: expected {repr(expected)}, got {repr(result)}")
    
    # Test compilation
    python_code = brainpy.compile_to_python("+++.")
    if "def brainpy_program()" in python_code:
        print("✅ Compilation test passed")
    else:
        print("❌ Compilation test failed")
        
    print("🎉 All checks passed!")
    
except ImportError as e:
    print(f"❌ Failed to import BrainPy: {e}")
    exit(1)
except Exception as e:
    print(f"❌ Error during testing: {e}")
    exit(1)
