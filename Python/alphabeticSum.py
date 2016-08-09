def convert(string):
    sum = 0;
    
    for c in string:
        code_point = ord(c);
        location = code_point - 65 if code_point >= 65 and code_point <= 90 else code_point - 97;
        sum += location + 1;
        
    return sum;
    
print(convert("pyThOn"));
print(convert("PYTHON"));
print(convert("python"));