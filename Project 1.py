#!/usr/bin/python3.8

"""This program will allow you to see what a dog has to say."""


from random import randint
from tkinter import Label, Text, Tk, Button, Entry
from time import sleep


class Dog:
    """Defines Dog."""

    def __init__(
                self,
                size="medium",
                name="no name",
                fur_color="blank",
                fur_length="short",
                eye_color="colorless",
                age=0
                ):
        """Initialize dog."""
        self.size = size  # large, medium, small
        self.name = name
        self.fur_color = fur_color
        self.fur_length = fur_length
        self.eye_color = eye_color
        self.age = age  # Dog years

    def talk(self):
        """Dog will say something."""
        decision = randint(0, 1)
        if self.size == "small":
            if decision == 0:
                return "pow"
            return "wow"
        elif self.size == "medium":
            if decision == 0:
                return "howl"
            return "uwu"
        elif self.size == "large":
            if decision == 0:
                return "woof"
            return "boof"

    def called(self):
        """Return name of dog."""
        return self.name


class initial_IO:
    """Create IO."""

    def __init__(self, master):
        """Initialize IO."""
        self.master = master
        self.master.title("Talk to dogs")

        self.name_Box = Entry(master)
        self.name_Box.grid(column=2, row=4)

        self.name_Label = Label(text="Name:")
        self.name_Label.grid(column=1, row=4)

        self.outputdog = Label(master, text="")

        self.top_Text = Label(master, text="Please select a dog size:")
        self.top_Text.grid(column=2, row=1)

        self.lg_Button = Button(master, text="Large",
                                command=lambda *args: dogtalk(
                                                            self, size="large"
                                                            ))
        self.lg_Button.grid(column=1, row=2)

        self.md_Button = Button(master, text="Medium",
                                command=lambda *args: dogtalk(
                                                            self, size="medium"
                                                            ))
        self.md_Button.grid(column=2, row=2)

        self.sm_Button = Button(master, text="Small",
                                command=lambda *args: dogtalk(
                                                            self, size="small"
                                                            ))
        self.sm_Button.grid(column=3, row=2)

        self.responce = Label(master)
        self.responce.grid(column=2, row=5)

        self.goodbye = Label(text="Dog says goodbye")
        self.quit = Button(master, text="Quit",
                           command=self.quitfun).grid(column=10, row=10)

        def dogtalk(self, size):
            self.outputdog.config(text=make_Dog(size, self.name_Box.get()))
            self.outputdog.grid(column=2, row=6)

    def quitfun(self):
        """Quit program."""
        self.outputdog.destroy()
        self.goodbye.grid(column=2, row=6)
        self.master.after(2000, lambda: self.master.destroy())


def make_Dog(size, name):
    """Create dog entity."""
    new_dog = Dog(size=size, name=str(name))
    if new_dog.called() == "":
        return f"The {size} dog says {new_dog.talk()}."
    return f"{new_dog.called()}, the {size} dog says {new_dog.talk()}."


def main():
    """Initialize program."""
    root = Tk()
    _ = initial_IO(root)
    root.mainloop()


if __name__ == "__main__":
    main()
