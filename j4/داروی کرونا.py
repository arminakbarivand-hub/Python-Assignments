n = int(input())
k = int(input())
p = int(input())
q = int(input())
if 1 <= k <= n <= 1000:
    if 1 <= q <= p <= 1000:
        if (n - k) > (p - q) : print ("Shekarestan")
        elif (p - q) > (n - k) : print("Namakestan")
        else : print("Equal")
    else : print("enter valid numbers")
else : print("enter valid numbers")
