def palindrome(string):
    matchCount = 0
    lista = string.replace(" ", "").lower()
    for i in range(len(lista)):
        if lista[i] == lista[-1 - i]:
            matchCount += 1

    if matchCount == len(lista):
        return True
    else:
        return False


def main():
    print(palindrome("A nut for a jar of tuna"))
    return


if __name__ == '__main__':
    main()
