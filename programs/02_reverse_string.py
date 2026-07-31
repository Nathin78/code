# Reverse a string using slicing and loop
def reverse_string(s):
    return s[::-1]

def reverse_string_loop(s):
    result = ""
    for ch in s:
        result = ch + result
    return result

print(reverse_string("hello"))         # olleh
print(reverse_string_loop("python"))   # nohtyp
