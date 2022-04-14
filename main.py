
class Stack:
    def __init__(self, list_of_stek):
        self.list_of_stek = list_of_stek

# isEmpty - проверка стека на пустоту. Метод возвращает True или False.
    def isEmpty(self):
        return len(self.list_of_stek) == 0

# push - добавляет новый элемент на вершину стека. Метод ничего не возвращает.
    def push(self):
        # new_element = input('ведите новый элемент')
        # self.list_of_stek.insert(0, new_element)
        self.list_of_stek.insert(0, new_element)

# pop - удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека
    def pop(self):
       return self.list_of_stek.pop(0)


# peek - возвращает верхний элемент стека, но не удаляет его. Стек не меняется.
    def peek(self):
        return self.list_of_stek[0]


# size - возвращает количество элементов в стеке.
    def size(self):
        return len(self.list_of_stek)


    def checing_brackets(self):
        st_brackets = []
        for i in self.list_of_stek:
            if i == '(' or i == '{' or i == '[':
                st_brackets.append(i)
                continue
            if (i == ')' or i == '}' or i == ']') and st_brackets:
                if (st_brackets[-1] + i == '()') or (st_brackets[-1] + i == '{}') \
                        or (st_brackets[-1] + i == '[]'):
                    st_brackets.pop()
                else:
                    return 'no'

            else:
                return 'no'

        if st_brackets == []:
            return 'Yes'
        else:
            return 'no'





if __name__ == '__main__':
    start_string = input("Ввидите начальную строку")
    list_for_test = start_string.split()
    new_stack = Stack(list_for_test)
    if new_stack.isEmpty():
        print("список пуст")
        quantity = int(input("введите количествоэлеметов"))
        for element in range(quantity):
            #new_stack.push()
            new_element = input('ведите новый элемент')
            new_stack.push(new_element)
    else:
        print("список имеет значения")

    print(list_for_test)
    print(new_stack.checing_brackets())
    print(new_stack.pop())
    print(new_stack.peek())
    print(new_stack.size())


