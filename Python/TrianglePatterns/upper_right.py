#upper right triangle
"""
*****
 ****
  ***
   **
    *
"""

max_limit = 5;

for i in range(max_limit, 0, -1):
    for j in range(0, max_limit - i, 1):
        print(" ", end='');
    for k in range(0, i, 1):
        print("*", end='');        
    print();