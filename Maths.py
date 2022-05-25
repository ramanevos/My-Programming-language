import operator


class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None

    def postorder(self):

        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.data, end=" ")


def is_greater_precedence(op1, op2):
    pre = {'+': 4, '-': 4, '*': 5, '/': 5, '^': 6, '&': 1, '|': 0, '<': 3, '>': 3, '<=': 3, '>=': 3, '==': 2, '!=': 2, '!': 7}
    #pre['('] = 8
    #pre[')'] = 8
    return pre[op1] >= pre[op2]


def associativity(op):
    ass = {'+': 0, '-': 0, '*': 0, '/': 0, '^': 1, '&': 0, '|': 0, '<': 0, '>': 0, '<=': 0, '>=': 0, '==': 0, '!=': 0, '!':0}
    #ass['('] = 0
    #ass[')'] = 0
    return ass[op]


def build_tree(exp):
    exp_list = exp.split()
    # print(exp_list)
    stack = []
    tree_stack = []
    for i in exp_list:
        if i not in ['+', '-', '*', '/', '^', '(', ')', '&', '|', '<', '>', '<=', '>=', '==', '!=', 'f', 't','!']:
            t = Node(float(i))
            tree_stack.append(t)

        elif i in ['t', 'f']:
            if i == "t":
                i = True
            else:
                i = False
            t = Node(i)
            tree_stack.append(t)
        elif i == '(':
            stack.append('(')

        elif i in ['+', '-', '*', '/', '^', '|', '&', '<', '>', '<=', '>=', '==', '!=', '!']:
            if not stack or stack[-1] == '(':
                stack.append(i)

            elif is_greater_precedence(i, stack[-1]) and associativity(i) == 6:
                stack.append(i)

            else:
                while stack and stack[-1] != "(" and is_greater_precedence(stack[-1], i) and associativity(i) == 0:
                    popped_item = stack.pop()
                    t = Node(popped_item)
                    if t.data == "!":
                        t1 = tree_stack.pop()
                        t.left = t1
                    else:
                        t1 = tree_stack.pop()
                        t2 = tree_stack.pop()
                        t.right = t1
                        t.left = t2
                    tree_stack.append(t)
                stack.append(i)



        elif i == ')':
            while stack[-1] != '(':
                popped_item = stack.pop()
                t = Node(popped_item)
                if t.data == "!":
                    t1 = tree_stack.pop()
                    t.left = t1
                else:
                    t1 = tree_stack.pop()
                    t2 = tree_stack.pop()
                    t.right = t1
                    t.left = t2
                tree_stack.append(t)
            stack.pop()
    while stack:
        popped_item = stack.pop()
        t = Node(popped_item)
        if t.data == "!":
            t1 = tree_stack.pop()
            t.left =t1

        else:
            t1 = tree_stack.pop()
            t2 = tree_stack.pop()
            t.right = t1
            t.left = t2
        tree_stack.append(t)

    t = tree_stack.pop()

    return t


def evaluate(expTree):
    opers = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv, '^': operator.pow}
    opers['<'] = operator.lt
    opers['<='] = operator.le
    opers['>'] = operator.gt
    opers['>='] = operator.ge
    opers['=='] = operator.eq
    opers['!='] = operator.ne
    opers['|'] = operator.or_
    opers['&'] = operator.and_
    opers['!'] = operator.not_

    leftC = expTree.left
    rightC = expTree.right

    if leftC and rightC:
        fn = opers[expTree.data]
        return fn(evaluate(leftC), evaluate(rightC))
    elif leftC and expTree.data == "!":
        fn = opers[expTree.data]
        return fn(evaluate(leftC))
    else:
        return expTree.data

def calculatevariable(expression):
    new_expression = ""
    previous = None
    previous2 = None
    previous3 = None
    operators = ['+', '-', '*', '/']
    count = 0

    for char in expression:
        if count == 0:
            if not char.isspace():
                new_expression += char
                previous2 = previous
                previous = char

            else:
                pass
            count += 1
        else:
            if char == "t" or char == "f":
                new_expression += " " + char
                previous3 = previous2
                previous2 = previous
                previous = char

            elif char.isdigit() or char == ".":
                if previous.isdigit() or previous == ".":
                    new_expression += char
                    previous3 = previous2
                    previous2 = previous
                    previous = char


                elif previous == "-":
                    if previous2 == None:
                        new_expression += char
                        previous3 = previous2
                        previous2 = previous
                        previous = char

                    elif previous2 in operators:
                        new_expression += char
                        previous3 = previous2
                        previous2 = previous
                        previous = char
                    elif previous2 == "(" or previous2 == ")":
                        if previous3 in operators or previous3 == None:
                            new_expression += char
                            previous3 = previous2
                            previous2 = previous
                            previous = char
                        else:
                            new_expression += " " + char
                            previous3 = previous2
                            previous2 = previous
                            previous = char
                    else:
                        new_expression += " " + char
                        previous3 = previous2
                        previous2 = previous
                        previous = char


                else:
                    new_expression += " " + char
                    previous3 = previous2
                    previous2 = previous
                    previous = char

            elif char == "=":
                if previous == "=" or previous == "<" or previous == ">" or previous == "!":
                    new_expression += char
                    previous3 = previous2
                    previous2 = previous
                    previous = char
                else:
                    new_expression += " " + char
                    previous3 = previous2
                    previous2 = previous
                    previous = char

            elif char == " ":
                pass
            else:
                new_expression += " " + char
                previous3 = previous2
                previous2 = previous
                previous = char

    t = build_tree(new_expression)

    return str(evaluate(t))

