#! /user/bin/env Python 3.7
import tkinter as tk
from tkinter import ttk
import db2
import armorDB
import weaponsDB

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
        self.professionCombo.bind("<<ComboboxSelected>>", self.getProfessionChoice)
        ttk.Label(self, text="Game Mode:").grid(column=4, row=0)
        self.gameModeCombo.grid(column=5, row=0)
        self.gameModeCombo.bind("<<ComboboxSelected>>", self.getGameModeChoice)
        ttk.Label(self, text="Build Type:").grid(column=6, row=0)
        self.buildType.grid(column=7, row=0)
        # ttk.Button(self, text="Save", command=self.save).grid(column=8, row=0)

        # ArmorObject code
        # create the drop down lists
        # self.insigList = armorDB.getPvEInsignias()
        # self.runeList = armorDB.getPvERunes()

        # defining the drop down variables
        self.headIns = ttk.Combobox(self, state='readonly')
        self.headRune = ttk.Combobox(self, state='readonly')
        self.shoulderIns = ttk.Combobox(self, state='readonly')
        self.shoulderRune = ttk.Combobox(self, state='readonly')
        self.chestIns = ttk.Combobox(self, state='readonly')
        self.chestRune = ttk.Combobox(self, state='readonly')
        self.glovesIns = ttk.Combobox(self, state='readonly')
        self.glovesRune = ttk.Combobox(self, state='readonly')
        self.pantsIns = ttk.Combobox(self, state='readonly')
        self.pantsRune = ttk.Combobox(self, state='readonly')
        self.bootsIns = ttk.Combobox(self, state='readonly')
        self.bootsRune = ttk.Combobox(self, state='readonly')

            # Labels:
        ttk.Label(self, text="Insignia:").grid(column=1, row=1)
        ttk.Label(self, text="Rune:").grid(column=2, row=1)
        ttk.Label(self, text="Head:").grid(column=0, row=2)
        ttk.Label(self, text="Shoulders:").grid(column=0, row=3)
        ttk.Label(self, text="Chest:").grid(column=0, row=4)
        ttk.Label(self, text="Gloves:").grid(column=0, row=5)
        ttk.Label(self, text="Pants:").grid(column=0, row=6)
        ttk.Label(self, text="Boots:").grid(column=0, row=7)

        # Inscription dropdowns locations
        self.headIns.grid(column=1, row=2)
        self.shoulderIns.grid(column=1, row=3)
        self.chestIns.grid(column=1, row=4)
        self.glovesIns.grid(column=1, row=5)
        self.pantsIns.grid(column=1, row=6)
        self.bootsIns.grid(column=1, row=7)

        # Rune dropdowns location:
        self.headRune.grid(column=2, row=2)
        self.shoulderRune.grid(column=2, row=3)
        self.chestRune.grid(column=2, row=4)
        self.glovesRune.grid(column=2, row=5)
        self.pantsRune.grid(column=2, row=6)
        self.bootsRune.grid(column=2, row=7)

        #WeaponObject code
        # create the drop downs for the weapons, inscriptions, and sigils
        self.mainHand1 = ttk.Combobox(self, state="readonly")
        self.mainHand1.bind("<<ComboboxSelected>>", self.offHand1None)
        self.offHand1 = ttk.Combobox(self, state="readonly")
        self.mainHand1Ins = ttk.Combobox(self, state="readonly")
        self.offHand1Ins = ttk.Combobox(self, state="readonly")
        self.mainHand1Sig = ttk.Combobox(self, state="readonly")
        self.offHand1Sig = ttk.Combobox(self, state="readonly")

        self.mainHand2 = ttk.Combobox(self, state="readonly")
        self.mainHand2.bind("<<ComboboxSelected>>", self.offHand2None)
        self.offHand2 = ttk.Combobox(self, state="readonly")
        self.mainHand2Ins = ttk.Combobox(self, state="readonly")
        self.offHand2Ins = ttk.Combobox(self, state="readonly")
        self.mainHand2Sig = ttk.Combobox(self, state="readonly")
        self.offHand2Sig = ttk.Combobox(self, state="readonly")

        # create the labels for the hands, inscriptions and sigils
        tk.Label(self, text="Weapon:").grid(column=4, row=1)
        tk.Label(self, text="Sigil:").grid(column=5, row=1)
        tk.Label(self, text="Inscription:").grid(column=6, row=1)
        tk.Label(self, text="Main Hand1:").grid(column=3, row=2)
        tk.Label(self, text="Off Hand1:").grid(column=3, row=3)
        tk.Label(self, text="Main Hand2:").grid(column=3, row=4)
        tk.Label(self, text="Off Hand2:").grid(column=3, row=5)

        self.mainHand1.grid(column=4, row=2)
        self.offHand1.grid(column=4, row=3)
        self.mainHand2.grid(column=4, row=4)
        self.offHand2.grid(column=4, row=5)
        self.mainHand1Ins.grid(column=5, row=2)
        self.offHand1Ins.grid(column=5, row=3)
        self.mainHand2Ins.grid(column=5, row=4)
        self.offHand2Ins.grid(column=5, row=5)
        self.mainHand1Sig.grid(column=6, row=2)
        self.offHand1Sig.grid(column=6, row=3)
        self.mainHand2Sig.grid(column=6, row=4)
        self.offHand2Sig.grid(column=6, row=5)



        #Add button for test adding pveWeaponsObject to tbl_PvEWeaponsObjects
        # tk.Button(self, text="Save", command=self.save).grid(column=3, row=5)

        # Add padding to all child components
        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=3)

    def offHand1None(self, event):
        self.mainHand1.current()
        self.mh1 = self.mainHand1.get()
        if self.mh1 == "Greatsword" or self.mh1 == "Staff" or self.mh1 == "Shortbow":
            self.oh1List = ["None"]
            self.offHand1 = ttk.Combobox(self, state="readonly", values=self.oh1List)
            self.offHand1.grid(column=4, row=3)
        else:
            self.oh1List = weaponsDB.getOHWeapons(self.prof)
            self.offHand1 = ttk.Combobox(self, state="readonly", values=self.oh1List)
            self.offHand1.grid(column=4, row=3)

    def offHand2None(self, event):
        self.mainHand2.current()
        self.mh2 = self.mainHand2.get()
        if self.mh2 == "Greatsword" or self.mh2 == "Staff" or self.mh2 == "Shortbow":
            self.oh2List = ["None"]
            self.offHand2 = ttk.Combobox(self, state="readonly", values=self.oh2List)
            self.offHand2.grid(column=4, row=5)
        else:
            self.oh1List = weaponsDB.getOHWeapons(self.prof)
            self.offHand1 = ttk.Combobox(self, state="readonly", values=self.oh1List)
            self.offHand1.grid(column=4, row=5)

    def getProfessionChoice(self, event):
        self.mh1 = tk.StringVar
        self.mh2 = tk.StringVar
        self.professionCombo.current()
        self.prof = self.professionCombo.get()
        self.mh1List = weaponsDB.getMHWeapons(self.prof)
        self.oh1List = weaponsDB.getOHWeapons(self.prof)
        self.mh2List = weaponsDB.getMHWeapons(self.prof)
        self.oh2List = weaponsDB.getOHWeapons(self.prof)
        tk.Label(self, text="Weapon:").grid(column=4, row=1)
        self.mainHand1 = ttk.Combobox(self, state="readonly", values=self.mh1List)
        self.mainHand1.bind("<<ComboboxSelected>>", self.offHand1None)
        self.offHand1 = ttk.Combobox(self, state="readonly", values=self.oh1List)
        self.mainHand2 = ttk.Combobox(self, state="readonly", values=self.mh2List)
        self.mainHand2.bind("<<ComboboxSelected>>", self.offHand2None)
        self.offHand2 = ttk.Combobox(self, state="readonly", values=self.oh2List)
        self.mainHand1.grid(column=4, row=2)
        self.offHand1.grid(column=4, row=3)
        self.mainHand2.grid(column=4, row=4)
        self.offHand2.grid(column=4, row=5)

    def getGameModeChoice(self, event):
        self.gameModeCombo.current()
        self.gm = self.gameModeCombo.get()
        if self.gm == "PvP":
            # create the drop down lists
            self.insigList = armorDB.getPvPInsignias()
            self.runeList = armorDB.getPvPRunes()

            # defining the drop down variables
            self.insignia = ttk.Combobox(self, state='readonly', values=self.insigList)
            self.rune = ttk.Combobox(self, state='readonly', values=self.runeList)

            # creating the labels and drop downs in the frame
            ttk.Label(self, text="Insignia:").grid(column=1, row=1)
            ttk.Label(self, text="Rune:").grid(column=2, row=1)
            self.insignia.grid(column=1, row=2)
            self.rune.grid(column=2, row=2)

            # The following are unnecessary will be set to none.
            self.shoulderIns = ttk.Combobox(self, state='readonly', values=["None"])
            self.shoulderRune = ttk.Combobox(self, state='readonly', values=["None"])
            self.chestIns = ttk.Combobox(self, state='readonly', values=["None"])
            self.chestRune = ttk.Combobox(self, state='readonly', values=["None"])
            self.glovesIns = ttk.Combobox(self, state='readonly', values=["None"])
            self.glovesRune = ttk.Combobox(self, state='readonly', values=["None"])
            self.pantsIns = ttk.Combobox(self, state='readonly', values=["None"])
            self.pantsRune = ttk.Combobox(self, state='readonly', values=["None"])
            self.bootsIns = ttk.Combobox(self, state='readonly', values=["None"])
            self.bootsRune = ttk.Combobox(self, state='readonly', values=["None"])
            self.mainHand1Ins = ttk.Combobox(self, state="readonly", values=["None"])
            self.offHand1Ins = ttk.Combobox(self, state="readonly", values=["None"])
            self.mainHand2Ins = ttk.Combobox(self, state="readonly", values=["None"])
            self.offHand2Ins = ttk.Combobox(self, state="readonly", values=["None"])
            self.mainHand1Ins.grid(column=6, row=2)
            self.offHand1Ins.grid(column=6, row=3)
            self.mainHand2Ins.grid(column=6, row=4)
            self.offHand2Ins.grid(column=6, row=5)
            self.mainHand1Ins.set("None")
            self.offHand1Ins.set("None")
            self.mainHand2Ins.set("None")
            self.offHand2Ins.set("None")
            self.mainHand1Ins.set("None")
            self.offHand1Ins.set("None")
            self.mainHand2Ins.set("None")
            self.offHand2Ins.set("None")

            ttk.Label(self, text="Shoulders:").grid(column=0, row=3)
            ttk.Label(self, text="Chest:").grid(column=0, row=4)
            ttk.Label(self, text="Gloves:").grid(column=0, row=5)
            ttk.Label(self, text="Pants:").grid(column=0, row=6)
            ttk.Label(self, text="Boots:").grid(column=0, row=7)
            tk.Label(self, text="Inscription:").grid(column=6, row=1)
            self.shoulderIns.grid(column=1, row=3)
            self.chestIns.grid(column=1, row=4)
            self.glovesIns.grid(column=1, row=5)
            self.pantsIns.grid(column=1, row=6)
            self.bootsIns.grid(column=1, row=7)
            self.shoulderRune.grid(column=2, row=3)
            self.chestRune.grid(column=2, row=4)
            self.glovesRune.grid(column=2, row=5)
            self.pantsRune.grid(column=2, row=6)
            self.bootsRune.grid(column=2, row=7)
            self.shoulderIns.set("None")
            self.chestIns.set("None")
            self.glovesIns.set("None")
            self.pantsIns.set("None")
            self.bootsIns.set("None")
            self.shoulderRune.set("None")
            self.chestRune.set("None")
            self.glovesRune.set("None")
            self.pantsRune.set("None")
            self.bootsRune.set("None")

            # create the list for the drop downs
            self.mh1SigList = weaponsDB.getPvPSigils()
            self.oh1SigList = weaponsDB.getPvPSigils()
            self.mh2SigList = weaponsDB.getPvPSigils()
            self.oh2SigList = weaponsDB.getPvPSigils()

            # create the drop downs for the weapons, inscriptions, and sigils
            self.mainHand1Sig = ttk.Combobox(self, state="readonly", values=self.mh1SigList)
            self.offHand1Sig = ttk.Combobox(self, state="readonly", values=self.oh1SigList)
            self.mainHand2Sig = ttk.Combobox(self, state="readonly", values=self.mh2SigList)
            self.offHand2Sig = ttk.Combobox(self, state="readonly", values=self.oh2SigList)

            # create the labels for the hands, inscriptions and sigils
            tk.Label(self, text="Sigil:").grid(column=5, row=1)
            tk.Label(self, text="Main Hand1:").grid(column=3, row=2)
            tk.Label(self, text="Off Hand1:").grid(column=3, row=3)
            tk.Label(self, text="Main Hand2:").grid(column=3, row=4)
            tk.Label(self, text="Off Hand2:").grid(column=3, row=5)
            self.mainHand1Sig.grid(column=5, row=2)
            self.offHand1Sig.grid(column=5, row=3)
            self.mainHand2Sig.grid(column=5, row=4)
            self.offHand2Sig.grid(column=5, row=5)

            tk.Button(self, text="Save PvP Build", command=self.savePvPBuild).grid(column=7, row=6)

        else:
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
            ttk.Label(self, text="Insignia:").grid(column=1, row=1)
            ttk.Label(self, text="Rune:").grid(column=2, row=1)
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
            self.headRune.grid(column=2, row=2)
            self.shoulderRune.grid(column=2, row=3)
            self.chestRune.grid(column=2, row=4)
            self.glovesRune.grid(column=2, row=5)
            self.pantsRune.grid(column=2, row=6)
            self.bootsRune.grid(column=2, row=7)

            self.mh1InsList = weaponsDB.getInscription()
            self.oh1InsList = weaponsDB.getInscription()
            self.mh1SigList = weaponsDB.getPvESigils()
            self.oh1SigList = weaponsDB.getPvESigils()
            self.mh2InsList = weaponsDB.getInscription()
            self.oh2InsList = weaponsDB.getInscription()
            self.mh2SigList = weaponsDB.getPvESigils()
            self.oh2SigList = weaponsDB.getPvESigils()

            self.mainHand1Ins = ttk.Combobox(self, state="readonly", values=self.mh1InsList)
            self.offHand1Ins = ttk.Combobox(self, state="readonly", values=self.oh1InsList)
            self.mainHand1Sig = ttk.Combobox(self, state="readonly", values=self.mh1SigList)
            self.offHand1Sig = ttk.Combobox(self, state="readonly", values=self.oh1SigList)
            self.mainHand2Ins = ttk.Combobox(self, state="readonly", values=self.mh2InsList)
            self.offHand2Ins = ttk.Combobox(self, state="readonly", values=self.oh2InsList)
            self.mainHand2Sig = ttk.Combobox(self, state="readonly", values=self.mh2SigList)
            self.offHand2Sig = ttk.Combobox(self, state="readonly", values=self.oh2SigList)

            tk.Label(self, text="Inscription:").grid(column=6, row=1)
            tk.Label(self, text="Sigil:").grid(column=5, row=1)
            tk.Label(self, text="Main Hand1:").grid(column=3, row=2)
            tk.Label(self, text="Off Hand1:").grid(column=3, row=3)
            tk.Label(self, text="Main Hand2:").grid(column=3, row=4)
            tk.Label(self, text="Off Hand2:").grid(column=3, row=5)

            self.mainHand1Sig.grid(column=5, row=2)
            self.offHand1Sig.grid(column=5, row=3)
            self.mainHand2Sig.grid(column=5, row=4)
            self.offHand2Sig.grid(column=5, row=5)
            self.mainHand1Ins.grid(column=6, row=2)
            self.offHand1Ins.grid(column=6, row=3)
            self.mainHand2Ins.grid(column=6, row=4)
            self.offHand2Ins.grid(column=6, row=5)

            tk.Button(self, text="Save PvE Build", command=self.savePvEBuild).grid(column=7, row=6)

    def saveProf(self): #Saves the variables and inserts the data into the necessary database tables.
        self.professionCombo.current()
        self.gameModeCombo.current()
        self.buildType.current()
        self.BuildNameChoice = self.buildName.get()
        self.ProfessionChoice = self.professionCombo.get()
        self.GameModeChoice = self.gameModeCombo.get()
        self.buildTypeChoice = self.buildType.get()
        db2.addProfessionObject(self.BuildNameChoice, self.ProfessionChoice, self.GameModeChoice, self.buildTypeChoice)

    def savePvPArmor(self):
        self.insignia.current()
        self.rune.current()
        self.insig = self.insignia.get()
        self.r = self.rune.get()
        armorDB.addPvPArmorObject(self.insig, self.r)

    def savePvEArmor(self):
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

        armorDB.addPvEArmorObject(self.hI, self.shI, self.chI, self.glI, self.paI, self.boI,
                                  self.hR, self.shR, self.chR, self.glR, self.paR, self.boR)

    def savePvPWeapons(self):
        self.mainHand1.current()
        self.mh1 = self.mainHand1.get()
        self.offHand1Sig.current()
        self.oh1 = self.offHand1.get()
        self.mainHand2Sig.current()
        self.mh2 = self.mainHand2.get()
        self.offHand2Sig.current()
        self.oh2 = self.offHand2.get()
        self.mainHand1Sig.current()
        self.mh1s = self.mainHand1Sig.get()
        self.offHand1Sig.current()
        self.oh1s = self.offHand1Sig.get()
        self.mainHand2Sig.current()
        self.mh2s = self.mainHand2Sig.get()
        self.offHand2Sig.current()
        self.oh2s = self.offHand2Sig.get()

        weaponsDB.addPvPWeaponsObject(self.mh1, self.oh1, self.mh2, self.mh2, self.mh1s, self.oh1s, self.mh2s, self.oh2s)

    def savePvEWeapons(self):
        self.mainHand1.current()
        self.mh1 = self.mainHand1.get()
        self.offHand1Sig.current()
        self.oh1 = self.offHand1.get()
        self.mainHand2Sig.current()
        self.mh2 = self.mainHand2.get()
        self.offHand2Sig.current()
        self.oh2 = self.offHand2.get()
        self.mainHand1Ins.current()
        self.mh1i = self.mainHand1Ins.get()
        self.offHand1Ins.current()
        self.oh1i = self.offHand1Ins.get()
        self.mainHand2Ins.current()
        self.mh2i = self.mainHand2Ins.get()
        self.offHand2Ins.current()
        self.oh2i = self.offHand2Ins.get()
        self.mainHand1Sig.current()
        self.mh1s = self.mainHand1Sig.get()
        self.offHand1Sig.current()
        self.oh1s = self.offHand1Sig.get()
        self.mainHand2Sig.current()
        self.mh2s = self.mainHand2Sig.get()
        self.offHand2Sig.current()
        self.oh2s = self.offHand2Sig.get()

        weaponsDB.addPvEWeaponsObject(self.mh1, self.oh1, self.mh2, self.mh2, self.mh1i, self.oh1i, self.mh2i, self.oh2i,
                                      self.mh1s, self.oh1s, self.mh2s, self.oh2s)

    def savePvPBuild(self):
        self.saveProf()
        self.savePvPArmor()
        self.savePvPWeapons()

    def savePvEBuild(self):
        self.saveProf()
        self.savePvEArmor()
        self.savePvEWeapons()

if __name__== "__main__":
    root = tk.Tk()
    root.title("Build Template")
    MainApplication(root)
    root.mainloop()
