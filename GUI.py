from tkinter import *
import random


class Application(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()

        file = open("words.txt", "r")
        self.wordlist = []
        for x in file:
            x = x.strip()
            self.wordlist.append(x)

        number = random.randint(1, len(self.wordlist))
        self.word = self.wordlist[number]
        self.wordlength = len(self.word)

        self.create_widgets()

    def create_widgets(self):
        picture = "Capture.PNG"
        imageLarge = PhotoImage(file=r"C:\Users\alvin\Pictures\Hangman\\" + picture)
        w = Label(self, image=imageLarge)
        w.photo = imageLarge
        w.grid(row=0, column=0)
        print(self.word)
        x = 0
        for char in self.word:
            Label(self, text="_", width=3, font=("Impact", 30)).grid(row=0, column=x + 1)
            x += 1
        self.letterEntry = Entry(self)
        self.letterEntry.grid(row=1, column=0, sticky=W)
        confirmButton = Button(self, command=self.letterInput, text="Confirm")
        confirmButton.grid(row=1, column=0, sticky=E)

    def letterInput(self):
        dict = {}
        correct = []
        for x in range(len(self.word)):
            dict[x] = self.word[x]
        input = self.letterEntry.get()
        print(dict)
        for x in range(len(dict)):
            if input == dict[x]:
                correct.append(x)
        print

root = Tk()
root.title("Hangman")
app = Application(root)
root.mainloop()