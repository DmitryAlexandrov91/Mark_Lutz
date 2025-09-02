def while_func(number):
    res = ""
    while number:
        res += f"{number} "
        number -= 1
    return res + "stop"


def countdown(number):
    if number < 1:
        return "stop"
    else:
        return str(number) + " " + countdown(number - 1)


result = ''.join(
    [f"{number} " if number != 0 else "stop" for number in range(5, -1, -1)]
)
