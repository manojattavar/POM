
class email:
    def checkEmail(self):
        file = "C:\\Users\\029693744\\PycharmProjects\\microFocus\\email.txt"
        with open(file) as text:
            txt = text.read()
            print(txt)


email().checkEmail()