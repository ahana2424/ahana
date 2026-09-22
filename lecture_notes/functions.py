"""
name = "ahana"
print("Hello", name)

def say_hello(name):
    print("Hello", name)

say_hello(name="ahana")

def add(a,b):
    print(a + b)

add(7,8)

def check_num(num):
    if num > 0:
        return"Positive"
    elif num < 0:
        return"Negative"
    else:
        return"Zero"

print(check_num(-5)) 


def can_vote(age, is_citizen):
    if age >= 18 and is_citizen:
        print("You can vote!")
    else:
        print("You cannot vote.")

can_vote(19, True)

def is_weekend(day):
    if day == "Saturday" or day == "Sunday":
        return "It is the weekend"
    else:
        return "It is a weekday"

print(is_weekend("monday"))


for i in range(10):
    print(i)

fruit_basket = ["apple", "banana", "cherry", "date"]

for fruit in fruit_basket:
    print(fruit)
    """

def countdown(start):
    while start > 0:
        print("t-", start)
        start -= 1
    print("Liftoff!")

countdown(10)