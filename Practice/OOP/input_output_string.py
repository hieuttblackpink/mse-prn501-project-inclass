class InputOutputString:
    string: str

    def __init__(self) -> None:
        pass

    def getString(self):
        self.string = input("Input string: ")

    def printString(self):
        print("Your string: " + self.string.upper())