# Binary Search (Out-place)
def binary_search(array, left, right, target):
    # Not Found
    if left > right:
        return -1  # Not found

    mid = (left + right) // 2
    print(array[left : right + 1])  # Print current search range
    if array[mid] == target:
        return mid  # Return index where found
    elif array[mid] < target:
        return binary_search(array, mid + 1, right, target)
    else:
        return binary_search(array, left, mid - 1, target)


def main():
    data = [1, 3, 5, 7, 9, 11, 13, 15]
    target = 8

    index = binary_search(data, 0, len(data) - 1, target)

    if index != -1:
        print(f"값 {target}은 인덱스 {index}에 있습니다.")
    else:
        print(f"값 {target}은 배열에 없습니다.")


if __name__ == "__main__":
    main()
