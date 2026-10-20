favorite_foods = ["piiza","ramen","chocolate","ice cream","sushi"]
print(favorite_foods[1])
print(favorite_foods[-1])
favorite_foods.append("pasta")
favorite_foods.insert(0, "apple")
del favorite_foods[2]
print(len(favorite_foods))
for food in favorite_foods:
    print(food.upper())
newlist = [favorite_foods[0],favorite_foods[-1]]
if "potato" in favorite_foods:
    print("A potato!")
else:
    print("No potato!")

numbers = list(range(0,20))
def get_first_15(lst):
    return lst[:15]
def get_every_5th(lst):
    return lst[::5]
def reverse_and_stride(lst):
    reversed_list = lst[::-1]
    return reversed_list[::3]
step1 = get_first_15(numbers)
step2 = get_every_5th(step1)
step3 = reverse_and_stride(step2)

number = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]
print(number[2])
print(number[1][1])
numbers.append([10, 11, 12])
def sum_nested(x):
    total = 0
    for row in x:
        for item in row:
            total += item
    return total
print(sum_nested(number))

def grid():
    grid_inside = []
    value = 1
    for a in range(5):
        row = []
        for b in range(5):
            row.append(value)
            value += 1
        grid_inside.append(row)
    return grid_inside

new_grid = grid()
def replace3(x):
    for a in range(len(x)):
        for b in range(len(x[a])):
            if x[a][b] % 3 == 0:
                x[a][b] = "?"
    return x
new_grid = replace3(new_grid)

def sum_not_question(x):
    total = 0
    for row in x:
        for item in row:
            if item != "?":
                total += item
    return total
sum = sum_not_question(new_grid)
print(sum)

ages = {
"Katie": 30,
"Mariam": 42,
"Safia": 25,
"Mira": 48
}
print(ages["Katie"])
ages["Mira"] = 100
ages["Milana"] = 52
ages.pop("Mariam")

for name, age in ages.items():
    print(name, age)

grid()
print(grid())
print(replace3(grid()))
