from typing import List

def remove_element(arr: List[int], ele: int) -> int:
    k = 0
    for i in range(len(arr)):
        if arr[i]!= ele:
            # arr[k], arr[i] = arr[i], arr[k]
            arr[k] = arr[i]
            print(f"arr[k]: {arr[k]}, arr[i]: {arr[i]}, k: {k}, i: {i}")
            k += 1
    return k

def main():
    arr = [0, 1, 3, 0, 2, 2, 4, 2]
    ele = 2
    print(remove_element(arr, ele))

if __name__ == "__main__":
    main()