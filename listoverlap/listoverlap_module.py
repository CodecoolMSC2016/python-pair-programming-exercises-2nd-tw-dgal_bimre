import random


def listoverlap(list1, list2):
    return list(set(list1) & set(list2))


def main():
    print(listoverlap(random.sample(range(1, 100), random.randint(5, 100)),
                      random.sample(range(1, 100), random.randint(5, 100))))
    return


if __name__ == '__main__':
    main()
