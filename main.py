import os
import tkinter as tk
from tkinter import font as tkfont

import StartPage


class RandomAssignGenerator(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        if not os.path.exists("Result"):
            os.makedirs("Result")

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.winfo_toplevel().title("Random Assign Generator")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # self.current_data = PhoneData()
        # self.current_data.data = []

        self.frames = {}
        # for F in (StartPage.StartPage):
        # page_name = F.__name__
        # frame = StartPage.StartPage(parent=container, controller=self)
        self.frames[StartPage.StartPage.__name__] = StartPage.StartPage(parent=container, controller=self)

        # put all of the pages in the same location;
        # the one on the top of the stacking order
        # will be the one that is visible.
        # frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main = RandomAssignGenerator()
    main.wm_geometry("550x400")
    main.title("Random Assign Generator")
    main.mainloop()
