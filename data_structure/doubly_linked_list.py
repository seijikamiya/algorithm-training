from ast import Num


class Doubly_linked_list:
    def __init__(self):
        self.list = []

    def inssert(self, x):
        self.list.insert(0, x)

    def delete(self, x):
        self.list.remove(x)

    def deleteFirst(self):
        self.list.popleft()

    def deleteLast(self):
        self.list.pop()


if __name__ == "__main__":
    Linked_list = Doubly_linked_list()
    for _ in range(int(input())):
        input_cmd = input()

        if input_cmd == "deleteFirst":
            Linked_list.deleteFirst()

        elif input_cmd == "deleteLast":
            Linked_list.deleteLast()

        else:
            cmd, num = input_cmd.split()
        
            if cmd == "insert":
                Linked_list.inssert(int(num))
            elif cmd == "delete":
                try:
                    Linked_list.delete(int(num))
                except:
                    pass


    print(*Linked_list.list)