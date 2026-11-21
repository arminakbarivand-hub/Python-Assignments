X = int(input())
N = int(input())
if 0 <= X <= 20 and 0 <= N <= 100:
    if N == 0 : print(20)
    elif N == 7 : print(X)
    else : 
        Answer = X - N
        if Answer < 0:
            Answer = 0
        print(Answer)