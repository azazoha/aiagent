from functions.run_python_file import run_python_file

result = run_python_file("calculator", "main.py")
print(f'result for run_python_file("calculator", "main.py"): {result}')

result = run_python_file("calculator", "main.py", ["3 + 5"])
print(f'result for run_python_file("calculator", "main.py", ["3 + 5"]): {result}')

result = run_python_file("calculator", "tests.py")
print(f'result for run_python_file("calculator", "tests.py"): {result}')

result = run_python_file("calculator", "../main.py")
print(f'result for run_python_file("calculator", "../main.py"): {result}')

result = run_python_file("calculator", "nonexistent.py")
print(f'result for run_python_file("calculator", "nonexistent.py"): {result}')

result = run_python_file("calculator", "lorem.txt")
print(f'result for run_python_file("calculator", "lorem.txt"): {result}')