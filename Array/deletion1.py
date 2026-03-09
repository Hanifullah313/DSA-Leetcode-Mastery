if __name__ == "__main__":
    arr = [10, 20, 30, 40]
    n = len(arr)
    pos = 2

    print("Array before deletion")
    for i in range(n):
        print(arr[i], end=" ")

    # Delete the element at the given position
    for i in range(pos, n):
        arr[i - 1] = arr[i]
  
    if pos <= n:
        n -= 1
    # why we are doing this because we have to decrease the size of the array by 1 after deletion
    print("\nArray after deletion")
    for i in range(n):
        print(arr[i], end=" ")