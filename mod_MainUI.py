#! /user/bin/env Python 3.7
import tkinter as tk
from tkinter import ttk
import db2
import armorDB
import weaponsDB
# import mod_ProfessionObjectUI as po
# import mod_ArmorObjectUI as ao
# import mod_WeaponsObjectUI as wo

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.pack(fill=tk.BOTH, expand=True)

        #ProfessionObject code
        self.Profession = db2.getProfession()
        self.gameMode = db2.getGameMode()
        self.buildTypeList = db2.getBuildTypes()

        #Define string variable for the entry field
        self.buildName = tk.StringVar()
        self.professionCombo = ttk.Combobox(self, state='readonly', values=self.Profession)
        self.gameModeCombo = ttk.Combobox(self, state="readonly", values=self.gameMode)
        self.buildType = ttk.Combobox(self, state='readonly', values=self.buildTypeList)

        #Create a label, an entry field, and a button
        ttk.Label(self, text="Build Name:").grid(column=0, row=0, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.buildName).grid(column=1, row=0)
        ttk.Label(self, text="Profession:").grid(column=2, row=0)
        self.professionCombo.grid(column=3, row=0)
        ttk.Label(self, text="Game Mode:").grid(column=4, row=0)
        self.gameModeCombo.grid(column=5, row=0)
        ttk.Label(self, text="Build Type:").grid(column=6, row=0, sticky=tk.E)
        self.buildType.grid(column=7, row=0)
        # ttk.Button(self, text="Save", command=self.save).grid(column=8, row=0)

        # ArmorObject code
        # create the drop down lists
        self.insigList = armorDB.getPvEInsignias()
        self.runeList = armorDB.getPvERunes()

        # defining the drop down variables
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

            # Labels:
        ttk.Label(self, text="Inscription:").grid(column=1, row=1)
        ttk.Label(self, text="Rune:").grid(column=3, row=1)
        ttk.Label(self, text="Head:").grid(column=0, row=2, sticky=tk.E)
        ttk.Label(self, text="Shoulders:").grid(column=0, row=3, sticky=tk.E)
        ttk.Label(self, text="Chest:").grid(column=0, row=4, sticky=tk.E)
        ttk.Label(self, text="Gloves:").grid(column=0, row=5, sticky=tk.E)
        ttk.Label(self, text="Pants:").grid(column=0, row=6, sticky=tk.E)
        ttk.Label(self, text="Boots:").grid(column=0, row=7, sticky=tk.E)

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
        # ttk.Button(self, text="Save", command=self.save).grid(column=3, row=8)

        #WeaponObject code
        self.mh1 = tk.StringVar
        self.mh2 = tk.StringVar

        # create the list for the drop downs
        self.mh1List = weaponsDB.getMHWeapons()
        self.oh1List = weaponsDB.getOHWeapons()
        self.mh1InsList = weaponsDB.getInscription()
        self.oh1InsList = weaponsDB.getInscription()
        self.mh1SigList = weaponsDB.getPvESigils()
        self.oh1SigList = weaponsDB.getPvESigils()

        self.mh2List = weaponsDB.getMHWeapons()
        self.oh2List = weaponsDB.getOHWeapons()
        self.mh2InsList = weaponsDB.getInscription()
        self.oh2InsList = weaponsDB.getInscription()
        self.mh2SigList = weaponsDB.getPvESigils()
        self.oh2SigList = weaponsDB.getPvESigils()

        # create the drop downs for the weapons, inscriptions, and sigils
        self.mainHand1 = ttk.Combobox(self, state="readonly", values=self.mh1List)
        # self.mainHand1.grid(column=1, row=1)
        self.mainHand1.bind("<<ComboboxSelected>>", self.offHand1None)
        self.offHand1 = ttk.Combobox(self, state="readonly", values=self.oh1List)
        self.mainHand1Ins = ttk.Combobox(self, state="readonly", values=self.mh1InsList)
        self.offHand1Ins = ttk.Combobox(self, state="readonly", values=self.oh1InsList)
        self.mainHand1Sig = ttk.Combobox(self, state="readonly", values=self.mh1SigList)
        self.offHand1Sig = ttk.Combobox(self, state="readonly", values=self.oh1SigList)

        self.mainHand2 = ttk.Combobox(self, state="readonly", values=self.mh2List)
        # self.mainHand2.grid(column=1, row=3)
        self.mainHand2.bind("<<ComboboxSelected>>", self.offHand2None)
        self.offHand2 = ttk.Combobox(self, state="readonly", values=self.oh2List)
        self.mainHand2Ins = ttk.Combobox(self, state="readonly", values=self.mh2InsList)
        self.offHand2Ins = ttk.Combobox(self, state="readonly", values=self.oh2InsList)
        self.mainHand2Sig = ttk.Combobox(self, state="readonly", values=self.mh2SigList)
        self.offHand2Sig = ttk.Combobox(self, state="readonly", values=self.oh2SigList)

        # create the labels for the hands, inscriptions and sigils
        tk.Label(self, text="Weapon:").grid(column=5, row=1)
        tk.Label(self, text="Insignia:").grid(column=6, row=1)
        tk.Label(self, text="Sigil:").grid(column=7, row=1)
        tk.Label(self, text="Main Hand1:").grid(column=4, row=2, sticky=tk.E)
        tk.Label(self, text="Off Hand1:").grid(column=4, row=3, sticky=tk.E)
        tk.Label(self, text="Main Hand2:").grid(column=4, row=4, sticky=tk.E)
        tk.Label(self, text="Off Hand2:").grid(column=4, row=5, sticky=tk.E)

        self.mainHand1.grid(column=5, row=2)
        self.offHand1.grid(column=5, row=3)
        self.mainHand2.grid(column=5, row=4)
        self.offHand2.grid(column=5, row=5)
        self.mainHand1Ins.grid(column=6, row=2)
        self.offHand1Ins.grid(column=6, row=3)
        self.mainHand2Ins.grid(column=6, row=4)
        self.offHand2Ins.grid(column=6, row=5)
        self.mainHand1Sig.grid(column=7, row=2)
        self.offHand1Sig.grid(column=7, row=3)
        self.mainHand2Sig.grid(column=7, row=4)
        self.offHand2Sig.grid(column=7, row=5)

        # Add padding to all child components
        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=3)

    def offHand1None(self, event):
        self.mainHand1.current()
        self.mh1 = self.mainHand1.get()
        if self.mh1 == "Greatsword" or self.mh1 == "Shortbow":
            self.oh1List = ["None"]
            self.offHand1 = ttk.Combobox(self, state="readonly", values=self.oh1List)
            self.offHand1.grid(column=5, row=3)
        else:
            self.oh1List = ["None", "Sword", "Focus", "Shield"]
            self.offHand1 = ttk.Combobox(self, state="readonly", values=self.oh1List)
            self.offHand1.grid(column=5, row=3)

    def offHand2None(self, event):
        self.mainHand2.current()
        self.mh2 = self.mainHand2.get()
        if self.mh2 == "Greatsword" or self.mh2 == "Staff" or self.mh2 == "Shortbow":
            self.oh2List = ["None"]
            self.offHand2 = ttk.Combobox(self, state="readonly", values=self.oh2List)
            self.offHand2.grid(column=5, row=5)
        else:
            self.oh1List = ["None", "Sword", "Focus", "Shield"]
            self.offHand1 = ttk.Combobox(self, state="readonly", values=self.oh1List)
            self.offHand1.grid(column=5, row=5)


if __name__== "__main__":
    root = tk.Tk()
    root.title("Build Template")
    MainApplication(root)
    root.mainloop()
