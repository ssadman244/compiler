class Stack:
    def __init__(self):
        self.a = []

    def isEmpty(self):
        return self.a == []

    def push(self, i):
        self.a.append(i)

    def pop(self):
        return self.a.pop()

    def peek(self):
        return self.a[len(self.a)-1]

prec = {
    '/': 3,
    '*': 3,
    '+': 2,
    '-': 2,
    '^': 4,
    '(': 1
}

def infixToPrefix(s):
    opStack = Stack()    
    prefixList = []
    temp = []
    for token in s:
        if token in "abcdefghijklmnopqrstuvwxyz" or token in "0123456789":
            prefixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                temp.append(topToken)
                topToken = opStack.pop()
            prefixList = temp + prefixList
            temp = []
        else:
            while (not opStack.isEmpty()) and \
                  (prec[opStack.peek()] >= prec[token]):
                temp.append(opStack.pop())
            prefixList = temp + prefixList
            temp = []
            opStack.push(token)
    while not opStack.isEmpty():
        temp.append(opStack.pop())
    prefixList = temp + prefixList
    return ''.join(prefixList)


def infixToPostfix(s):
    opStack = Stack()
    postfixList = []
    temp = []
    for token in s:
        if token in "abcdefghijklmnopqrstuvwxyz" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                temp.append(topToken)
                topToken = opStack.pop()
            postfixList = postfixList + temp
            temp = []
        else:
            while (not opStack.isEmpty()) and \
                  (prec[opStack.peek()] >= prec[token]):
                temp.append(opStack.pop())
            postfixList = postfixList + temp
            temp = []
            opStack.push(token)
    while not opStack.isEmpty():
        temp.append(opStack.pop())
    postfixList = postfixList + temp
    return ''.join(postfixList)


def file_op():
    file_input = open('file.txt', 'r')
    file_str = file_input.read().split(" ")

    file_conv_type = int(
        input("Enter convert type :\n1. Infix to Prefix\n2. Infix to Postfix\n> "))

    if file_conv_type == 1:
        file_result = infixToPrefix(file_str[0])

    elif file_conv_type == 2:
        file_result = infixToPostfix(file_str[0])

    return file_result

# *************************main**************************

while True:
    value_temp = ""
    print("Input type :")
    choice = int(input("1. Console Input\n2. File Input\n3. Exit\n> "))

    if choice == 1:
        console_input = input("Type the infix expression :\n> ").lower()
        value_temp += console_input

    elif choice == 2:
        f_res = file_op()
        # print(f_res)
        f2 = open('file.txt', 'w')
        f2.write(f_res)
        break

    elif choice == 3:
        break

    else:
        print('Wrong input!')

    conv_type = int(
        input("Enter convert type :\n1. Infix to Prefix\n2. Infix to Postfix\n> "))

    if conv_type == 1:
        infix_result = infixToPrefix(value_temp)
        print(infix_result)
        break
    elif conv_type == 2:
        postfix_result = infixToPostfix(value_temp)
        print(postfix_result)
        break

    else:
        print('Wrong input!\n')
