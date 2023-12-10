class TextEditor:
    def __init__(self):
        self.text = ""
        self.operations = []

    def append(self, string):
        self.operations.append(self.text)
        self.text += string

    def delete(self, k):
        self.operations.append(self.text)
        self.text = self.text[:-k]

    def print_char(self, k):
        print(self.text[k - 1])

    def undo(self):
        if self.operations:
            self.text = self.operations.pop()

if __name__ == "__main__":
    text_editor = TextEditor()

    Q = int(input().strip())
    for _ in range(Q):
        operation = input().strip().split()
        op = int(operation[0])

        if op == 1:
            text_editor.append(operation[1])
        elif op == 2:
            text_editor.delete(int(operation[1]))
        elif op == 3:
            text_editor.print_char(int(operation[1]))
        elif op == 4:
            text_editor.undo()
