import datetime


def years(age):
    now = datetime.datetime.now()
    return now.year - age + 100


def main():
    name = input("Pease enter your name: ")
    age = int(input("Please enter your age: "))
    howmanytimes = int(input("How many times you want to know this: "))
    for i in range(howmanytimes):
        print(name + ", you will be 100 years old in " + str(years(age)))
    return


if __name__ == '__main__':
    main()
