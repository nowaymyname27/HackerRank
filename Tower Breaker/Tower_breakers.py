#
# Complete the 'towerBreakers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def towerBreakers(n, m):
    num_of_towers = n
    height = m
    y = height - 1
    setup = []
    player = 1
    for num in range(num_of_towers):
        setup.append(height)
    for i in range(len(setup)):
        while True:
            if height % y == 0:
                height -= y
                y = height - 1
                if height > 1 and player == 1:
                    player = 2
                elif height > 1 and player == 2:
                    player = 1
                else:
                    break
            else:
                y -= 1
    return player
                
    

def main():
    print(towerBreakers(2, 6))
    print(towerBreakers(1, 4))
    
main()