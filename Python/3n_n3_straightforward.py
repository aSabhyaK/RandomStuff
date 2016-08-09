"""
3^n - n^3 = 5k , where k is an integer and n<1000 ; what are the values of n that satisfy this equation?
"""
def isDivisibleBy5(number):
    return (3 ** n - n ** 3) % 5 == 0;

count = 0;
for n in range(0, 1000, 1):
    if(isDivisibleBy5(n)):
        print(n, end = ', ');
        count += 1;
        
print("count:", count);