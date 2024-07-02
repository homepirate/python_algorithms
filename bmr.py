def get_table(word):
    s = set() # набор уникальных бук в word
    shifts = dict() # словарь смещений
    for i in range(len(word)-2 , -1 , -1):
        if word[i] not in s:
            shifts[word[i]] = len(word) - i - 1
            s.add(word[i])

    if word[len(word) - 1] not in s:
        shifts[word[len(word)-1]] = len(word)

    shifts['*'] = len(word)
    print(shifts)
    return shifts


def find(word, text):
    shifts = get_table(word)
    N = len(text)

    if N >= len(word):
        i = len(word)-1

        while i < N:
            k = 0
            for j in range(len(word)-1, -1, -1):
                if text[i-k] != word[j]:
                    if j == len(word) - 1:
                        off = shifts[text[i]] if shifts.get(text[i], False) else shifts['*']
                    else:
                        off = shifts[word[j]]

                    i += off
                    break
                k += 1
            if j == 0:
                return i-k+1
    return None


def main():
    print(find('данные', 'большие метеоданные'))


if __name__ == '__main__':
    main()
