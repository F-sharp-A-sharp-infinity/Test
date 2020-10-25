current_number = 1
output = ""


def check(multiple, word):
    if current_number % multiple == 0:
        global output
        output += word


while current_number <= 100:
    output = ""
    check(3, "fizz")
    check(5, "buzz")
    if output == "":
        output = current_number
    print(output)
    current_number = current_number + 1
