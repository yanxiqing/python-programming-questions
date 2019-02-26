# write a program that asks the user for a number n and prints the sum of the numbers 1 tp n
if __name__ == "__main__":
    num = int(input('please write a number: \n'))
    total = 0
    for i in range(1 , num+1):
        total += i
    print(total)