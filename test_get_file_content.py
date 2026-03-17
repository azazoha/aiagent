from functions.get_file_content import get_file_content

result = get_file_content("calculator", "lorem.txt")
print(f'result get_file_content("calculator", "lorem.txt"): {result}')


result = get_file_content("calculator", "main.py")
print(f'result get_file_content("calculator", "main.py")): {result}')


result = get_file_content("calculator", "pkg/calculator.py")
print(f'result get_file_content("calculator", "pkg/calculator.py")): {result}')

result = get_file_content("calculator", "/bin/cat")
print(f'result get_file_content("calculator", "/bin/cat"): {result}')

result = get_file_content("calculator", "pkg/does_not_exist.py")
print(f'result get_file_content("calculator", "pkg/does_not_exist.py"): {result}')
