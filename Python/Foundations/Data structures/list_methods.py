# *************************************************************************************************
#                                     LIST METHODS IN PYTHON
# *************************************************************************************************
# 1. append()
# 2. insert()
# 3. extend()
# 4. remove()
# 5. pop()
# 6. index()
# 7. count()
# 8. sort()
# 9. sort() - Descending Order
# 10. reverse()
# 11. copy()
# 12. clear()


# REAL-TIME EXAMPLE: ONLINE SHOPPING CART
# ----------------------------------------

# List with duplicate values
cart = ["Laptop", "Mouse", "Laptop", "Keyboard", "Mouse", "Laptop"]

cart = ["Laptop", "Mouse", "Keyboard"]
print("List Values: ",cart)

# 1. APPEND()
cart.append("Headphones")
print("After Append: ",cart)

# 2. INSERT()
cart.insert(2, "Webcam")
print("Inserted_Values: ",cart)

# 3. EXTEND()
cart.extend(["USB Cable", "Speaker"])
print("Extended_Values: ",cart)

# 4. REMOVE()
cart.remove("Mouse")
print("After Remove_values: ",cart)

# 5. POP()
cart.pop(2)
print("After Popped_Values: ",cart)

# 6. INDEX()
print("Index of Laptop is: ",cart.index("Laptop"))

# 7. COUNT()
cart.append("Keyboard")
product = "Keyboard"
print("Count of ",product,"is: ",cart.count(product))


# 8. SORT()
cart.sort()
print("Ascending Order: ",cart)

# 9. SORT() - DESCENDING ORDER
cart.sort(reverse=True)
print("Descending order: ",cart)

# 10. REVERSE()
cart.reverse()
print("Reversed Order: ",cart)

# 11. COPY()
saved_cart = cart.copy()
print("Duplicate list:  ",cart)
print("Original list:", cart)
print("Copied list:", saved_cart)

# 12. CLEAR()
cart.clear()
print("After Clear:  ",cart)

# 13. DELETE THE LIST
# It shows whether the list exists or not
# del cart
# if "cart" in locals():
#     print("List exists")
# else:
#     print("List is deleted")

# It shows only True or False
del cart
print("cart" in locals())