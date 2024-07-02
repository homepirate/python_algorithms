import random


def s_sort(a):
    i = 0
    j = 1

    while j < len(a):
        element_index = a[j: len(a)].index(min(a[j: len(a)])) + j
        if a[element_index] < a[i]:
            a[i], a[element_index] = a[element_index], a[i]
        i += 1
        j += 1

    return a


def main():
    random_arrays = [[random.randint(-100, 100) for _ in range(random.randint(5, 20))] for i in range(10)]

    for array in random_arrays:
        res = s_sort(array)
        print(res == sorted(array))


if __name__ == '__main__':
    main()

