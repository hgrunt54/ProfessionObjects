#!user/bin/env/python3
# This module is used for creating the SQL code that will be used in the WeaponsObjectUI
import sqlite3
from contextlib import closing

# connect to the database
sqliteFile = './../Test.db'
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
def mhWeaponCount(profession):
    weaponCount = 'SELECT * FROM tbl_Weapons WHERE MainHand IS 1 AND "%s" IS 1' % (profession)
    c.execute(weaponCount)
    weaponCounter = len(c.fetchall())
    return weaponCounter

def getMHWeapons(profession):
    weaponList = []
    x = 0
    j = mhWeaponCount(profession)
    query1 = 'SELECT WeaponName FROM tbl_Weapons WHERE MainHand IS 1 AND "%s" IS 1' % (profession)
    c.execute(query1)
    while x < j:
        weapon = c.fetchone()
        weaponList.append(weapon[0])
        x += 1
    return weaponList

def ohWeaponCount(profession):
    weaponCount = 'SELECT * FROM tbl_Weapons WHERE OffHand IS 1 AND "%s" IS 1' % (profession)
    c.execute(weaponCount)
    weaponCounter = len(c.fetchall())
    return weaponCounter

def getOHWeapons(profession):
    weaponList = []
    x = 0
    j = ohWeaponCount(profession)
    query1 = 'SELECT WeaponName FROM tbl_Weapons WHERE OffHand IS 1 AND "%s" IS 1' % (profession)
    c.execute(query1)
    while x < j:
        weapon = c.fetchone()
        weaponList.append(weapon[0])
        x += 1
    return weaponList

def getPvPWeaponsObjectID():
    maxPvPWOid = '''SELECT MAX(PvPWeaponsObjectID) FROM tbl_PvPWeaponsObjects'''
    c.execute(maxPvPWOid)
    a = c.fetchone()
    PvPWOid = a[0] + 1
    return PvPWOid

def addPvPWeaponsObject(mh1, oh1, mh2, oh2, mh1s, oh1s, mh2s, oh2s):
    PvPWeaponsObjectID = getPvPWeaponsObjectID()
    insert = '''INSERT INTO tbl_PvPWeaponsObjects (PvPWeaponsObjectID, MainHand1, OffHand1, MainHand2, OffHand2,
                MainHand1Sigil, OffHand1Sigil, MainHand2Sigil, OffHand2Sigil) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)'''
    c.execute(insert, (PvPWeaponsObjectID, mh1, oh1, mh2, oh2, mh1s, oh1s, mh2s, oh2s))
    conn.commit()

def getPvEWeaponsObjectID():
    maxPvEWOid = '''SELECT MAX(PvEWeaponsObjectID) FROM tbl_PvEWeaponsObjects'''
    c.execute(maxPvEWOid)
    a = c.fetchone()
    PvEWOid = a[0] + 1
    return PvEWOid

def addPvEWeaponsObject(mh1, oh1, mh2, oh2, mh1i, oh1i, mh2i, oh2i, mh1s, oh1s, mh2s, oh2s):
    PvEWeaponsObjectID = getPvEWeaponsObjectID()
    insert = '''INSERT INTO tbl_PvEWeaponsObjects (PvEWeaponsObjectID, MainHand1, OffHand1, MainHand2, OffHand2,
                MainHand1Inscription, OffHand1Inscription, MainHand2Inscription, OffHand2Inscription,
                MainHand1Sigil, OffHand1Sigil, MainHand2Sigil, OffHand2Sigil) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
    c.execute(insert, (PvEWeaponsObjectID, mh1, oh1, mh2, oh2, mh1i, oh1i, mh2i, oh2i, mh1s, oh1s, mh2s, oh2s))
    conn.commit()
