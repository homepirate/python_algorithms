class Queue:
    def __init__(self):
        self.__items = []

    def add(self, item):
        self.__items.append(item)

    def remove(self):
        return self.__items.pop(0)

    def __len__(self):
        return len(self.__items)


def main():
    q = Queue()
    q.add(1)
    q.add(2)
    print(q.remove())


if __name__ == '__main__':
    main()

