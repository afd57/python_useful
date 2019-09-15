"""
Daily Coding Problem: Problem #269 [Easy]
For example, given the string .L.R....L, you should return LL.RRRLLL.

Given the string ..R...L.L, you should return ..RR.LLLL.
"""


def convert_number_arry(domino_string):
    domino_number_arry = []
    for letter in domino_string:
        if letter == ".":
            domino_number_arry.append(0)
        elif letter == "L":
            domino_number_arry.append(-1)
        elif letter == "R":
            domino_number_arry.append(1)
    return domino_number_arry


def play_domino(domino_number_arry):
    lenght = len(domino_number_arry)
    played_domino = domino_number_arry[:]
    domino_number_arry_tmp = domino_number_arry[:]
    while True:
        for i, side in enumerate(domino_number_arry_tmp):
            if (side == 1) and (i+1 < lenght):
                if played_domino[i+1] == 0:
                    played_domino[i+1] = 1
                elif played_domino[i+1] == -1:
                    played_domino[i+1] = 2
            elif (side == -1) and (i-1 >= 0):
                if played_domino[i-1] == 0:
                    played_domino[i-1] = -1
                elif played_domino[i-1] == 1:
                    played_domino[i-1] = 2
        if domino_number_arry_tmp == played_domino:
            break
        else:
            domino_number_arry_tmp = played_domino[:]

    return played_domino


def play_domino_refactoring(domino):
    domino_arry = list(domino)
    domino_result = domino_arry[:]
    lenght = len(domino_arry)

    while True:
        for i, side in enumerate(domino_arry):
            if side == "R" and i+1 < lenght:
                if domino_arry[i+1] == ".":
                    if i+2 < lenght and domino_arry[i+2] == "L":
                        domino_result[i+1] = "."
                    else:
                        domino_result[i+1] = "R"
            elif side == "L" and i-1 >= 0:
                if domino_arry[i-1] == ".":
                    if i-2 > 0 and domino_arry[i-2] == "R":
                        domino_result[i-1] = "."
                    else:
                        domino_result[i-1] = "L"
        if domino_arry == domino_result:
            break
        else:
            domino_arry = domino_result[:]
    print(''.join(domino_arry))
    return domino_result


def display_domino(played_domino):
    string_domino_result = ""
    for number in played_domino:
        if number == 2 or number == 0:
            string_domino_result += "."
        elif number == 1:
            string_domino_result += "R"
        elif number == -1:
            string_domino_result += "L"
    return string_domino_result


if __name__ == "__main__":
    domino_string = ".L.R....L"
    domino_string2 = "..R...L.L"

    # domino_number_arry = convert_number_arry(domino_string)
    # print(domino_number_arry)
    # played = play_domino(domino_number_arry)
    # print(played)
    # print(display_domino(played))

    domino_result = play_domino_refactoring(domino_string2)
    print(domino_result)
    """
    domino_number_arry = convert_number_arry(domino_string2)
    print(domino_number_arry)
    played = play_domino(domino_number_arry)
    print(played)
    print(display_domino(played))
    """
