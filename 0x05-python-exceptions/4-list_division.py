#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []

    try:
        for i in range(list_length):
            element_1 = my_list_1[i] if i < len(my_list_1) else 0
            element_2 = my_list_2[i] if i < len(my_list_2) else 0

            try:
                result = element_1 / element_2
            except ZeroDivisionError:
                print("division by 0")
                result = 0
            except (TypeError, ValueError):
                print("wrong type")
                result = 0

            result_list.append(result)

    except IndexError:
        print("out of range")

    finally:
        return result_list
