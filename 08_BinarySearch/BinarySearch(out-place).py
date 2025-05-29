def binary_search(array, target):
    if not array:
        return -1

    mid = len(array) // 2
    print(array)
    if array[mid] == target:
        return mid
    elif array[mid] < target:
        return binary_search(array[mid + 1 :], target)  # 배열 슬라이싱 발생
    else:
        return binary_search(array[:mid], target)  # 배열 슬라이싱 발생


def main():
    data = [1, 3, 5, 7, 9, 11, 13, 15]
    target = 8

    index = binary_search(data, target)

    if index != -1:
        print(f"값 {target}은 인덱스 {index}에 있습니다.")
    else:
        print(f"값 {target}은 배열에 없습니다.")


if __name__ == "__main__":
    main()
