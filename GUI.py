from tkinter import *
import random


class Application(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.picturenum = int(1)
        file = open("words.txt", "r")
        self.wordlist = []
        self.times = 0
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
        self.w = Label(self, image=imageLarge)
        self.w.photo = imageLarge
        self.w.grid(row=0, column=0)
        print(self.word)
        x = 0
        self.labelDict = {}
        for char in self.word:
            self.labelDict[x] = Label(self, text="_", width=3, font=("Impact", 30))
            self.labelDict[x].grid(row=0, column=x + 1)
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
        input = input.lower()
        for x in range(len(dict)):
            if input == dict[x]:
                correct.append(x)
        if len(correct) == 0:
            self.w.config(image='')
            self.picturenum += 1
            self.picturenum = str(self.picturenum)
            picture = "Capture" + self.picturenum + ".PNG"
            imageLarge = PhotoImage(file=r"C:\Users\alvin\Pictures\Hangman\\" + picture)
            self.w = Label(self, image=imageLarge)
            self.w.photo = imageLarge
            self.w.grid(row=0, column=0)
            self.picturenum = int(self.picturenum)
        else:
            for x in correct:
                self.labelDict[x].config(text=dict[x])
                self.times += 1
            if self.times == len(self.word):
                Label(self, text="You Won!", font=("Impact", 30)).grid(row=2, column=0, sticky=N)


root = Tk()
root.title("Hangman")
app = Application(root)
root.mainloop()
