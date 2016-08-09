import math;

def cube_root(n):
    multiplier = -1 if n < 0 else 1;
    root = int(math.pow(n * multiplier, float(1) / 3));
    return -root if multiplier == -1 else root;

n = 196;
smallerOrEqual = cube_root(n);
largerOrEqual = smallerOrEqual + 1 if smallerOrEqual >= 0 else smallerOrEqual - 1;
print("The cube root of " + str(n) + " lies between " + str(smallerOrEqual) + " and " + str(largerOrEqual));