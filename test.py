import re


def f_re(i: str) -> str:
    s = i.strip()
    num_list = [str(int(num)) for num in filter(
        lambda num: num.isnumeric(), s)]
    if num_list:
        return ''.join(num_list)