def get_count_char(str):
    one_str = " ".join(main_str.split())
    low_str = one_str.lower()
    dict_ = {}
    for char in low_str:
        if char.isalpha():
            if not (char in dict_.keys()):
                dict_[char] = 1
            else:
                dict_[char] += 1
    return dict_


def calc_proc_(dictionary):
    calc_proc = 0
    for i in dictionary:
        calc_proc += dictionary[i]
    new_dict_ = {}
    for i in dictionary:
        new_dict_[i] = int(dictionary[i] / calc_proc * 100)
    return new_dict_

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
print(calc_proc_(get_count_char(main_str)))
