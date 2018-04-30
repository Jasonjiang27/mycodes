#PingPongMatchAnalysis.py

from random import random
def getInputs():
    a = eval(input("请输入选手张继科的能力值（0-1）:"))
    b = eval(input("请输入选手马龙的能力值（0-1）:"))
    n = eval(input("模拟比赛的场次："))
    return a,b,n


def simNGames(n,probA,probB):
    winsA,winsB = 0,0
    for i in range(n):
        scoreA,scoreB = simOneGame(probA,probB)
        if scoreA > scoreB:
            winsA+=1
        else:
            winsB+=1
    return winsA,winsB

def gameover(scoreA,scoreB):
    return scoreA == 11 or scoreB == 11


def simOneGame(probA,probB):
    scoreA,scoreB = 0,0
    score = scoreA+scoreB
    while not gameover(scoreA,scoreB):
        if (score//2)%2 ==0:  #总比分每加两分，转换发球权
            serving = "A"
            if random() < probA:
                scoreA += 1
            else:
                scoreB += 1 
        else:
            serving = "B"
            if random() < probB:
                scoreB += 1
            else:
                scoreA +=1
           
    return scoreA, scoreB


def printSummary(winsA, winsB):
    n = winsA+winsB
    print("竞技分析开始，共模拟{}场比赛".format(n))
    print("选手张继科获胜{}场比赛，占比{:.1%}".format(winsA, winsA/n))
    print("选手马龙获胜{}场比赛，占比{:.1%}".format(winsB, winsB/n))


def main():
    probA, probB, n = getInputs()
    winsA,winsB = simNGames(n, probA, probB)#获胜场次函数
    
    printSummary(winsA, winsB)


main()
