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
        self.confirmButton = Button(self, command=self.letterInput, text="Confirm")
        self.confirmButton.grid(row=1, column=0, sticky=E)
        self.usedCharacters = []
        self.badLabel = Label(self, font=("Times", 15))
        self.badLabel.grid(row=2, column=0, sticky=N)
        self.rightLabel = Label(self, font=("Times", 20))
        self.rightLabel.grid(row=4, column=0, sticky=N)

    def letterInput(self):
        self.badLabel["text"] = ""
        self.bad = False
        dict = {}
        correct = []
        for x in range(len(self.word)):
            dict[x] = self.word[x]
        input = self.letterEntry.get()
        input = input.lower()
        words = self.checkInput(input)
        self.badLabel["text"] = words
        if self.bad == False:
            for x in range(len(dict)):
                if input == dict[x]:
                    correct.append(x)
            if len(correct) == 0:
                self.w.config(image='')
                self.picturenum += 1
                if self.picturenum > 7:
                    self.picturenum = 7
                self.picturenum = str(self.picturenum)
                picture = "Capture" + self.picturenum + ".PNG"
                imageLarge = PhotoImage(file=r"C:\Users\alvin\Pictures\Hangman\\" + picture)
                self.w = Label(self, image=imageLarge)
                self.w.photo = imageLarge
                self.w.grid(row=0, column=0)
                self.picturenum = int(self.picturenum)
                if self.picturenum == 7:
                    self.wonlost = Label(self, text="You Lost!", font=("Impact", 30))
                    self.wonlost.grid(row=2, column=0, sticky=N)
                    self.letterEntry.destroy()
                    self.confirmButton.destroy()
                    self.retryButton = Button(self, text="Retry", font=("Impact", 20), bg="Light Blue", command=self.retry)
                    self.retryButton.grid(row=3, column=0, sticky=N)
                    self.rightLabel["text"] = "The word was " + self.word
            else:
                for x in correct:
                    self.labelDict[x].config(text=dict[x])
                    self.times += 1
                if self.times == len(self.word):
                    self.wonlost = Label(self, text="You Won!", font=("Impact", 30))
                    self.wonlost.grid(row=2, column=0, sticky=N)
                    self.badLabel.destroy()
                    self.letterEntry.destroy()
                    self.confirmButton.destroy()
                    self.retryButton = Button(self, text="Retry", font=("Impact", 20), bg="Light Blue", command=self.retry)
                    self.retryButton.grid(row=3, column=0, sticky=N)
            self.usedCharacters.append(input)
        elif self.bad == True:
            pass

    def checkInput(self, input):
        validList = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        if len(input) > 1:
            self.bad = True
            return "Please only enter one character"
        elif input not in validList:
            self.bad = True
            return "Invalid character"
        elif input in self.usedCharacters:
            self.bad = True
            return "You already used that character"

    def retry(self):
        self.rightLabel.destroy()
        self.picturenum = int(1)
        self.times = 0
        number = random.randint(1, len(self.wordlist))
        self.word = self.wordlist[number]
        self.wordlength = len(self.word)
        print(self.word)
        self.wonlost.destroy()
        self.retryButton.destroy()
        self.w.destroy()
        picture = "Capture.PNG"
        imageLarge = PhotoImage(file=r"C:\Users\alvin\Pictures\Hangman\\" + picture)
        self.w = Label(self, image=imageLarge)
        self.w.photo = imageLarge
        self.w.grid(row=0, column=0)
        for x in self.labelDict.values():
            x.destroy()
        self.labelDict.clear()
        x = 0
        for char in self.word:
            self.labelDict[x] = Label(self, text="_", width=3, font=("Impact", 30))
            self.labelDict[x].grid(row=0, column=x + 1)
            x += 1
        self.letterEntry = Entry(self)
        self.letterEntry.grid(row=1, column=0, sticky=W)
        self.confirmButton = Button(self, command=self.letterInput, text="Confirm")
        self.confirmButton.grid(row=1, column=0, sticky=E)
        self.usedCharacters = []
        self.badLabel = Label(self, font=("Times", 15))
        self.badLabel.grid(row=2, column=0, sticky=N)


root = Tk()
root.title("Hangman")
app = Application(root)
root.mainloop()