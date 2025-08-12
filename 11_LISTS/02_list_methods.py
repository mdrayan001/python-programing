marks = [90, 85, 78, 92, 88]

print(marks)
marks.append(95)  # Adding an element to the end
print(marks)

# Removing an element
marks.remove(78)  # Removing the first occurrence of 78

# Inserting an element at a specific position
marks.insert(2, 80)  # Inserting 80 at index 2

# extending the list with another list
more_marks = [75, 88]
marks.extend(more_marks)  # Adding more elements to the end

# Sorting the list
marks.sort()  # Sorts the list in ascending order

