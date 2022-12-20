# Создайте программу для игры с конфетами человек против компьютера.
# Условие задачи: На столе лежит 150 конфет. Играют игрок против компьютера. Первый ход определяется жеребьёвкой.За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Подумайте как наделить бота ""интеллектом""
from random import choice,randint
import candy_conf
import datetime as dt

import log

candyOnTable=candy_conf.candyOnTable_base
maxCanTake=candy_conf.maxCanTake_base
round=1
firstTurnComp=0
Error=''
StartTime=''
EndTime=''
Battle=[]

def getFirstTurnComp():
    global firstTurnComp
    return firstTurnComp

def getError():
    global Error
    return Error

def checkMessage(text):
    global maxCanTake, Error, candyOnTable
    if text.isdigit():
        if int(text) in range(1,maxCanTake+1):
            if not int(text)>candyOnTable:
                Error = 'Столько конфет нет на столе!'
            return True
        else:
            Error = f'Нельзя брать больше {maxCanTake}!'

    else:
        Error='Введите число!'
    return False

def checkWin():
    global round,candyOnTable,maxCanTake,EndTime
    if candyOnTable==0:
        EndTime=dt.datetime.now().replace(microsecond=0)
        candyOnTable = candy_conf.candyOnTable_base
        maxCanTake = candy_conf.maxCanTake_base

        return True
    else:
        return False

def getHumanTurn (numTurn):
    global candyOnTable
    candyOnTable-=numTurn


def getCompTurn ():
    global candyOnTable, maxCanTake,round,firstTurnComp
    if candyOnTable<=maxCanTake:
        turn=candyOnTable
    else:
        turn=candyOnTable%(maxCanTake+1)
    if turn==0:
        turn=randint(1,maxCanTake+1)
    candyOnTable -= turn
    tips=''
    if firstTurnComp:
        tips=f' (Осталось - {candyOnTable})'
    return f'{turn}{tips}'

def info()->str:
    global round, candyOnTable,maxCanTake
    str=f'Ход {round}. На столе {candyOnTable} конфет. Сколько заберете? (max={maxCanTake}):'
    round+=1
    return str

def whosFirst(name:str,user_id)->str:
    global firstTurnComp,StartTime,round,Battle
    stringBattle=log.loadBattle()
    infoBatle=''
    if stringBattle:
        getBattleFromLog(stringBattle)
        infoBatle=getNumberMatch(user_id)
    round = 1
    StartTime=dt.datetime.now().replace(microsecond=0)
    firstTurnComp=choice([0,1])
    if firstTurnComp==1:
        name='bot'
    return f'{infoBatle}Жеребьевка определила, что первый ходит {name}'
def getStrToLog(user_id,who):
    global StartTime,EndTime,round,Battle

    return f'{int(Battle[-1][0])+1};{user_id};{StartTime};{EndTime};{round-1};{who}\n'

def getBattleFromLog(str):
    global Battle
    Battle.clear()
    for s in str:
        Battle.append(s.replace('\n','').split(';'))
    return Battle

def getNumberMatch(user_id):
    global Battle
    count=0
    win=0
    lose=0
    rounds=0
    for b in Battle:
        if int(b[1])==user_id:
            count+=1
            rounds+=int(b[4])
            if b[5]=='bot':
                lose+=1
            else:
                win+=1
    aver=''
    if count>0:
        aver=f'Среднее количество раундов {rounds//count}'

    str=f'Это наша битва №{count+1}. Счет ({win}/{lose}) Вы/бот.{aver}\n'
    return str