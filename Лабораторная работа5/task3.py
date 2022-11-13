def get_unique_list_numbers() -> list[int]:
    from random import randint
    un = []
    while len(un) != 15:
        for i in range(15):
            i = randint(-10, 10)
        if i in un:
            continue
        else:
            un.append(i)
    return un


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
