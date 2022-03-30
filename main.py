# Необходимо реализовать класс Stack со следующими методами:«последним пришёл — первым вышел»

# Используя стек из задания 1 необходимо решить задачу на проверку сбалансированности скобок.
# Сбалансированность скобок означает, что каждый открывающий символ имеет соответствующий ему закрывающий, и пары скобок правильно вложены друг в друга.

class Stack:
    def __init__(self, list_of_stek):
        self.list_of_stek = list_of_stek

# isEmpty - проверка стека на пустоту. Метод возвращает True или False.
    def isEmpty(self):
        aaa = None
        if len(self.list_of_stek) == 0:
            aaa = True
        else:
            aaa = False
        return aaa
#push - добавляет новый элемент на вершину стека. Метод ничего не возвращает.
    def push(self):
        new_element = input('ведите новый элемент')
        self.list_of_stek.append(new_element)

# pop - удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека
    def pop(self):
       resul = self.list_of_stek[-1]
       del self.list_of_stek[-1]
       #print(self.list_of_stek)
       return resul


# peek - возвращает верхний элемент стека, но не удаляет его. Стек не меняется.
    def peek(self):
        return self.list_of_stek[-1]


# size - возвращает количество элементов в стеке.
    def size (self):
        return len(self.list_of_stek)

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
    print(new_stack.pop())
    print(new_stack.peek())
    print(new_stack.size())


