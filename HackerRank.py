

t = divmod(int(input()), int(input()))
print(t[0])
print(t[1])
print(t)


for i in range(1, int(input())+1):
    print((10**i//9)**2)

# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    n = int(input())

for i in range(1, n + 1):
    if i == n:
        for j in range(n):
            print(n - j, end="")
    else:
        print(i, end="")