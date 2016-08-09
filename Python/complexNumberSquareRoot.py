import math;

def root_if_real(number):
    print(math.sqrt(number)) if number >= 0 else print(str(math.sqrt(number * -1.0)) + "i");
        
def root_if_not(re, im):
    theta = math.atan(im / re);
    r = math.sqrt(re ** 2 + im ** 2);
    
    theta /= 2;
    
    final_re = math.sqrt(r) * math.cos(theta);
    final_im = math.sqrt(r) * math.sin(theta);
    sign = " + " if final_im >= 0 else " - ";
   
    if(final_im < 0.0):
        final_im *= -1.0;
    
    print(str(final_re) + sign + str(final_im));
    
def get_input():
    re = im = 0.0;
    array = [];
    
    try:
        re = float(input("Enter the real part: "));
        im = float(input("Enter the imaginary part: "));
    except:
        print("Bitch be like givin' me strings now!");
        
    array.append(re);
    array.append(im);
    
    return array;

data = get_input();

if(data[1] == 0.0):
    root_if_real(data[0]);
    
else:
    root_if_not(data[0], data[1]);