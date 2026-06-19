# 1. Create a list with 5 items (names of people) and output the 2nd item.
names = ["Jamey", "John", "James", "Jethro", "Jonathan"]
print("2nd item:", names[1])

# 2. Change the value of the first item to a new value.
names[0] = "Alex"
print("After changing 1st item:", names)

# 3. Add a sixth item to the list.
names.append("Judith")
print("After adding 6th item:", names)

# 4. Add “Bathel” as the 3rd item in your list.
names.insert(2, "Bathel")
print("After inserting Bathel:", names)

# 5. Remove the 4th item from the list.
# Note: Charlie was 3rd, but inserting Bathel pushed Charlie to 4th index (index 3).
removed_item = names.pop(3)
print(f"After removing 4th item ({removed_item}):", names)

# 6. Use negative indexing to print the last item in your list.
print("Last item:", names[-1])

# 7. Create a new list with 7 items and use a range of indexes to print the 3rd, 4th and 5th items.
# Indices for 3rd, 4th, 5th items are 2, 3, 4. Slicing is [start:stop_exclusive] -> [2:5]
numbers = [10, 20, 30, 40, 50, 60, 70]
print("3rd, 4th, and 5th items:", numbers[2:5])

# 8. Write a list of countries and make a copy of it.
countries = ["Uganda", "Kenya", "Tanzania", "Rwanda"]
countries_copy = countries.copy()

# 9. Write a python program to loop through the list of countries.
print("Looping through countries:")
for country in countries:
    print(f"- {country}")

# 10. Write a list of animal names and sort them in both descending and ascending order.
animals = ["Zebra", "Lion", "Elephant", "Antelope", "Girafe"]
animals.sort()
print("Ascending order:", animals)
animals.sort(reverse=True)
print("Descending order:", animals)

# 11. Output only animal names with the letter ‘a’ in them (case-insensitive check).
print("Animals with 'a' in their name:")
for animal in animals:
    if "a" in animal.lower():
        print(f"- {animal}")

# 12. Write two lists (first names and second names) and join them.
first_names = ["John", "Jane"]
second_names = ["Doe", "Smith"]
full_names = first_names + second_names
print("Joined names list:", full_names)