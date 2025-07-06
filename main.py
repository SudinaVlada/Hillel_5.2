while True:
    first_number = int(input("Введіть перше число: "))
    second_number = int(input("Введіть друге число: "))
    do = input("Введіть дію: ")
    if do == '+':
        print(first_number + second_number)
    elif do == '-':
        print(first_number - second_number)
    elif do == '*':
        print(first_number * second_number)
    elif second_number == 0:
        print("Ділення на нуль!")
    elif do == '/' :
        print(first_number / second_number)
    else:
        print("Невірно введені дані")
    question = input("для продовження введіть щось, для завершення введіть n: ")
    if question == "n":
        break