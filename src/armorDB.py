#!user/bin/env/python3
# This module is used for creating the SQL code that will be used in the ArmorObjectUI
import sqlite3
from contextlib import closing

# connect to the database
sqliteFile = './../Test.db'
conn = sqlite3.connect(sqliteFile)
c = conn.cursor()

# Counter for the insignias
def insigniaPvPCount():
    insigCount = '''SELECT * FROM tbl_Insignias
                    WHERE PvP IS 1 AND Active IS 1'''
    c.execute(insigCount)
    insigCounter = len(c.fetchall())
    return insigCounter

def insigniaPvECount():
    insigCount = '''SELECT * FROM tbl_Insignias
                    WHERE PvE IS 1 AND Active IS 1'''
    c.execute(insigCount)
    insigCounter = len(c.fetchall())
    return insigCounter

def getPvPInsignias():
    insigList = []
    x = 0
    j = insigniaPvPCount()
    query1 = '''SELECT Insignia FROM tbl_Insignias
                WHERE PvP IS 1 AND Active IS 1'''
    c.execute(query1)
    while x < j:
        insig = c.fetchone()
        insigList.append(insig[0])
        x += 1
    return insigList

def getPvEInsignias():
    insigList = []
    x = 0
    j = insigniaPvECount()
    query1 = '''SELECT Insignia FROM tbl_Insignias
                WHERE PvE IS 1 AND Active IS 1'''
    c.execute(query1)
    while x < j:
        insig = c.fetchone()
        insigList.append(insig[0])
        x += 1
    return insigList

def getInsigniaID(insignia):
    insigniaID = '''SELECT InsigniaID FROM tbl_Insignias WHERE Insignia IS ?'''
    c.execute(insigniaID, (insignia,))
    a = c.fetchone()
    insigid = a[0]
    return insigid

# Counter for the Runes
def runePvPCount():
    runeCount = '''SELECT * FROM tbl_Runes
                    WHERE PvP IS 1 AND Active IS 1'''
    c.execute(runeCount)
    runeCounter = len(c.fetchall())
    return runeCounter

def runePvECount():
    runeCount = '''SELECT * FROM tbl_Runes
                    WHERE PvE IS 1 AND Active IS 1'''
    c.execute(runeCount)
    runeCounter = len(c.fetchall())
    return runeCounter

# Generate list for Runes drop down
def getPvPRunes():
    runeList = []
    x = 0
    j = runePvPCount()
    query1 = '''SELECT Rune FROM tbl_Runes
                WHERE PvP IS 1 AND Active IS 1'''
    c.execute(query1)
    while x < j:
        rune = c.fetchone()
        runeList.append(rune[0])
        x += 1
    return runeList

def getPvERunes():
    runeList = []
    x = 0
    j = runePvECount()
    query1 = '''SELECT Rune FROM tbl_Runes
                WHERE PvE IS 1 AND Active IS 1'''
    c.execute(query1)
    while x < j:
        rune = c.fetchone()
        runeList.append(rune[0])
        x += 1
    return runeList

def getRuneID(rune):
    RuneID = '''SELECT RuneID FROM tbl_Runes WHERE Rune is ?'''
    c.execute(RuneID, (rune,))
    a = c.fetchone()
    rid = a[0]
    return rid

def getPvPArmorObjectID():
    maxPvPAOid = '''SELECT MAX(PvPArmorObjectID) FROM tbl_PvPArmorObjects'''
    c.execute(maxPvPAOid)
    a = c.fetchone()
    PvPAOid = a[0] + 1
    return PvPAOid

def getPvEArmorObjectID():
    maxPvEAOid = '''SELECT MAX(PvEArmorObjectID) FROM tbl_PvEArmorObjects'''
    c.execute(maxPvEAOid)
    a = c.fetchone()
    PvEAOid = a[0] + 1
    return PvEAOid

def addPvPArmorObject(insignia, rune):
    PvPArmorObjectID = getPvPArmorObjectID()
    insigniaID = getInsigniaID(insignia)
    runeID = getRuneID(rune)
    insert = '''INSERT INTO tbl_PvPArmorObjects (PvPArmorObjectID, InsigniaID, RuneID) VALUES (?, ?, ?)'''
    c.execute(insert, (PvPArmorObjectID, insigniaID, runeID))
    conn.commit()

def addPvEArmorObject(hI, sI, cI, gI, pI, bI, hR, sR, cR, gR, pR, bR):
    PvEArmorObjectID = getPvEArmorObjectID()
    insert = '''INSERT INTO tbl_PvEArmorObjects (PvEArmorObjectID, HeadInsignia, ShoulderInsignia,
                ChestInsignia, GlovesInsignia, PantsInsignia, BootsInsignia, HeadRune, ShoulderRune, ChestRune,
                GlovesRune, PantsRune, BootsRune) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
    c.execute(insert, (PvEArmorObjectID, hI, sI, cI, gI, pI, bI, hR, sR, cR, gR, pR, bR))
    conn.commit()
