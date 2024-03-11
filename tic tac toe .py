

print("Welcome to Tic Toc Toe Game!")


def printchart(xlist,zlist):
    zero = 'x' if xlist[0] else('0' if zlist[0] else 0)
    one = 'x' if xlist[1] else('0' if zlist[1] else 1)
    two = 'x' if xlist[2] else('0' if zlist[2] else 2)
    three = 'x' if xlist[3] else('0' if zlist[3] else 3)
    four = 'x' if xlist[4] else('0' if zlist[4] else 4)
    five = 'x' if xlist[5] else('0' if zlist[5] else 5)
    six = 'x' if xlist[6] else('0' if zlist[6] else 6)
    seven = 'x' if xlist[7] else('0' if zlist[7] else 7)
    eight = 'x' if xlist[8] else('0' if zlist[8] else 8)
    print(f"{zero}|{one}|{two}")
    print(f"-|-|-")
    print(f"{three}|{four}|{five}")
    print(f"-|-|-")
    print(f"{six}|{seven}|{eight}")
    


def checkwins(xlist , zlist):
    winlist = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in winlist:
        if xlist[win[0]]+xlist[win[1]]+xlist[win[2]] == 3:
            print("X won the game")
            return 1
    if zlist[win[0]]+zlist[win[1]]+zlist[win[2]] == 3:
            print("0 won the game")
            return 0
        
    return -1
            


xlist = [0,0,0,0,0,0,0,0,0]
zlist = [0,0,0,0,0,0,0,0,0]
turn = 1
while(True):
    printchart(xlist,zlist)
    if(turn == 1):
        print("Now a X'Chance ")
        value = int(input("Enter any value"))
        xlist[value] = 1
    else:
        print("Now a 0'Chance ")
        value = int(input("Enter any value"))
        zlist[value] = 1
    turn = 1-turn
    y = checkwins(xlist,zlist)
    if y!=-1:
        print("Game is over")
        break




        





