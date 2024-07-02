import random


def merge_lists(a: list, b: list):
    res_array = []
    f_array = a.copy()
    s_array = b.copy()
    i = j = 0
    while i < len(f_array) and j < len(s_array):
        if f_array[i] <= s_array[j]:
            res_array.append(f_array[i])
            i += 1
        else:
            res_array.append(s_array[j])
            j += 1
    res_array.extend(f_array[i:])
    res_array.extend(s_array[j:])

    return res_array


def main():
    a = [1, 2, 7]
    b = [2, 3, 5]
    print(merge_lists(a, b))
    random_arrays = [sorted([random.randint(-100, 100) for _ in range(random.randint(5, 20))]) for _ in range(10)]

    for i in range(0, len(random_arrays), 2):
        test_list = random_arrays[i].copy()
        test_list.extend(random_arrays[i+1])
        print(merge_lists(random_arrays[i], random_arrays[i+1]) == sorted(test_list))


if __name__ == '__main__':
    main()