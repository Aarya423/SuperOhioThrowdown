import random
        
class Fighter:
    def __init__(self, stats, moveset, expTot, fileName, name):
        self.expTot = expTot
        self.level = findLevel(self.expTot)
        self.baseAtk = stats[0]
        self.baseDfs = stats[1]
        self.baseSpd = stats[2]
        self.baseHp = stats[3]
        self.atk = (stats[0] // 20 + 1) * self.level
        self.dfs = (stats[1] // 20 + 1) * self.level
        self.spd = (stats[2] // 20 + 1) * self.level
        self.hp = (stats[3] // 20 + 1) * self.level
        self.accuracy = 1.0
        self.tempAcc = self.accuracy
        self.tempAtk = self.atk
        self.tempDfs = self.dfs
        self.tempSpd = self.spd
        self.tempHp = self.hp

        self.usedBlockLast = False
        self.isProtected = False
        self.isChargingUp = True
        self.turnsOfChipLeft = 0
        
        self.move1bp = moveset[0][0]
        self.move1acc = moveset[0][1]
        self.move1pp = moveset[0][2]
        self.move1effect = moveset[0][3]
        self.move1priority = moveset[0][4]
        self.move1learnLvl = moveset[0][5]
        self.move1name = moveset[0][6]

        self.move2bp = moveset[1][0]
        self.move2acc = moveset[1][1]
        self.move2pp = moveset[1][2]
        self.move2effect = moveset[1][3]
        self.move2priority = moveset[1][4]
        self.move2learnLvl = moveset[1][5]
        self.move2name = moveset[1][6]
        
        self.move3bp = moveset[2][0]
        self.move3acc = moveset[2][1]
        self.move3pp = moveset[2][2]
        self.move3effect = moveset[2][3]
        self.move3priority = moveset[2][4]
        self.move3learnLvl = moveset[2][5]
        self.move3name = moveset[2][6]
        
        self.move4bp = moveset[3][0]
        self.move4acc = moveset[3][1]
        self.move4pp = moveset[3][2]
        self.move4effect = moveset[3][3]
        self.move4priority = moveset[3][4]
        self.move4learnLvl = moveset[3][5]
        self.move4name = moveset[3][6]

        self.move1TempPP = self.move1pp
        self.move2TempPP = self.move2pp
        self.move3TempPP = self.move3pp
        self.move4TempPP = self.move4pp

        self.imageSource = fileName
        self.fighterName = name

        self.fighterName = name

    def reset(self):
        self.accuracy = 1.0
        self.tempAcc = self.accuracy
        self.tempAtk = self.atk
        self.tempDfs = self.dfs
        self.tempSpd = self.spd
        self.tempHp = self.hp
        self.move1TempPP = self.move1pp
        self.move2TempPP = self.move2pp
        self.move3TempPP = self.move3pp
        self.move4TempPP = self.move4pp
    
    def afterWin(self, expTot):
        self.expTot = expTot
        self.level = findLevel(self.expTot)
        self.atk = (self.baseAtk // 20 + 1) * self.level
        self.dfs = (self.baseDfs // 20 + 1) * self.level
        self.spd = (self.baseSpd // 20 + 1) * self.level
        self.hp = (self.baseHp // 20 + 1) * self.level

    def getLevel(self):
        return self.level

    def replaceMove(self, moveToReplace):
        # user picks move to replace, move position is assigned to moveSelected, cancel button = 0
        moveSelected = 5
        if moveSelected == 0:
            moveSelected #do the update thingy to resume to game
        elif moveSelected == 1:
            self.move1 = moveToReplace
        elif moveSelected == 2:
            self.move2 = moveToReplace
        elif moveSelected == 3:
            self.move3 = moveToReplace
        elif moveSelected == 4:
            self.move4 = moveToReplace

def findLevel(expTot):
    level =  0
    level = expTot // 1000
    return (level)

lebronStats = [85, 75, 60, 70]
obamaStats = [45, 120, 120, 25]
luffyStats = [50, 90, 90, 60]
ohmStats = [100, 100, 100, 100]
emStats = [70, 100, 50, 20]
bruceStats = [90, 45, 45, 110]
jackStats = [110, 50, 40, 70]
sharkStats = [100, 30, 60, 70]
bearStats = [40, 140, 80, 40]
gruntStats = [40, 40, 40, 40]


"""
Effects list (to implement later)
1 - The user runs with high speeds and blocks the enemies attack, this move has priority. If this move is repeated consecutively, its accuracy is halved. 
2 - The user sings with such confidence putting the opponent in a dream-like state causing them to fall asleep.
3 - Increases attack stat by 1 stage - maxes out at 6
4 - This move has a 20% chance of lowering the opponents defense by 1 stage. 
"""

def speedCalc(p1, p2, move1Speed, move2Speed):
    if (p1 == p2):
        if (move1Speed > move2Speed):
            return True
        elif (move1Speed == move2Speed):
            speedTie = random.randint(1,2)
            if speedTie == 1:
                return True
            elif speedTie == 2:
                return False
        elif (move1Speed < move2Speed):
            return False
    elif (p1 > p2):
        return True
    elif (p1 < p2):
        return False

def damageCalc(A, P, L, D):
    rng = random.randint(1,100)
    if rng > 95:
        criticalHit = 1.5
    else:
        criticalHit = 1
    if (P > 0):
        damage = ((((((2 * L) / 5) + 2) * P * (A / D)) / 50) + 2) * criticalHit
        damage = round(damage)
    else:
        damage = 0
    print(damage)
    return damage