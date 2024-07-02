import random


def bubble_sort(a):
    array = a.copy()
    for i in range(len(array)-1):
        for j in range(0, len(array)-1-i):
            if array[j+1] < array[j]:
                array[j+1], array[j] = array[j], array[j+1]
    return array


def main():
    random_arrays = [[random.randint(-100, 100) for _ in range(random.randint(5, 20))] for _ in range(10)]

    for array in random_arrays:
        res = bubble_sort(array)
        print(res == sorted(array))


if __name__ == '__main__':
    main()
