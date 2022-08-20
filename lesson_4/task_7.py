def identical_numbers(first_list, second_list):
  first_list_set = set(first_list)
  second_list_set = set(second_list)

  if (first_list_set & second_list_set):
    print(first_list_set & second_list_set)
  else:
    print("Не має спільних елементів")


def find_missing(first_list, second_list, string_first_list, string_second_list):
    for num in range(string_first_list):
        for num_1 in range(string_second_list):
            if (first_list[num] == second_list[num_1]):
                break

        if (num_1 == string_second_list - 1):
            print(first_list[num], end = " ")


def unique_in_list(first_list, second_list):
    res = list(set(first_list + second_list))
    print(f"\n{res}")



first_list = [20, 35, 6, 7, 7, 8, 10]
second_list = [45, 20, 7, 10, 100]
string_first_list = len(first_list)
string_second_list = len(second_list)
identical_numbers(first_list, second_list)
find_missing(first_list, second_list, string_first_list, string_second_list)
unique_in_list(first_list, second_list)
