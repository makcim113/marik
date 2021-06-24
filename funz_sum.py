def sum_int(str_int):
    st = list(str_int)
    new_str = [int(i) for i in st]
    new_sum = sum(new_str)
    print(new_sum)
