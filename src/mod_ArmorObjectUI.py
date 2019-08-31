#!user/bin/env/python3
# This module creates the UI frame for the Armor Object that will get the builds armor stats and runes
import tkinter as tk
from tkinter import ttk
import armorDB

class PvPArmorObjectFrame(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="10 10 10 10")
        self.pack(fill=tk.BOTH, expand=True)

        # create the drop down lists
        self.buildTypeList = armorDB.getBuildTypes()
        self.insigList = armorDB.getPvPInsignias()
        self.runeList = armorDB.getPvPRunes()


        # defining the drop down variables
        self.buildType = ttk.Combobox(self, state='readonly', values=self.buildTypeList)
        self.insignia = ttk.Combobox(self, state='readonly', values=self.insigList)
        self.rune = ttk.Combobox(self, state='readonly', values=self.runeList)

        # creating the labels and drop downs in the frame
        ttk.Label(self, text="Build Type:").grid(column=0, row=0, sticky=tk.E)
        self.buildType.grid(column=1, row=0)
        ttk.Label(self, text="Insignia:").grid(column=1, row=1)
        ttk.Label(self, text="     ").grid(column=2, row=1)
        ttk.Label(self, text="Rune:").grid(column=3, row=1)
        self.insignia.grid(column=1, row=2)
        ttk.Label(self, text="     ").grid(column=2, row=2)
        self.rune.grid(column=3, row=2)

        # Add padding to all child components
        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=3)

class PvEArmorObjectFrame(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="10 10 10 10")
        self.pack(fill=tk.BOTH, expand=True)

        # create the drop down lists
        self.buildTypeList = armorDB.getBuildTypes()
        self.insigList = armorDB.getPvEInsignias()
        self.runeList = armorDB.getPvERunes()

        # defining the drop down variables
        self.buildType = ttk.Combobox(self, state='readonly', values=self.buildTypeList)
        self.headIns = ttk.Combobox(self, state='readonly', values=self.insigList)
        self.headRune = ttk.Combobox(self, state='readonly', values=self.runeList)
        self.shoulderIns = ttk.Combobox(self, state='readonly', values=self.insigList)
        self.shoulderRune = ttk.Combobox(self, state='readonly', values=self.runeList)
        self.chestIns = ttk.Combobox(self, state='readonly', values=self.insigList)
        self.chestRune = ttk.Combobox(self, state='readonly', values=self.runeList)
        self.glovesIns = ttk.Combobox(self, state='readonly', values=self.insigList)
        self.glovesRune = ttk.Combobox(self, state='readonly', values=self.runeList)
        self.pantsIns = ttk.Combobox(self, state='readonly', values=self.insigList)
        self.pantsRune = ttk.Combobox(self, state='readonly', values=self.runeList)
        self.bootsIns = ttk.Combobox(self, state='readonly', values=self.insigList)
        self.bootsRune = ttk.Combobox(self, state='readonly', values=self.runeList)

        # create labels and dropdowns in the frame
        ttk.Label(self, text="Build Type:").grid(column=0, row=0, sticky=tk.E)
        self.buildType.grid(column=1, row=0)
        ttk.Label(self, text="Inscription:").grid(column=1, row=1)
        ttk.Label(self, text="     ").grid(column=2, row=1)
        ttk.Label(self, text="Rune:").grid(column=3, row=1)
        ttk.Label(self, text="Head:").grid(column=0, row=2)
        self.headIns.grid(column=1, row=2)
        ttk.Label(self, text="     ").grid(column=2, row=2)
        self.headRune.grid(column=3, row=2)
        ttk.Label(self, text="").grid(column=0, row=3)
        ttk.Label(self, text="Shoulders:").grid(column=0, row=4)
        self.shoulderIns.grid(column=1, row=4)
        ttk.Label(self, text="     ").grid(column=2, row=4)
        self.shoulderRune.grid(column=3, row=4)
        ttk.Label(self, text="").grid(column=0, row=5)
        ttk.Label(self, text="Chest:").grid(column=0, row=6)
        self.chestIns.grid(column=1, row=6)
        ttk.Label(self, text="     ").grid(column=2, row=6)
        self.chestRune.grid(column=3, row=6)
        ttk.Label(self, text="").grid(column=0, row=7)
        ttk.Label(self, text="Gloves:").grid(column=0, row=8)
        self.glovesIns.grid(column=1, row=8)
        ttk.Label(self, text="     ").grid(column=2, row=8)
        self.glovesRune.grid(column=3, row=8)
        ttk.Label(self, text="").grid(column=0, row=9)
        ttk.Label(self, text="Pants:").grid(column=0, row=10)
        self.pantsIns.grid(column=1, row=10)
        ttk.Label(self, text="     ").grid(column=2, row=10)
        self.pantsRune.grid(column=3, row=10)
        ttk.Label(self, text="").grid(column=0, row=11)
        ttk.Label(self, text="Boots:").grid(column=0, row=12)
        self.bootsIns.grid(column=1, row=12)
        ttk.Label(self, text="     ").grid(column=2, row=12)
        self.bootsRune.grid(column=3, row=12)

        # Add padding to all child components
        #for child in self.winfo_children():
        #    child.grid_configure(padx=5, pady=3)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Armor Object")
    PvEArmorObjectFrame(root)
    root.mainloop()
