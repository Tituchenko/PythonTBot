battleLog='battle.csv'


def saveBattle(Battle):
    global battleLog
    with open (battleLog,'a',encoding='UTF-8') as f:
        f.write(Battle)
def loadBattle():
    global battleLog
    try:
        with open (battleLog,'r',encoding='UTF-8') as f:
            str=f.readlines()
    except:
        return False
    return str
