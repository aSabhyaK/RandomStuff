def isPalindrome(number):
    length = len(number);
    
    for i in range(0, int(length / 2 + 1), 1):
        if(number[i] != number[length - 1 - i]):
            return False;
            
    return True;
    
count = 0;
for i in range(0, 1000, 1):
    if(isPalindrome(str(i))):
        print(i);
        count += 1;
        
print("count", count);