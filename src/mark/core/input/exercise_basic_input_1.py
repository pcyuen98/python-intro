# Objective - To get used to basic input

# What to do
# ==========
# 1. Input the food and print the price
# 2. Print invalid choice if wrong input

food_1 = "Mcdonald"
food_price_1 = "RM 10"
food_2 = "Nasi Lemak"
food_price_2 = "RM 2"
food_3 = "Mee Kosong"
food_price_3 = "RM 1"


print ("Food 1. Mcdonald RM 10")
print ("Food 2. Nasi Lemak RM 2")
print ("Food 3. Mee Kosong RM 1")

x = input("Enter your food choice here: Enter 1 2 or 3 ")

if (x == "1"):
	print ('Your selected food is ' + food_1 + ' and the total price is ' + food_price_1)

elif (x == "2"):
	print ('Your selected food is ' + food_2 + ' and the total price is ' + food_price_2)
elif (x == "3"):
	print ('Your selected food is ' + food_3 + ' and the total price is ' + food_price_3)
else:
	print("Invalid choice selected!")



# Quiz: If the food and drink is selectable, how do you calculate the total price?