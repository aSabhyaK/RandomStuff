#upper half triangle
"""
@@@@*@@@@
@@@*@*@@@
@@*@*@*@@
@*@*@*@*@
*@*@*@*@*
"""

#number of rows, basically
max_limit = 5;
filler = "@";

"""
for i in range(0, max_limit, 1):
    for j in range(0, max_limit - i - 1, 1):
        print(filler, end='');
    for k in range(0, 2 * i + 1, 1):
        if(k % 2 == 0):
            print("*", end='');
        else:
            print(filler, end='');
    for l in range(0, max_limit - i - 1, 1):
        print(filler, end='');
    print();
"""

#approach 2
twice = 2 * max_limit - 1;

for i in range(0, max_limit, 1):
    for j in range(0, twice, 1):
        twice_2 = int(twice / 2);
        if(j <= twice_2 - i or j > twice_2 + 1):
            print(filler, end='');
        else:
            for k in range(j, j + )
            print("*", end='');
    print();