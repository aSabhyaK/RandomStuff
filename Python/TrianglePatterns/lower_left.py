#lower left triangle
"""
*
**
***
****
*****
"""

max_limit = 5;

for i in range(0, max_limit, 1):
    for j in range(0, i + 1, 1):
        print("*", end='');
    print();
