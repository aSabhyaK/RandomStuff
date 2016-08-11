def checkIfStaircase(number):
    n = str(number);
    length = len(n);
    
    start = int(n[0]);
    end = int(n[length - 1]);
    
    return start * start + end * end == int(n[1:length - 1]);
    
lower_limit = 10000;
upper_limit = 99999;

for i in range(lower_limit, upper_limit, 1):
        if(checkIfStaircase(i)):
            print(i);
