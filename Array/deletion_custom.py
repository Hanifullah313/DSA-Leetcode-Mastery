
arr = [10, 20, 30, 40]

print("Array before deletion")
for i in range(len(arr)):
    print(arr[i], end=" ")

n= len(arr)
# Shift all elements to the left
for i in range(1, n):
    arr[i - 1] = arr[i]

n-=1
print("\nArray after deletion")
for i in range(n):
    print(arr[i], end=" ")