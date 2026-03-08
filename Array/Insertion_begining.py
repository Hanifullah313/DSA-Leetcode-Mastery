# Python program to insert a given element at the beginning 
# of an array
# Approach 1
arr = [10, 20, 30, 40]
element = 50
print("Array before insertion")
for i in range(len(arr)):
	# print(arr[i], end=" ")

# Insert element at the beginning
# arr.insert(0, element)

# print("\nArray after insertion")
# for i in range(len(arr)):
    # print(arr[i], end=" ")


# Python program to insert given element at the beginning 
# of an array
# Approach 2
arr1 = [10, 20, 30, 40, 0]
n = 4
element = 50
    
print("Array before insertion")
for i in range(n):
    print(arr1[i], end=" ")
    
# Shift all elements to the right
for i in range(n - 1, -1, -1):
    arr[i + 1] = arr[i]

# Insert new element at the beginning
arr1[0] = element

print("\nArray after insertion")
for i in range(n + 1):
    print(arr1[i], end=" ")