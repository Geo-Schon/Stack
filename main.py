from valiator import is_valid

balanced1 = '(((([{}]))))'
balanced2 = '[([])((([[[]]])))]{()}'
balanced3 = '{{[()]}}'
unbalanced1 = '}{}'
unbalanced2 = '{{[(])]}}'
unbalanced3 = '[[{())}]'

if __name__ == '__main__':
    print(is_valid(balanced1))
    print(is_valid(balanced2))
    print(is_valid(balanced3))
    print(is_valid(unbalanced1))
    print(is_valid(unbalanced2))
    print(is_valid(unbalanced3))
