"""
sum of the series: (1/1 . 1/3) + (1/3 . 1/5) + (1/5 . 1/7) + ...
"""

#n: number of terms
def sum(n):
    start = 1;
    sum = 0.0;
    
    for i in range(1, n + 1, 1):
        sum += (1.0 / start) * (1.0 / (start + 2));
        start += 2;
        
    return sum;

print(sum(10));
print(sum(100));
print(sum(1000));
print(sum(10000));
print(sum(100000));
print(sum(1000000));    
print(sum(10000000));