def loading_bar(num):

    number_of_loadings = num // 10
    lst_of_loadings = number_of_loadings * '%'
    lst_of_dots = (10 - len(lst_of_loadings)) * '.'
    if len(lst_of_loadings) < 10:
        return f"{num}% [{lst_of_loadings}{lst_of_dots}]\n" \
               f"Still loading..."
    else:
        return f"100% Complete!\n"\
               f'[%%%%%%%%%%]'


number = int(input())
print(loading_bar(number))
