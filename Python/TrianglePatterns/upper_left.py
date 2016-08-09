#upper left triangle
"""
*****
****
***
**
*
"""

max_limit = 5;

for i in range(max_limit + 1, 1, -1):
    for j in range(i, 1, -1):
        print("*", end='');
    print();