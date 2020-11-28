class node:
    def __init__(self):
        self.value = ""
        self.next = None

class linked_list:
    def __init__(self):
        self.headval = node()
        self.headval.value = 'ROOT'

    def add(self, input_value):  
        curr_node = self.headval
        while curr_node.next != None:
            curr_node = curr_node.next 
        curr_node.next = node()
        curr_node.next.value = input_value

    def has(self, input_value):
        ret_val = False
        curr_node = self.headval
        while curr_node is not None:
            if curr_node.value == input_value:
                ret_val = True
                break
            else:
                curr_node = curr_node.next
        return ret_val

    def list_print(self):
        curr_node = self.headval
        while curr_node is not None:
            print(curr_node.value)
            curr_node = curr_node.next
        