class Elements:
    def __init__(self, vertiba):
        self.vertiba = vertiba
        self.nakamais = None
class LinkedList:
    def __init__(self):
        self.sakums = None
if __name__ == '__main__':
    linked_list = LinkedList()
    code = input()  
    sakuma_iekavas = ["(", "[", "{"]
    beigu_iekavas = [")", "]", "}"]
    stack = []
    for i, char in enumerate(code, start=1):
        if char in sakuma_iekavas:
            stack.append((char, i))
        elif char in beigu_iekavas:
            if not stack:
                print(i)
                break
            top = stack.pop()
            if (top[0] == "(" and char != ")") or \
                    (top[0] == "[" and char != "]") or \
                    (top[0] == "{" and char != "}"):
                print(i)
                break
    else:

      
        if stack:
            print(stack[0][1])
          
        else:
            print("Success")
