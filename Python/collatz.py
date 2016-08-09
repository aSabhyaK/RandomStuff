def collatz(n):
    print(int(n));
    if(n == 1):
        return;
        
    return collatz(n / 2) if n % 2 == 0 else collatz(3 * n + 1);
            
collatz(6);