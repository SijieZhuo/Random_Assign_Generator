import os
import tkinter as tk
from tkinter import filedialog
import pandas as pd
import random
import ntpath
import numpy as np


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.student_file_path = tk.StringVar()
        student_label = tk.Label(self, textvariable=self.student_file_path)
        student_label.grid(column=1, pady=3)
        student_path_btn = tk.Button(self, text="Browse student set",
                                     command=lambda: browse_btn_hit(self.student_file_path),
                                     width=25)
        student_path_btn.grid(column=1, pady=3)

        self.colour_file_path = tk.StringVar()
        colour_label = tk.Label(self, textvariable=self.colour_file_path)
        colour_label.grid(column=1, pady=3)
        colour_path_btn = tk.Button(self, text="Browse colour set",
                                    command=lambda: browse_btn_hit(self.colour_file_path), width=25)
        colour_path_btn.grid(column=1, pady=3)

        generate_btn = tk.Button(self, text="Generate", command=lambda: self.generateRandomAssign(), width=25)
        generate_btn.grid(column=1, pady=3)

        self.grid_columnconfigure((0, 2), weight=1)
        self.grid_rowconfigure((0, 5), weight=1)

        self.pack()
        # self.setup_window()

    def generateRandomAssign(self):
        # student_file = pd.read_csv(self.student_file_path.get())
        # colour_file = pd.read_csv(self.colour_file_path.get())
        student_file = pd.read_csv("H:/PhDFiles/PhD/COMPSCI345_SOFTENG350/RanAssignGenerator/Data/345_student.csv")
        colour_file = pd.read_csv("H:/PhDFiles/PhD/COMPSCI345_SOFTENG350/RanAssignGenerator/Data/ral_standard.csv")

        file_name = os.path.basename(self.student_file_path.get())

        student_ids = student_file[student_file['SIS User ID'].notna()]['SIS Login ID']

        colour_code = colour_file[~colour_file[' English'].str.contains('grey|black|white')]['HEX']
        print(colour_code)

        result_data = pd.DataFrame(columns=['Student_ID', 'Colour HEX'])

        for index, student in student_ids.items():
            result_data = result_data.append(
                pd.DataFrame([[student, random.choice(colour_code.tolist())]], columns=result_data.columns))

        print(result_data)

        result_data.to_csv(os.getcwd() + "/Result/Result_.csv" + file_name, index=False)


def browse_btn_hit(folder_path):
    """
    This function used to trigger the browse button event to save the
    file path to the inout parameter
    :param folder_path: the StringVar that stores the file path
    """
    filename = filedialog.askopenfilename()
    folder_path.set(filename)
    print(filename)


def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail
