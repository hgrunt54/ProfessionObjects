#!/user/bin/env/python3
# This module is meant for creating the ProfessionObjects for the ProfressionObjects frame section.
class ProfessionObject:
    def __init__(self, bnid=0, pid=0, gmid=0):
        self.bnid = bnid
        self.pid = pid
        self.gmid = gmid

class BuildName:
    def __init__(self, bnid=0, bn=None):
        self.bnid = bnid
        self.bn = bn

class Profession:
    def __init__(self, pid=0, p=None):
        self.pid = pid
        self.p = p

class GameMode:
    def __init__(self, gmid=0, gm=None):
        self.gmid = gmid
        self.gm = gm

