#!user/bin/env/python3
# This module creates the UI frame for the Armor Object that will get the builds armor stats and runes
import tkinter as tk
from tkinter import ttk
import armorDB
import random

gameMode = random.randint(0, 1)

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
        ttk.Label(self, text="Rune:").grid(column=2, row=1)
        self.insignia.grid(column=1, row=2)
        self.rune.grid(column=2, row=2)
        ttk.Button(self, text="Save", command=self.save).grid(column=2, row=3)

        # Add padding to all child components
        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=3)

    def save(self):
        self.buildType.current()
        self.insignia.current()
        self.rune.current()
        self.bType = self.buildType.get()
        self.insig = self.insignia.get()
        self.r = self.rune.get()
        armorDB.addPvPArmorObject(self.bType, self.insig, self.r)
        print("The PvPArmorObject was added to the tbl_PvPArmor Table!")

        #print("Build Type: " + self.bType)
        #print("Insignia: " + self.insig)
        #print("Rune: " + self.r)

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
        # BuildType Dropdown:
        self.buildType.grid(column=1, row=0)

        #Labels:
        ttk.Label(self, text="Build Type:").grid(column=0, row=0, sticky=tk.E)
        ttk.Label(self, text="Inscription:").grid(column=1, row=1)
        ttk.Label(self, text="Rune:").grid(column=3, row=1)
        ttk.Label(self, text="Head:").grid(column=0, row=2)
        ttk.Label(self, text="Shoulders:").grid(column=0, row=3)
        ttk.Label(self, text="Chest:").grid(column=0, row=4)
        ttk.Label(self, text="Gloves:").grid(column=0, row=5)
        ttk.Label(self, text="Pants:").grid(column=0, row=6)
        ttk.Label(self, text="Boots:").grid(column=0, row=7)

        # Inscription dropdowns
        self.headIns.grid(column=1, row=2)
        self.shoulderIns.grid(column=1, row=3)
        self.chestIns.grid(column=1, row=4)
        self.glovesIns.grid(column=1, row=5)
        self.pantsIns.grid(column=1, row=6)
        self.bootsIns.grid(column=1, row=7)

        # Rune dropdowns:
        self.headRune.grid(column=3, row=2)
        self.shoulderRune.grid(column=3, row=3)
        self.chestRune.grid(column=3, row=4)
        self.glovesRune.grid(column=3, row=5)
        self.pantsRune.grid(column=3, row=6)
        self.bootsRune.grid(column=3, row=7)

        # Creating a test button
        ttk.Button(self, text="Save", command=self.save).grid(column=3, row=8)

        # Add padding to all child components
        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=3)

    # Button's function to test if it saves the data to the database.
    def save(self):
        # Code to get the current drop down for the Build Type
        self.buildType.current()
        self.bType = self.buildType.get()

        # Code to get the current drop down options for Inscriptions
        self.headIns.current()
        self.hI = self.headIns.get()
        self.shoulderIns.current()
        self.shI = self.shoulderIns.get()
        self.chestIns.current()
        self.chI = self.chestIns.get()
        self.glovesIns.current()
        self.glI = self.glovesIns.get()
        self.glovesIns.current()
        self.paI = self.pantsIns.get()
        self.bootsIns.current()
        self.boI = self.bootsIns.get()

        # Code to get the current drop downs for Runes
        self.headRune.current()
        self.hR = self.headRune.get()
        self.shoulderRune.current()
        self.shR = self.shoulderRune.get()
        self.chestRune.current()
        self.chR = self.chestRune.get()
        self.glovesRune.current()
        self.glR = self.glovesRune.get()
        self.glovesRune.current()
        self.paR = self.pantsRune.get()
        self.bootsRune.current()
        self.boR = self.bootsRune.get()

        armorDB.addPvEArmorObject(self.bType, self.hI, self.shI, self.chI, self.glI, self.paI, self.boI,
                                  self.hR, self.shR, self.chR, self.glR, self.paR, self.boR)
        print("The PvEArmorObject was added to the tbl_PvEArmorObjects Table!")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Armor Object")
    if gameMode == 0:
        PvPArmorObjectFrame(root)
    else:
        PvEArmorObjectFrame(root)
    root.mainloop()
