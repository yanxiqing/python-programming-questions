# Write a program that asks the uses for a number and gives him the possbility to choose between computing the sum and compting the product of 1 to n
import sys

if __name__ =="__main__":
    num = int(input("please the write a number:\n"))
    col = input(" '+' or '*':\n")
    if col == '+':
        s = 0
        s = sum(range(1, num+1))
        print(s)
    elif col == '*':
        ans =1
        for j in range(1, num+1):
            ans *= j
        print(ans)