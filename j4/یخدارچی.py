T = int(input())
if -273 <= T <= 6000 :
    if T <= 0 : print("Ice")
    elif 0 < T <= 100 : print("Water")
    else : print("Steam")
else: print()