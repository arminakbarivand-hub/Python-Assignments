n = int(input("enter a number: "))
yekan = n % 10
dahgan = n // 10
sum_numbers = yekan + dahgan
reverse = int(str(yekan)+str(dahgan))

print(f"sum : {sum_numbers}\nreverse : {reverse}")