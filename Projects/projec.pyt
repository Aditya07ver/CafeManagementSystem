#DEFINE THE MENU RESTAURENT

menu = {
    'Pizza': 40,
    'Pasta': 50,
    'Burger':60,
    'Salad': 70,
    'Coffee':80,
}
print("welcome to PYTHON Restaurent")
print(" Pizza: Rs40\n Pasta: Rs50\n Burger:Rs60\n Salad:Rs70\n Coffee: Rs80\n")

order_total = 0
# 80 + 70 = 150

item_1 = input("Enter the name of item your want to order = ")
if item_1 in menu:
    order_total += menu[item_1] # 0 + 50 
    print(f"Your item {item_1} has been added to your order")

else:
    print(f"Ordered item {item_1} is not available yet!")

another_order = input("Do you want to add another item? (YES/NO)")  
if another_order == "Yes":
  item_2 = input("Enter the name of second item = ")
  if item_2 in menu:
     order_total += menu[item_2]
     print(f"Item {item_2} has been added to order")
  else:
     print(f"Ordered Item{item_2} is not available!") 

print(f"the total amount of item to pay is {order_total}")