#!user/bin/env/python3
# This module is used for creating the SQL code that will be used in the WeaponsObjectUI
import sqlite3
from contextlib import closing

# connect to the database
sqliteFile = 'C:/SQLite/Databases/Test.db'
conn = sqlite3.connect(sqliteFile)
c = conn.cursor()

# The following is for the Inscriptions/Insignias
# Counter for the Insignias/Inscriptions
def inscriptionCount():
    inscriptCount = '''SELECT * FROM tbl_Insignias
                    WHERE PvE IS 1 AND Active IS 1'''
    c.execute(inscriptCount)
    inscriptCounter = len(c.fetchall())
    return inscriptCounter

def getInscription():
    inscriptList = []
    x = 0
    j = inscriptionCount()
    query1 = '''SELECT Insignia FROM tbl_Insignias
                WHERE PvE IS 1 AND Active IS 1'''
    c.execute(query1)
    while x < j:
        inscript = c.fetchone()
        inscriptList.append(inscript[0])
        x += 1
    return inscriptList

def getInscriptionID(inscription):
    inscriptionID = '''SELECT InsigniaID FROM tbl_Insignias WHERE Insignia is ?'''
    c.execute(inscriptionID, (inscription,))
    a = c.fetchone()
    inscriptid = a[0]
    return inscriptid

# The following is all of the code to get the Sigils for the Weapons
def sigilPvPCount():
    sigilCount = '''SELECT * FROM tbl_Sigils
                    WHERE PvP IS 1 AND Active IS 1'''
    c.execute(sigilCount)
    sigilCounter = len(c.fetchall())
    return sigilCounter

def sigilPvECount():
    sigilCount = '''SELECT * FROM tbl_Sigils
                    WHERE PvE IS 1 AND Active IS 1'''
    c.execute(sigilCount)
    sigilCounter = len(c.fetchall())
    return sigilCounter

def getPvPSigils():
    sigilList = []
    x = 0
    j = sigilPvPCount()
    query1 = '''SELECT SigilName FROM tbl_Sigils
                WHERE PvP IS 1 AND Active IS 1'''
    c.execute(query1)
    while x < j:
        sigil = c.fetchone()
        sigilList.append(sigil[0])
        x += 1
    return sigilList

def getPvESigils():
    sigilList = []
    x = 0
    j = sigilPvECount()
    query1 = '''SELECT SigilName FROM tbl_Sigils
                WHERE PvE IS 1 AND Active IS 1'''
    c.execute(query1)
    while x < j:
        sigil = c.fetchone()
        sigilList.append(sigil[0])
        x += 1
    return sigilList

# The following code is used for the Weapon selections
def mhWeaponCount():
    weaponCount = '''SELECT * FROM tbl_Weapons
                    WHERE MainHand IS 1 AND Mesmer IS 1'''
    c.execute(weaponCount)
    weaponCounter = len(c.fetchall())
    return weaponCounter

def getMHWeapons():
    weaponList = []
    x = 0
    j = mhWeaponCount()
    query1 = '''SELECT WeaponName FROM tbl_Weapons
                WHERE MainHand IS 1 AND Mesmer IS 1'''
    c.execute(query1)
    while x < j:
        weapon = c.fetchone()
        weaponList.append(weapon[0])
        x += 1
    return weaponList

def ohWeaponCount():
    weaponCount = '''SELECT * FROM tbl_Weapons
                    WHERE OffHand IS 1 AND Mesmer IS 1'''
    c.execute(weaponCount)
    weaponCounter = len(c.fetchall())
    return weaponCounter

def getOHWeapons():
    weaponList = []
    x = 0
    j = ohWeaponCount()
    query1 = '''SELECT WeaponName FROM tbl_Weapons
                WHERE OffHand IS 1 AND Mesmer IS 1'''
    c.execute(query1)
    while x < j:
        weapon = c.fetchone()
        weaponList.append(weapon[0])
        x += 1
    return weaponList