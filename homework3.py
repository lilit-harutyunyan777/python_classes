# Python program to Convert Kilometers to Miles( kilometers should give the user)
Kilometer = int(input("Write kilometer\n"))
Mile = Kilometer / 1.609344
print(Kilometer, "km =", Mile, "mi")

#create an app which will exchange the given amount of money to dollar, dollar rate should be taken from another file
from rate import rate_AMD
value_AMD = int(input("Write AMD\n"))
value_USD = value_AMD * rate_AMD
print(value_AMD, "AMD =", value_USD, "USD")

#Ask user his height and tell him the optimal weight depending of his height.Google will help you, how to calculate this.

my_height = int(input("Height in cm\n"))
my_optimal_weight_m = 50 + (0.91 * (my_height - 152.4))
my_optimal_weight_f = 45.5 + (0.91 * (my_height - 152.4))
print("Optimal weight for male is", int(my_optimal_weight_m), "kg")
print("Optimal weight for female is", int(my_optimal_weight_m), "kg")

#Write python program for food court. There should be a menu with two dishes, pizza and kebab, and two additions ketchup, “Mayonez” all should have their prices. Depending on the answers of the user the value of the price row should be True .
#EX. pizza = 1000 , ketchup = 100, Mayonez = 500
#User ordered pizza with ketchup then in terminal should be seen
#	You have ordered pizza with Mayonez and your price is 1500 => False
#	You have ordered pizza with Ketchup and your price is 1100 => True
#You should NOT use if/elif/else statement
#Hello



#pizza = 1000 ,kebab = 1200, ketchup = 100, mayonez = 500, 

order_pizza = bool(int(input("Would you like to have some pizza(1/0)")))
order_kebab = bool(int(input("Would you like to have some kebab(1/0)")))
order_mayo = bool(int(input("Would you like to have some mayo(1/0)")))
order_ketchup = bool(int(input("Would you like to have some ketchup(1/0)")))

print("You have ordered", order_pizza * "pizza", order_kebab * "kebab", "with", order_mayo * "mayo", order_ketchup * "ketchup", "and your price is", order_pizza * 1000 + order_kebab * 1200 + order_mayo * 500 + order_ketchup * 100, sep = " ")
