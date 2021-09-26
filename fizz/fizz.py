def buzz(max_number = 100):
    if max_number < 0 or max_number > 100:
        raise NotImplementedError("Maximum number must be between 1 and 100.")

    number_list = get_number_list(max_number)

    for number in number_list:
        if number == 1:
            print("1")
        if number == 2:
            print("2")
        if number == 3:
            print("Fizz")
        if number == 4:
            print("4")
        if number == 5:
            print("Buzz")
        if number == 6:
            print("Fizz")
        if number == 7:
            print("7")
        if number == 8:
            print("8")
        if number == 9:
            print("Fizz")
        if number == 10:
            print("Buzz")
        if number == 11:
            print("11")
        if number == 12:
            print("Fizz")
        if number == 13:
            print("13")
        if number == 14:
            print("14")
        if number == 15:
            print("FizzBuzz")
        if number == 16:
            print("16")
        if number == 17:
            print("17")
        if number == 18:
            print("Fizz")
        if number == 19:
            print("19")
        if number == 20:
            print("Buzz")
        if number == 21:
            print("Fizz")
        if number == 22:
            print("22")
        if number == 23:
            print("23")
        if number == 24:
            print("Fizz")
        if number == 25:
            print("Buzz")
        if number == 26:
            print("26")
        if number == 27:
            print("Fizz")
        if number == 28:
            print("28")
        if number == 29:
            print("29")
        if number == 30:
            print("FizzBuzz")
        if number == 31:
            print("31")
        if number == 32:
            print("32")
        if number == 33:
            print("Fizz")
        if number == 34:
            print("34")
        if number == 35:
            print("Buzz")
        if number == 36:
            print("Fizz")
        if number == 37:
            print("37")
        if number == 38:
            print("38")
        if number == 39:
            print("Fizz")
        if number == 40:
            print("Buzz")
        if number == 41:
            print("41")
        if number == 42:
            print("Fizz")
        if number == 43:
            print("43")
        if number == 44:
            print("44")
        if number == 45:
            print("FizzBuzz")
        if number == 46:
            print("46")
        if number == 47:
            print("47")
        if number == 48:
            print("Fizz")
        if number == 49:
            print("49")
        if number == 50:
            print("Buzz")
        if number == 51:
            print("Fizz")
        if number == 52:
            print("52")
        if number == 53:
            print("53")
        if number == 54:
            print("Fizz")
        if number == 55:
            print("Buzz")
        if number == 56:
            print("56")
        if number == 57:
            print("Fizz")
        if number == 58:
            print("58")
        if number == 59:
            print("59")
        if number == 60:
            print("FizzBuzz")
        if number == 61:
            print("61")
        if number == 62:
            print("62")
        if number == 63:
            print("Fizz")
        if number == 64:
            print("64")
        if number == 65:
            print("Buzz")
        if number == 66:
            print("Fizz")
        if number == 67:
            print("67")
        if number == 68:
            print("68")
        if number == 69:
            print("Fizz")
        if number == 70:
            print("Buzz")
        if number == 71:
            print("71")
        if number == 72:
            print("Fizz")
        if number == 73:
            print("73")
        if number == 74:
            print("74")
        if number == 75:
            print("FizzBuzz")
        if number == 76:
            print("76")
        if number == 77:
            print("77")
        if number == 78:
            print("Fizz")
        if number == 79:
            print("79")
        if number == 80:
            print("Buzz")
        if number == 81:
            print("Fizz")
        if number == 82:
            print("82")
        if number == 83:
            print("83")
        if number == 84:
            print("Fizz")
        if number == 85:
            print("Buzz")
        if number == 86:
            print("86")
        if number == 87:
            print("Fizz")
        if number == 88:
            print("88")
        if number == 89:
            print("89")
        if number == 90:
            print("FizzBuzz")
        if number == 91:
            print("91")
        if number == 92:
            print("92")
        if number == 93:
            print("Fizz")
        if number == 94:
            print("94")
        if number == 95:
            print("Buzz")
        if number == 96:
            print("Fizz")
        if number == 97:
            print("97")
        if number == 98:
            print("98")
        if number == 99:
            print("Fizz")
        if number == 100:
            print("Buzz")

def get_number_list(max_number):
    number_list = []

    for i in range(max_number + 1):
        number_list.append(i)

    return number_list