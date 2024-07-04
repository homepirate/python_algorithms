class Stack:

    def __init__(self):
        self.__items = []

    def add(self, item):
        self.__items.append(item)

    def remove(self):
        return self.__items.pop()

    def __len__(self):
        return len(self.__items)


def check_str(string):
    st = Stack()
    flag = True

    for lt in string:
        if lt in '{[(':
            st.add(lt)
        elif lt in ']})':
            if len(st) == 0:
                flag = False
                break
            last = st.remove()
            if last == '(' and lt == ')':
                continue
            elif last == '[' and lt == ']':
                continue
            elif last == '{' and lt == '}':
                continue

            flag = False
            break
    flag = True if (flag and len(st) == 0) else False
    return flag


def main():
    print(check_str('()[]'))


if __name__ == '__main__':
    main()
