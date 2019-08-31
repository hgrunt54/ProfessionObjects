import tkinter as tk
from tkinter import ttk
import db2
import mod_ProfessionObjects as pos

class ProfessionObjectFrame(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="10 10 10 10")
        self.pack(fill=tk.BOTH, expand=True)
        self.Profession = db2.getProfession()
        self.gameMode = db2.getGameMode()

        #Define string variable for the entry field
        self.buildName = tk.StringVar()
        self.professionCombo = ttk.Combobox(self, state='readonly', values=self.Profession)
        self.gameModeCombo = ttk.Combobox(self, state="readonly", values=self.gameMode)

        #Create a label, an entry field, and a button
        ttk.Label(self, text="Build Name:").grid(column=0, row=0, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.buildName).grid(column=1, row=0)
        ttk.Label(self, text="Profession:").grid(column=2, row=0)
        self.professionCombo.grid(column=3, row=0)
        ttk.Label(self, text="Game Mode:").grid(column=4, row=0)
        self.gameModeCombo.grid(column=5, row=0)
        ttk.Button(self, text="Save", command=self.save).grid(column=6, row=0)

        #Add padding to all child components
        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=3)

    #Define the callback method for the save button
    def save(self): #Saves the variables and inserts the data into the necessary database tables.
        self.professionCombo.current()
        self.gameModeCombo.current()
        self.BuildNameChoice = self.buildName.get()
        self.ProfessionChoice = self.professionCombo.get()
        self.GameModeChoice = self.gameModeCombo.get()
        db2.addBuildName(self.BuildNameChoice)
        db2.addProfessionObject(self.ProfessionChoice, self.GameModeChoice)
        print(self.BuildNameChoice + ": This Object was added to the ProfessionObjects table!")


if __name__== "__main__":
    root = tk.Tk()
    root.title("Profession Object")
    ProfessionObjectFrame(root)
    root.mainloop()