def calculate(expression):
    new_expression = ""
    previous = None
    previous2 = None
    previous3 = None
    operators = ['+', '-', '*', '/']
    count = 0

    for char in expression:
        if count == 0:
            if not char.isspace():
                new_expression += char
                previous2 = previous
                previous = char

            else:
                pass
            count += 1
        else:
            if char == "t" or char == "f":
                new_expression += " " + char
                previous3 = previous2
                previous2 = previous
                previous = char

            elif char.isdigit() or char == ".":
                if previous.isdigit() or previous == ".":
                    new_expression += char
                    previous3 = previous2
                    previous2 = previous
                    previous = char


                elif previous == "-":

                    if previous2 == None:
                        new_expression += char
                        previous3 = previous2
                        previous2 = previous
                        previous = char

                    elif previous2 in operators:
                        new_expression += char
                        previous3 = previous2
                        previous2 = previous
                        previous = char
                    elif previous2 == "(" or previous2 == ")":
                        if previous3 in operators or previous3 == None:
                            new_expression += char
                            previous3 = previous2
                            previous2 = previous
                            previous = char
                        else:
                            new_expression += " " + char
                            previous3 = previous2
                            previous2 = previous
                            previous = char
                    else:
                        new_expression += " " + char
                        previous3 = previous2
                        previous2 = previous
                        previous = char


                else:
                    new_expression += " " + char
                    previous3 = previous2
                    previous2 = previous
                    previous = char

            elif char == "=":
                if previous == "=" or previous == "<" or previous == ">" or previous == "!":
                    new_expression += char
                    previous3 = previous2
                    previous2 = previous
                    previous = char
                else:
                    new_expression += " " + char
                    previous3 = previous2
                    previous2 = previous
                    previous = char

            elif char == " ":
                pass
            else:
                new_expression += " " + char
                previous3 = previous2
                previous2 = previous
                previous = char

    t = build_tree(new_expression)

    #print("The result of " + str(new_expression) + " is: " + str(evaluate(t)))
    print(str(evaluate(t)))
    # t.postorder()



###### STRING MATHS



def calculatestringvariable(expression):
    newexpression = []
    valid = True
    for token in expression:
        if "\\\\n" in token:
            token = token.replace('\\\\n', '\\n')
            newexpression.append(token)
        elif "\\n" in token:
            token = token.replace('\\n','\n')
            newexpression.append(token)
        elif "\\\\" in token:
            newexpression.append(token)
        elif "\\" in token:
            print("ERROR: invalid not printable character")
            valid = False
        else:
            newexpression.append(token)
    if valid:
        t = build_stringtree(newexpression)
        #print("The result of " + str(expression) + " is: " + str(evaluate(t)))
        return str(evaluate(t))

    # print(exp_list)

def calculatestring(expression):
    newexpression = []
    valid = True
    for token in expression:
        if "\\\\n" in token:
            token = token.replace('\\\\n', '\\n')
            newexpression.append(token)
        elif "\\n" in token:
            token = token.replace('\\n','\n')
            newexpression.append(token)
        elif "\\\\" in token:
            newexpression.append(token)
        elif "\\" in token:
            print("Error, invalid not printable character")
            valid = False
        else:
            newexpression.append(token)
    if valid:
        t = build_stringtree(newexpression)
        #print("The result of " + str(expression) + " is: " + str(evaluate(t)))
        print(str(evaluate(t)))

    # print(exp_list)
def build_stringtree(expression):
    stack = []
    tree_stack = []
    exp_list = expression[0:-1]
    for i in exp_list:
        if i == "$p4c£":
            i = ' '
            t = Node(str(i))
            tree_stack.append(t)


        elif i not in ['+', '-', '*', '/', '^', '(', ')', '&', '|', '<', '>', '<=', '>=', '==', '!=', 'f', 't', '!']:
            t = Node(str(i))
            tree_stack.append(t)

        elif i in ['t', 'f']:
            if i == "t":
                i = True
            else:
                i = False
            t = Node(i)
            tree_stack.append(t)
        elif i == '(':
            stack.append('(')

        elif i in ['+', '-', '*', '/', '^', '|', '&', '<', '>', '<=', '>=', '==', '!=', '!']:
            if not stack or stack[-1] == '(':
                stack.append(i)

            elif is_greater_precedence(i, stack[-1]) and associativity(i) == 6:
                stack.append(i)

            else:
                while stack and stack[-1] != "(" and is_greater_precedence(stack[-1], i) and associativity(i) == 0:
                    popped_item = stack.pop()
                    t = Node(popped_item)
                    if t.data == "!":
                        t1 = tree_stack.pop()
                        t.left = t1
                    else:
                        t1 = tree_stack.pop()
                        t2 = tree_stack.pop()
                        t.right = t1
                        t.left = t2
                    tree_stack.append(t)
                stack.append(i)



        elif i == ')':
            while stack[-1] != '(':
                popped_item = stack.pop()
                t = Node(popped_item)
                if t.data == "!":
                    t1 = tree_stack.pop()
                    t.left = t1
                else:
                    t1 = tree_stack.pop()
                    t2 = tree_stack.pop()
                    t.right = t1
                    t.left = t2
                tree_stack.append(t)
            stack.pop()
    while stack:
        popped_item = stack.pop()
        t = Node(popped_item)
        if t.data == "!":
            t1 = tree_stack.pop()
            t.left = t1

        else:
            t1 = tree_stack.pop()
            t2 = tree_stack.pop()
            t.right = t1
            t.left = t2
        tree_stack.append(t)

    t = tree_stack.pop()

    return t
