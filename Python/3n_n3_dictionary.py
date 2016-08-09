global dictionary;
dictionary = dict();

def calculateCyclicity(digit):
    number = ord(digit) - 48;
    list = [number];
    an_arbitrarily_large_number = 100;
    
    for i in range(2, an_arbitrarily_large_number, 1):
        units_digit = unitsDigit(number ** i);
        
        if(units_digit == digit):
            break;
            
        list.append(ord(units_digit) - 48);
        
    return list;
    
#returns the units digit of the calculated exponent    
def initiateCalculation(number, exponent):
    units_digit = unitsDigit(number);
    units_digit_int = int(units_digit);
  
    if not units_digit_int in dictionary:
        dictionary[units_digit_int] = calculateCyclicity(units_digit);
        
    length = len(dictionary[units_digit_int]);
    
    return int(dictionary[units_digit_int][(exponent % length) - 1]);
    
def isDivisibleBy5(number):
    difference = abs(initiateCalculation(3, number) - initiateCalculation(number, 3));
    return difference == 5 or difference == 0;

def unitsDigit(number):
    string = str(number);
    length = len(string);
    return string[length - 1];
    
count = 0;

for i in range(1, 1000, 1):
    if(isDivisibleBy5(i)):
        count += 1;
        #print(i, end = ', ');
        
print("count:", count);