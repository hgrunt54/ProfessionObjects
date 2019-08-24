import db

conn = db.connect()
c = conn.cursor()

# ------------------THE FOLLOWING CODE IS FOR THE ProfessionObject Module-------------------------

# get the current highest Primary Key number for tbl_BuildNames
def getbuildNameID():
    maxbnid = '''SELECT MAX(BuildNameID) FROM tbl_BuildNames'''
    c.execute(maxbnid)
    a = c.fetchone()
    bnid = a[0] + 1
    return bnid

# functions to get the BuildNameID, ProfessionID, and the GameModeID to insert into the addProfessionObject
def buildNameID():
    BuildNameID = '''SELECT MAX(BuildNameID) FROM tbl_BuildNames'''
    c.execute(BuildNameID)
    a = c.fetchone()
    bnid = a[0]
    return bnid

# create counter function for Professions
def professionCounter():
    profCount = '''SELECT * FROM tbl_Professions'''
    c.execute(profCount)
    profCounter = len(c.fetchall())
    return profCounter

# get the currently highest Primary Key number for tbl_ProfessionObjects and add 1 to insert a new row
def getProfessionObjectID():
    maxpoid = '''SELECT MAX(ProfessionObjectID) FROM tbl_ProfessionObjects'''
    c.execute(maxpoid)
    a = c.fetchone()
    poid = a[0] + 1
    return poid

# generate the dropdown list for Professions
def getProfession():
    profList = []
    x = 0
    j = professionCounter()
    query1 = '''SELECT Profession FROM tbl_Professions'''
    c.execute(query1)
    while x < j:
        prof = c.fetchone()
        profList.append(prof[0])
        x += 1
    return profList

def ProfessionID(profession):
    ProfessionID = '''SELECT ProfessionID FROM tbl_Professions WHERE Profession IS ?'''
    c.execute(ProfessionID, (profession,))
    a = c.fetchone()
    pid = a[0]
    return pid

# create counter function for Game Modes
def gameModeCounter():
    gameModeCount = '''SELECT * FROM tbl_GameModes'''
    c.execute(gameModeCount)
    gameModeCounter = len(c.fetchall())
    return gameModeCounter

# generate the drop down list for Game Modes
def getGameMode():
    GameModeList = []
    x = 0
    j = gameModeCounter()
    query1 = '''SELECT GameMode FROM tbl_GameModes'''
    c.execute(query1)
    while x < j:
        gameMode = c.fetchone()
        GameModeList.append(gameMode[0])
        x += 1
    return GameModeList

def GameModeID(gameMode):
    GameModeID = '''SELECT GameModeID FROM tbl_GameModes WHERE GameMode IS ?'''
    c.execute(GameModeID, (gameMode,))
    a = c.fetchone()
    gmid = a[0]
    return gmid

# Functions that work with the Build Type drop down
def buildTypeCount():
    btCount = '''SELECT * FROM tbl_BuildTypes'''
    c.execute(btCount)
    btCounter = len(c.fetchall())
    return btCounter

def getbuildTypeID(buildType):
    BuildTypeID = '''SELECT BuildTypeID FROM tbl_BuildTypes WHERE BuildType is ?'''
    c.execute(BuildTypeID, (buildType,))
    a = c.fetchone()
    bnid = a[0]
    return bnid

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

# insert into the ProfessionObject data into the ProfessionObjects table
def addProfessionObject(profession, gameMode, buildType):
    poid = getProfessionObjectID()
    bnid = buildNameID()
    pid = ProfessionID(profession)
    gmid = GameModeID(gameMode)
    btid = getbuildTypeID(buildType)
    insert = '''INSERT INTO tbl_ProfessionObjects (ProfessionObjectID, BuildNameID, ProfessionID, GameModeID, BuildTypeID) VALUES (?, ?, ?, ?, ?)'''
    c.execute(insert, (poid, bnid, pid, gmid, btid))
    conn.commit()

# insert the Build's Name into the BuildNames table
def addBuildName(buildName):
    x = getbuildNameID()
    insert = '''INSERT INTO tbl_BuildNames (BuildNameID, BuildName) VALUES (?, ?)'''
    c.execute(insert, (x, buildName))
    conn.commit()


#-------------THE FOLLOWING CODE IS FOR THE ArmorObject Module-----------------
