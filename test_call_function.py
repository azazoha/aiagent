from functions.call_function import call_function

class test_function:
    name = "get_file_content"
    args = {"file_path": "main.py"}

test_functions = test_function()

"""
result = call_function(test_functions)
print(f"result: {result}")
"""

result = call_function(test_functions)
print(f"result: {result}")