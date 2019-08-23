#!user/bin/env/python3
# This module is used for creating the SQL code that will be used in the ArmorObjectUI
import sqlite3
from contextlib import closing

# connect to the database
sqliteFile = 'C:/SQLite/Databases/Test.db'
conn = sqlite3.connect(sqliteFile)
c = conn.cursor()

# Counter for BuildTypes
def buildTypeCount():
    btCount = '''SELECT * FROM tbl_BuildTypes'''
    c.execute(btCount)
    btCounter = len(c.fetchall())
    return btCounter

# Counter for the insignias
def insigniaPvPCount():
    insigCount = '''SELECT * FROM tbl_Insignias
                    WHERE PvP IS 1'''
    c.execute(insigCount)
    insigCounter = len(c.fetchall())
    return insigCounter

def insigniaPvECount():
    insigCount = '''SELECT * FROM tbl_Insignias
                    WHERE PvE IS 1'''
    c.execute(insigCount)
    insigCounter = len(c.fetchall())
    return insigCounter

# Counter for the Runes
def runePvPCount():
    runeCount = '''SELECT * FROM tbl_Runes
                    WHERE PvP IS 1'''
    c.execute(runeCount)
    runeCounter = len(c.fetchall())
    return runeCounter

def runePvECount():
    runeCount = '''SELECT * FROM tbl_Runes
                    WHERE PvE IS 1'''
    c.execute(runeCount)
    runeCounter = len(c.fetchall())
    return runeCounter

# Building the list for the BuildType dropdown
def getBuildTypes():
    btList = []
    x = 0
    j = buildTypeCount()
    query1 = '''SELECT BuildType FROM tbl_BuildTypes'''
    c.execute(query1)
    while x < j:
        bt = c.fetchone()
        btList.append(bt[0])
        x += 1
    return btList

# Generate list for Insignias drop down
def getPvPInsignias():
    insigList = []
    x = 0
    j = insigniaPvPCount()
    query1 = '''SELECT Insignia FROM tbl_Insignias
                WHERE PvP IS 1'''
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
                WHERE PvE IS 1'''
    c.execute(query1)
    while x < j:
        insig = c.fetchone()
        insigList.append(insig[0])
        x += 1
    return insigList

# Generate list for Runes drop down
def getPvPRunes():
    runeList = []
    x = 0
    j = runePvPCount()
    query1 = '''SELECT Rune FROM tbl_Runes
                WHERE PvP IS 1'''
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
                WHERE PvE IS 1'''
    c.execute(query1)
    while x < j:
        rune = c.fetchone()
        runeList.append(rune[0])
        x += 1
    return runeList

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

def getbuildTypeID(buildType):
    BuildTypeID = '''SELECT BuildTypeID FROM tbl_BuildTypes WHERE BuildType is ?'''
    c.execute(BuildTypeID, (buildType,))
    a = c.fetchone()
    bnid = a[0]
    return bnid

def getInsigniaID(insignia):
    insigniaID = '''SELECT InsigniaID FROM tbl_Insignias WHERE Insignia is ?'''
    c.execute(insigniaID, (insignia,))
    a = c.fetchone()
    insigid = a[0]
    return insigid

def getRuneID(rune):
    RuneID = '''SELECT RuneID FROM tbl_Runes WHERE Rune is ?'''
    c.execute(RuneID, (rune,))
    a = c.fetchone()
    rid = a[0]
    return rid

def addPvPArmorObject(buildType, insignia, rune):
    PvPArmorObjectID = getPvPArmorObjectID()
    buildTypeID = getbuildTypeID(buildType)
    insigniaID = getInsigniaID(insignia)
    runeID = getRuneID(rune)
    insert = '''INSERT INTO tbl_PvPArmorObjects (PvPArmorObjectID, BuildTypeID, InsigniaID, RuneID) VALUES (?, ?, ?, ?)'''
    c.execute(insert, (PvPArmorObjectID, buildTypeID, insigniaID, runeID))
    conn.commit()

def addPvEArmorObject(buildType, hI, sI, cI, gI, pI, bI, hR, sR, cR, gR, pR, bR):
    PvEArmorObjectID = getPvEArmorObjectID()
    buildTypeID = getbuildTypeID(buildType)
    insert = '''INSERT INTO tbl_PvEArmorObjects (PvEArmorObjectID, BuildTypeID, HeadInsignia, ShoulderInsignia, 
                ChestInsignia, GlovesInsignia, PantsInsignia, BootsInsignia, HeadRune, ShoulderRune, ChestRune,
                GlovesRune, PantsRune, BootsRune) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
    c.execute(insert, (PvEArmorObjectID, buildTypeID, hI, sI, cI, gI, pI, bI, hR, sR, cR, gR, pR, bR))
    conn.commit()