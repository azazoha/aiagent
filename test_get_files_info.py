from functions.get_files_info import get_files_info


print(f"Result for current directory:")
result = get_files_info("calculator", ".")
print("\n".join(result))

print(f"Result for 'pkg' directory:")
result = get_files_info("calculator", "pkg")
print("\n".join(result))

print(f"Result for '/bin' directory:")
result = get_files_info("calculator", "/bin")
print(result)

print(f"Result for '../' directory:")
result = get_files_info("calculator", "../")
print(result)