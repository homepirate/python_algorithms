
def get_pi(word):
    pi = [0] * len(word)
    j = 0
    i = 1

    while i < len(word):
        if word[j] == word[i]:
            pi[i] = j + 1
            i += 1
            j += 1
        else:
            if j == 0:
                pi[i] = 0
                i += 1
            else:
                j = pi[j-1]
    return pi


def find(word, text):
    pi = get_pi(word)
    i = 0
    j = 0
    while i < len(text):
        if text[i] == word[j]:
            i += 1
            j += 1
            if j == len(word):
                print('Образ найден')
                return i - len(word), i
        else:
            if j > 0:
                j = pi[j-1]
            else:
                i += 1
    if i == len(text):
        print('Образ не найден')
        return


def main():
    result = find('лилила', 'лилилось лилилась')
    a, b = result if result else (0, 0)
    print(a, b, 'лилилось лилилась'[a:b])


if __name__ == '__main__':
    main()
