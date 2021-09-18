class Stack:
    def __init__(self):
        self.stack = [0]

    def isempty(self):
        """
        Return True if stack is empty
        Return False if stack isn't empty
        """
        if self.stack[0] == 0:
            return True
        else:
            return False

    def push(self, item):
        """
        Add an item into a stack
        """
        if len(self.stack) > self.stack[0]+1:
            self.stack[self.stack[0]:self.stack[0]+2] = self.stack[self.stack[0]], item
            self.stack[0] += 1
        else:
            self.stack[self.stack[0]:self.stack[0] + 1] = self.stack[self.stack[0]], item
            self.stack[0] += 1

    def pop(self):
        """
        Pop the top item from the stack if it is possible
        """
        if self.stack[0] > 0:
            self.stack[0] -= 1

    def top(self):
        """
        Return the top item of stack or '0' if there are no elements
        """
        if self.stack[0] > 0:
            return self.stack[self.stack[0]]
        else:
            return 0


def convert_to_rpn(expr):
    """
    Return an expression converted to reverse polish notation
    """
    expr += ' '
    reading_num = False
    num = ''
    rpn = []
    st = Stack()
    for i in range(len(expr)):
        if expr[i] == ' ':
            continue
        if expr[i] == '(':
            st.push(expr[i])
            continue
        if expr[i] in '+-/*':
            while not st.isempty() and st.top() != '(':
                if expr[i] == '*' or expr[i] == '/':
                    if st.top() == '*' or st.top() == '/':
                        rpn.append(st.top())
                        st.pop()
                    else:
                        break
                else:
                    rpn.append(st.top())
                    st.pop()
            st.push(expr[i])
            continue
        if expr[i] == ')':
            while st.top() != '(':
                rpn.append(st.top())
                st.pop()
            st.pop()
            continue
        if reading_num:
            num += expr[i]
            if expr[i + 1] not in '0123456789.':
                reading_num = False
                rpn.append(num)
                num = ''
        else:
            if expr[i + 1] in '0123456789.':
                reading_num = True
                num += expr[i]
            else:
                if num == '':
                    rpn.append(expr[i])
                else:
                    rpn.append(num)
                    num = ''
    while not st.isempty():
        rpn.append(st.top())
        st.pop()
    return rpn


def evaluate_rpn_expression(rpn):
    """
    Return the result of evaluating a RPN expression
    """
    st = Stack()
    for i in rpn:
        if i in '+-*/':
            b = st.top()
            st.pop()
            a = st.top()
            st.pop()
            if i == '+':
                a += b
            if i == '-':
                a -= b
            if i == '*':
                a *= b
            if i == '/':
                if b != 0:
                    a /= b
                else:
                    return 'inf'
            st.push(a)
        else:
            st.push(float(i))
    res = st.top()
    # convert to int if fractional part is equal to 0
    if res % 1 == 0:
        res = int(res)
    return res


def evaluate_expression(expr):
    """
    Return the result of evaluating an expression
    """
    rpn = convert_to_rpn(expr)
    result = evaluate_rpn_expression(rpn)
    return str(result)


def main():
    calc_in = input('Enter an expression using numbers and "+ - * / ( )": ')
    answ = evaluate_expression(calc_in)
    if answ == 'inf':
        print('An attempt to divide by 0 was made.')
    print(calc_in.replace(' ', '') + ' = ' + answ)


if __name__ == '__main__':
    main()
