t = int(input())
for _ in range(t):
    n = int(input())
    array = [abs(int(x)) for x in input().split()]
    print(sum(array))