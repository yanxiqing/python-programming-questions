# Modify the previous program such that only multiples of three or five are considered in the sum

if __name__=="__main__":
    num =int(input('please write a number:\n'))
    total = 0
    for i in range(1, num+1):
        if i % 3 ==0 or i % 5 ==0:
            total += i
            print(i)
    print(total)