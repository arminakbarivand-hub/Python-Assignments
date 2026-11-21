num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
if -1000 <= num1 <= 1000 and -1000 <= num2 <= 1000 and -1000 <= num3 <= 1000 and -1000 <= num4 <= 1000 : 
    sum = num1 + num2 + num3 + num4
    average = sum / 4
    mul = num1 * num2 * num3 * num4
    list = [num1,num2,num3,num4]
    
    print(f"Sum : {sum:.6f}")
    print(f"Average : {average:.6f}")
    print(f"Product : {mul:.6f}")
    print(f"MAX : {max(list):.6f}")
    print(f"MIN : {min(list):.6f}")