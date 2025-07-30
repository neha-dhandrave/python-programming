# Step 1: Create a list
fruits = ["Apple", "Banana", "Mango"]
print("Initial List:", fruits)

# Step 2: Append elements to the list
fruits.append("Orange")
fruits.append("Grapes")
print("After Appending Elements:", fruits)

# Step 3: Remove specific elements
fruits.remove("Banana")  # Removes "Banana" from the list
print("After Removing 'Banana':", fruits)

# Step 4: Remove by index using pop()
removed_item = fruits.pop(2)  # Removes item at index 2
print(f"After Popping index 2 ('{removed_item}'):", fruits)

# Step 5: Clear the entire list (optional)
# fruits.clear()
# print("After Clearing the List:", fruits)
