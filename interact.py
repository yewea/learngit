class Interact(object):
    def __init__(self, a1, a2):
        self.u1 = a1
        self.u2 = a2
        self.messages = []

    def add_information(self, sender, information):
        self.messages.append([sender, information])

    def del_information(self, sender, information):
        self.messages.remove([sender, information])

    def show(self):
        n = 0
        while n != len(self.messages):
            print(self.messages[n][0], ':', self.messages[n][1], '\n')
            n += 1


Try = Interact("user1", "user2")
first = input()
while first != '0':
    Try.add_information(Try.u1, first)
    first = input()
Try.show()
