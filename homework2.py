
#Write a short program that will covert °C to °F.

#3. The third task is very abstract, you need to write some code where you will use all the functions that we have learned in last two lessons


temperature1 = 37.5 # °C
temperature2 = (temperature1 * 1.8 + 32) # °F
print (temperature2, "°F", sep="")

#Create 3 variable ( a = 5, b = 6, c = 7),and write a program which sums and prints out
#the average value of a, b, c
#a^c + b^c (2^4 in python is 2**4)
#(a + b)^c
#abc + a*b*c  (for our case: 567 + 5*6*7)

a = 5
b = 6
c = 7
result_1 = int((a + b + c) / 3)
print(result_1)

result_2 = (a ** c + b ** c)
print(result_2)

result_3 = ((a + b) ** c)
print(result_3)

result_4 = ((a + b) ** c)
print(result_4)

result_5 = int(str(a) + str(b) + str(c)) + a * b * c
print(result_5)

# a = First price,  b = Packing price
a = 70
b = 10
c = a + b
d = c *7 / 100
print ("Calculate Manufacturing cost =", d)
e = c * 3 / 100
print ("Calculate Administrative cost =", e)
f = (c + d + e) * 20 / 100
print ("Profit = ", f )
h = (c + d + e) * 16.67 / 100
print ("Calculate Tax =", h)
f += c + d + e + f
print ("Planing Price =", int(f))
p = f % 10 
print ("New price =" , end = " ")
q = (int(f + 10 - p))
print (q)
k = 130
print ("Actual price =", k)
print (bool(k-q) * "Change price")

word_1 = "hi"
word_2 = "bye"
print (word_1 + word_2)