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
    if height == 1:
        return 2
    else:
        if num_of_towers % 2 == 0:
            return 2
        else:
            return 1
                
    

def main():
    print(towerBreakers(2, 6))
    print(towerBreakers(1, 4))
    
main()