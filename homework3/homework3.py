def say_goobye(name):
    print("Goodbye," , name)
#say_goobye("ahana")

def area_circle(r):
    return 3.14*r
#print(area_circle(5))

def subtract(a, b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

def temperature(readings):
    lowtemp = min(readings)
    hightemp = max(readings)
    return(lowtemp, hightemp)
readings = [15, 14, 17, 20, 23, 28, 20]
#print(temperature(readings))

def is_weekend(day):
    if day == 6 or day == 7:
        return True
    else:
        return False

def fuel_efficiency(distance, fuel):
    mpg = distance / fuel
    return mpg

def encrypt_data(number):
    last_digit = number % 10
    remaining_digits = number // 10
    
    temp = remaining_digits
    multiplier = 1
    while temp > 0:
        multiplier *= 10
        temp //= 10
        
    encrypted_number = (last_digit * multiplier) + remaining_digits
    return encrypted_number

def power(x, y):
    ans = 1
    for _ in range(y):
        ans = ans *x
    return ans 

#print(power(2,3))

def find_min(numbers):
    current_min = numbers[0]
    for num in numbers:
        if num < current_min:
            current_min = num
    return current_min


def find_max(numbers):
   
    current_max = numbers[0]
    for num in numbers:
        if num > current_max:
            current_max = num
    return current_max

#print(find_max([23,43,541,23]))

def min_while(numbers):
    min = numbers[0]
    x = 0
    while x < len(numbers):
        if numbers[x] < min:
            min = numbers[x]
        x += 1
    return min

def max_while(numbers):
    max = numbers[0]
    x = 0
    while x < len(numbers):
        if numbers[x] > max:
            max = numbers[x]
        x += 1
    return max

#print(max_while([23,43,541,23]))

def sum_digits(number):
    sum = 0
    number = abs(number) 
    while number > 0:
        sum += number % 10
        number //= 10
    return sum

print(f"The result of Check if it’s the Weekend (5.2) with day = {6} is {is_weekend(6)}.")