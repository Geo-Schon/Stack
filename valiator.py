from stack_class import Stack


def is_valid(lines):
    open_list = ['(', '{', '[']
    close_list = [')', '}', ']']
    paar = Stack()

    if len(lines) % 2 > 0:
        return 'Несбалансированно'

    for i, char in enumerate(lines):
        if char in open_list:
            paar.push(char)
        elif char in close_list:
            if paar.is_empty():
                return 'Несбалансированно'
            elif open_list.index(paar.peek()) != close_list.index(char):
                return 'Несбалансированно'
            else:
                paar.pop()
                if paar.is_empty() and i == len(lines) - 1:
                    return 'Сбалансированно'


if __name__ == '__main__':
    print(is_valid(input('Введите строку')))
