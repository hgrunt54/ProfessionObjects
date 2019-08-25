#!user\bin\env\python3
import tkinter as tk
from tkinter import ttk
import weaponsDB
import random

gm = random.randint(0, 1)
p = random.randint(0, 4)

# create the Weapons frame class
class pveWeaponsObject(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="5 5 5 5")
        self.pack(fill=tk.BOTH, expand=True)
        self.mh1 = tk.StringVar
        self.mh2 = tk.StringVar

        # create the list for the drop downs
        self.mh1List = ["Greatsword", "Sword", "Scepter", "Shortbow"]
        self.oh1List = ["None", "Sword", "Focus", "Shield"]
        self.mh1InsList = weaponsDB.getInscription()
        self.oh1InsList = weaponsDB.getInscription()
        self.mh1SigList = weaponsDB.getPvESigils()
        self.oh1SigList = weaponsDB.getPvESigils()

        self.mh2List = ["Greatsword", "Sword", "Scepter", "Shortbow"]
        self.oh2List = ["None", "Sword", "Focus", "Shield"]
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
        tk.Label(self, text="Weapon:").grid(column=1, row=0)
        tk.Label(self, text="Insignia:").grid(column=2, row=0)
        tk.Label(self, text="Sigil:").grid(column=3, row=0)
        tk.Label(self, text="Main Hand1:").grid(column=0, row=1, sticky=tk.E)
        tk.Label(self, text="Off Hand1:").grid(column=0, row=2, sticky=tk.E)
        tk.Label(self, text="Main Hand2:").grid(column=0, row=3, sticky=tk.E)
        tk.Label(self, text="Off Hand2:").grid(column=0, row=4, sticky=tk.E)

        self.mainHand1.grid(column=1, row=1)
        self.offHand1.grid(column=1, row=2)
        self.mainHand2.grid(column=1, row=3)
        self.offHand2.grid(column=1, row=4)
        self.mainHand1Ins.grid(column=2, row=1)
        self.offHand1Ins.grid(column=2, row=2)
        self.mainHand2Ins.grid(column=2, row=3)
        self.offHand2Ins.grid(column=2, row=4)
        self.mainHand1Sig.grid(column=3, row=1)
        self.offHand1Sig.grid(column=3, row=2)
        self.mainHand2Sig.grid(column=3, row=3)
        self.offHand2Sig.grid(column=3, row=4)


        # Add padding to all child components
        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=3)

    def offHand1None(self, event):
        self.mainHand1.current()
        self.mh1 = self.mainHand1.get()
        if self.mh1 == "Greatsword" or self.mh1 == "Shortbow":
            self.oh1List = ["None"]
            self.offHand1 = ttk.Combobox(self, state="readonly", values=self.oh1List)
            self.offHand1.grid(column=1, row=2)
        else:
            self.oh1List = ["None", "Sword", "Focus", "Shield"]
            self.offHand1 = ttk.Combobox(self, state="readonly", values=self.oh1List)
            self.offHand1.grid(column=1, row=2)

    def offHand2None(self, event):
        self.mainHand2.current()
        self.mh2 = self.mainHand2.get()
        if self.mh2 == "Greatsword" or self.mh2 == "Shortbow":
            self.oh2List = ["None"]
            self.offHand2 = ttk.Combobox(self, state="readonly", values=self.oh2List)
            self.offHand2.grid(column=1, row=4)
        else:
            self.oh1List = ["None", "Sword", "Focus", "Shield"]
            self.offHand1 = ttk.Combobox(self, state="readonly", values=self.oh1List)
            self.offHand1.grid(column=1, row=4)

