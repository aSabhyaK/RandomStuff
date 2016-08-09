#lower right triange
"""
    *
   **
  ***
 ****
*****
"""

max_limit = 5;

for i in range(0, max_limit, 1):
    for j in range(max_limit - i, 0, -1):
        print(" ", end='');
    for k in range(0, i + 1, 1):
        print("*", end='');
    print();