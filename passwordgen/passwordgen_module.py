import random
import string


def passwordgen():
    spec_char_list = "!@#$%^&*()?"
    pw_length = random.randint(8, 13)
    pw = ""
    for i in range(0, pw_length):
        random_char_type = random.randint(0, 2)
        if random_char_type == 0:
            pw += string.ascii_letters[random.randint(0, 51)]
        elif random_char_type == 1:
            pw += string.digits[random.randint(0, 9)]
        elif random_char_type == 2:
            pw += spec_char_list[random.randint(0, 10)]

    pw += string.ascii_letters[random.randint(0, 25)]
    pw += string.ascii_letters[random.randint(26, 51)]
    pw += string.digits[random.randint(0, 9)]
    pw += spec_char_list[random.randint(0, 10)]

    return pw


def main():
    word_list = ["kutya", "cica", "tündi", "móni", "1234",
                 "password", "naezajelszavam", "gyengejelszó", "asdasd"]
    strenght = input("How strong you want your password be (strong / weak): ")

    if strenght == "strong":
        print(passwordgen())
    else:
        print(word_list[random.randint(0, len(word_list))])

    return


if __name__ == '__main__':
    main()
