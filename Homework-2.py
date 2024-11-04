# 1-Creating a list of my favorite fruits
favorite_fruits=["mango","apple","watermelon","grapes","guava"]
print(favorite_fruits)

# 2-Accessing the list elements
colors= ["red","blue","green","yellow","purple"]
#Printing the specific elements
print("First element:", colors[0])
print("Third element:", colors[2])
print("Last element:", colors[4])

# 3-Modifying the list
numbers=['10','20','30','40','50']
numbers[1] = '25'
numbers.append('60')
print(numbers)

# 4-Slicing the list
names=['Alice','Bob','Charlie','David','Emma']
subset=names[:3]
#Printing the first 3 names only
print(subset)

# 5-Looping through the list
numbers=list(range(1, 11))
for number in numbers:
    print(number ** 2)

# 6-Appending the list
shopping_cart=[]
shopping_cart.append('milk')
shopping_cart.append('bread')
shopping_cart.append('eggs')
#Extending the list
shopping_cart.extend(['butter','cheese'])
print(shopping_cart)

# 7-Finding maximum and minimum elements
numbers = [45, 22, 88, 56, 92, 33]
#Printing maximum numbers
print("Maximum numbers:", max(numbers))
#Printing minimum numbers
print("Minimum numbers:", min(numbers))

# 8-Counting occurences
letters = ['a', 'b', 'a', 'c', 'b', 'a', 'd']
count_of_a= letters.count('a')
print("Count of a:", count_of_a)

# 9-Comprehensing the list
even_squares=[x**2 for x in range(11) if x %2 == 0]
print("Squares of even numbers from 0 to 10:")
print(even_squares)

# 10-Removing duplicates from the given list
nums = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
unique_nums = []
[unique_nums.append(x) for x in nums if x not in unique_nums]
# Printing the original list
print("Original list:")
print(nums)
# Printing the list with unique elements
print("\nList with unique elements:")
print(unique_nums)







