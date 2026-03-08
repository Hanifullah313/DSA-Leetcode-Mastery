# Python program to insert given element at a given position
# in an array using custom method

if __name__ == "__main__":
    n = 4
    arr = [10, 20, 30, 40, 0]
    ele = 50
    pos = 2
    print("Array before insertion")
    for i in range(n):
        print(arr[i], end=' ')

    # Shifting elements to the right
    for i in range(n, pos - 1, -1):
        arr[i] = arr[i - 1]

    # Insert the new element at index pos - 1
    arr[pos - 1] = ele

    print("\nArray after insertion")
    for i in range(n + 1):
        print(arr[i], end=' ')