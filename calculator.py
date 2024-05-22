# Write your code here
print("Earned amount:")
print("Bubblegum: $202")
bubblegum = int(202)
print("Toffee: $118")
toffee = int(118)
print("Ice cream: $2250")
ice_cream = int(2250)
print("Milk chocolate: $1680")
milk_chocolate = int(1680)
print("Doughnut: $1075")
doughnut = int(1075)
print("Pancake: $80\n")
pancake = int(80)

income = bubblegum + toffee + ice_cream + milk_chocolate + doughnut + pancake
print(f"Income: ${income}")

print("Staff expenses:")
staff_expenses = int(input())
print("Other expenses:")
other_expenses = int(input())

print(f"Net income: ${income - staff_expenses - other_expenses}")