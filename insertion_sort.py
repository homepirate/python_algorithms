import random


def insert_sort(a):
    new_array = a.copy()
    for i in range(1, len(new_array)):
        for j in range(i, 0, -1):
            if new_array[j] < new_array[j-1]:
                new_array[j], new_array[j-1] = new_array[j-1], new_array[j]
            else:
                break
    return new_array


def main():
    random_arrays = [[random.randint(-100, 100) for _ in range(random.randint(5, 20))] for i in range(10)]

    for array in random_arrays:
        res = insert_sort(array)
        print(res == sorted(array))


if __name__ == '__main__':
    main()
