from alpha import AlphaClass

class MyMainClass:
    def PrintFirstLine(self):
        message_string_first = "This is the first message!"
        print(message_string_first)

# Main class Instance
MyMainClassInstance = MyMainClass()
MyMainClassInstance.PrintFirstLine()

# Alpha class instance
AlphaClassInstance = AlphaClass()
AlphaClassInstance.AlphaPrintLine()
