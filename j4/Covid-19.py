p = int(input())
q = int(input())
if 0 <= p <= 1000 and 0 <= q <= 500 and q <= p:
    if p <= 50 and q <= 10:
        print("White")
    elif q > 30:
        print ("Red")
    else: 
        print("Yellow")