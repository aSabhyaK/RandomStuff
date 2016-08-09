def recursion(n, upper_limit):
    #base condition
    if(n == upper_limit):
        return n;
    
    return float(n) / (1.0 + recursion(n + 1.0, upper_limit));
    
#breaks at 990.0; works fine till 989.0
print(recursion(1.0, 989.0));