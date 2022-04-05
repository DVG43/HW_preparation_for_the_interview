# #
# Действительно стек должен принимать на вход строку, а внутри преобразовываться к списку
# Плохо называть переменную таким именем aaa = None в методе isEmpty и тем более она не используется. Вы можете просто написать len(self.list_of_stek) == 0
# push - должен принимать на вход значение и добавлять его в стек сверху
# pop - можно у списка просто вызвать pop(). del не нужен
# проверка на сбалансированность работает правильно, только для внутри checing_brackets нужно использовать которые есть у стека. То есть вместо st_brackets.append(self.list_of_stek[i]) использовать push. Вместо st_brackets[-1] использовать peek
# Никогда в python не итерируйтесь так for i in range(len(self.list_of_stek)). нужно ходить по самим объектам, а не по индексам.












class Stack:
    def __init__(self, list_of_stek):
        self.list_of_stek = list_of_stek

# isEmpty - проверка стека на пустоту. Метод возвращает True или False.
    def isEmpty(self):
        if len(self.list_of_stek) == 0:
            aaa = True
        else:
            aaa = False
        return aaa
#push - добавляет новый элемент на вершину стека. Метод ничего не возвращает.
    def push(self):
        new_element = input('ведите новый элемент')
        self.list_of_stek.insert(0,new_element)

# pop - удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека
    def pop(self):
       return self.list_of_stek.pop(0)


# peek - возвращает верхний элемент стека, но не удаляет его. Стек не меняется.
    def peek(self):
        return self.list_of_stek[0]


# size - возвращает количество элементов в стеке.
    def size (self):
        return len(self.list_of_stek)

    # Для стека из задания 1 проверка сбалансированности скобок.
    def checing_brackets (self):
        #s=list(input())
        st_brackets=[]
        for i in range(new_stack.size()):
            if self.list_of_stek[i]=='(' or self.list_of_stek[i]=='{' or self.list_of_stek[i]=='[':
                st_brackets.append(self.list_of_stek[i])
                continue
            if (self.list_of_stek[i]==')' or self.list_of_stek[i]=='}' or self.list_of_stek[i]==']') and st_brackets:
                if (st_brackets[-1]+self.list_of_stek[i]=='()') or (st_brackets[-1]+self.list_of_stek[i]=='{}') \
                        or (st_brackets[-1]+self.list_of_stek[i]=='[]'):
                    st_brackets.pop()
                else:
                    return 'no'
                    #exit()
            else:
                return 'no'
                #exit()
        if st_brackets==[]:
            return 'Yes'
        else:
            return 'no'





list_for_test = []

if __name__ == '__main__':


    new_stack = Stack(list_for_test)
    if new_stack.isEmpty() == True:
        print("список пуст")
    else:
        print("список имеет значения")
    quantity = int(input("введите количествоэлеметов"))
    for element in range(quantity):
        new_stack.push()
    print (list_for_test)
    print(new_stack.pop())
    print(new_stack.peek())
    print(new_stack.size())
    print(new_stack.checing_brackets())

