def nth_fibonacci_number(n):
    if(n == 1 or n == 2):
        return 1;
        
    return nth_fibonacci_number(n - 1) + nth_fibonacci_number(n - 2);
    
for i in range(1, 10, 1):
    print(nth_fibonacci_number(i));
