from number_theory_functions import extended_gcd, modular_inverse


if __name__ == '__main__':
    """stages of thinking:
    The goal was to find how many coins we would have to give and how many coins we would have to receive back,
    Therefore the equation we would like to find is this 1000000=911x'-7879y'
    We understood that if we find the gcd(911,7879) And it is divisible by 1000000 So there is a solution
    1.so we wanted to solve the following equation : z=911x+7879y and find the gcd
    If 1000000 is not divisible by z we will return false otherwise we will return true
    2.When we found z we multiplied the whole equation by 1000000/z and return x and y 
    x represents the number of coins we paid with
    y represents the number of coins we received in excess
    """
    gcd ,x, y = extended_gcd(911, 7879)
    
    x=x*-1
    y=y*-1

    x= x*1000000
    y= y*1000000
    print(f"the number that allows ot will be x={x} and y={y}")