class pvpWeaponsObject(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="5 5 5 5")
        self.pack(fill=tk.BOTH, expand=True)
        self.mh1 = tk.StringVar
        self.mh2 = tk.StringVar
        self.p = random.randint(0, 4)
        self.prof = profession(self.p)

        # create the list for the drop downs
        self.mh1List = weaponsDB.getMHWeapons()
        self.oh1List = weaponsDB.getOHWeapons()
        self.mh1SigList = weaponsDB.getPvPSigils()
        self.oh1SigList = weaponsDB.getPvPSigils()

        self.mh2List = weaponsDB.getMHWeapons()
        self.oh2List = weaponsDB.getOHWeapons()
        self.mh2SigList = weaponsDB.getPvPSigils()
        self.oh2SigList = weaponsDB.getPvPSigils()

        # create the drop downs for the weapons, inscriptions, and sigils
        self.mainHand1 = ttk.Combobox(self, state="readonly", values=self.mh1List)
        self.mainHand1.bind("<<ComboboxSelected>>", self.offHand1None)
        self.offHand1 = ttk.Combobox(self, state="readonly", values=self.oh1List)
        self.mainHand1Sig = ttk.Combobox(self, state="readonly", values=self.mh1SigList)
        self.offHand1Sig = ttk.Combobox(self, state="readonly", values=self.oh1SigList)

        self.mainHand2 = ttk.Combobox(self, state="readonly", values=self.mh2List)
        self.mainHand2.bind("<<ComboboxSelected>>", self.offHand2None)
        self.offHand2 = ttk.Combobox(self, state="readonly", values=self.oh2List)
        self.mainHand2Sig = ttk.Combobox(self, state="readonly", values=self.mh2SigList)
        self.offHand2Sig = ttk.Combobox(self, state="readonly", values=self.oh2SigList)

        # create the labels for the hands, inscriptions and sigils
        tk.Label(self, text="Weapon:").grid(column=1, row=0)
        tk.Label(self, text="Sigil:").grid(column=3, row=0)
        tk.Label(self, text="Main Hand1:").grid(column=0, row=1, sticky=tk.E)
        tk.Label(self, text="Off Hand1:").grid(column=0, row=2, sticky=tk.E)
        tk.Label(self, text="Main Hand2:").grid(column=0, row=3, sticky=tk.E)
        tk.Label(self, text="Off Hand2:").grid(column=0, row=4, sticky=tk.E)

        self.mainHand1.grid(column=1, row=1)
        self.offHand1.grid(column=1, row=2)
        self.mainHand2.grid(column=1, row=3)
        self.offHand2.grid(column=1, row=4)
        self.mainHand1Sig.grid(column=3, row=1)
        self.offHand1Sig.grid(column=3, row=2)
        self.mainHand2Sig.grid(column=3, row=3)
        self.offHand2Sig.grid(column=3, row=4)

        # Add padding to all child components
        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=3)

    def offHand1None(self, event):
        self.mainHand1.current()
        self.mh1 = self.mainHand1.get()
        if self.mh1 == "Greatsword" or self.mh1 == "Staff" or self.mh1 == "Shortbow":
            self.oh1List = ["None"]
            self.offHand1 = ttk.Combobox(self, state="readonly", values=self.oh1List)
            self.offHand1.grid(column=1, row=2)
        else:
            self.oh1List = ["None", "Sword", "Focus", "Shield"]
            self.offHand1 = ttk.Combobox(self, state="readonly", values=self.oh1List)
            self.offHand1.grid(column=1, row=2)

    def offHand2None(self, event):
        self.mainHand2.current()
        self.mh2 = self.mainHand2.get()
        if self.mh2 == "Greatsword" or self.mh2 == "Staff" or self.mh2 == "Shortbow":
            self.oh2List = ["None"]
            self.offHand2 = ttk.Combobox(self, state="readonly", values=self.oh2List)
            self.offHand2.grid(column=1, row=4)
        else:
            self.oh1List = ["None", "Sword", "Focus", "Shield"]
            self.offHand1 = ttk.Combobox(self, state="readonly", values=self.oh1List)
            self.offHand1.grid(column=1, row=4)

def gameMode(gm):
    if gm == 0:
        gMode = "PvE"
    else:
        gMode = "PvP"
    return gMode

def profession(p):
    if p == 0:
        prof = "Memser"
    elif p == 1:
        prof = "Necromancer"
    elif p == 2:
        prof = "Elementalist"
    elif p == 3:
        prof = "Thief"
    elif p == 4:
        prof = "Ranger"
    return prof

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Weapons Object")
    pvpWeaponsObject(root)
    root.mainloop()