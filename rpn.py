
class RPNParser(object):
    OPERATORS = ["+", "-", "*", "/"]

    class Stack(list):
        def push(self, obj):
            self.append(obj)

    def __init__(self):
        self.queue = []
        self.stack = self.Stack()

    def validate(self, rpn_string):
        rpn_list = rpn_string.split(" ")
        op_count = 0
        for op in self.OPERATORS:
            op_count += rpn_list.count(op)
        print op_count
        print len(rpn_list)
        var_count = op_count - len(rpn_list)
        print var_count
        if var_count > 0:
            return True
        else:
            return False


    def clear_queue(self):
        del self.queue[:]

    def read(self, rpn_string):
        rpn_string += " "
        data = ""
        for char in rpn_string:
            if char != " ":
                data += char
            else:
                self.queue.append(data)
                data = ""

    def process(self):
        temp_stack = self.Stack()
        for payload in self.queue:
            if payload not in self.OPERATORS:
                temp_stack.push(payload)
            else:
                values = (temp_stack.pop(), temp_stack.pop())
                expression = values[1] + payload + values[0]
                value = eval(expression)
                temp_stack.push(str(value))
        return temp_stack[0]


if __name__ == "__main__":
    r = RPNParser()
    r.read("4 4 + 3 *")
    print r.process()
    r.clear_queue()
    r.read("6 20 * 3 +")
