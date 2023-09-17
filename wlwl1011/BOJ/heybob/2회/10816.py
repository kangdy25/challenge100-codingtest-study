import sys, os, io, atexit
input = lambda : sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s : stdout.write(s.encode("ascii"))
atexit.register(lambda : os.write(1, stdout.getvalue()))

N = int(input())
arr = list(map(int, input().split()))
dictionary = dict()
for i in arr:
    if i in dictionary:
        dictionary[i] +=1
    else:
        dictionary[i] = 1    
M = int(input())
check = list(map(int, input().split()))
answer = []
for i in check:
    if i in dictionary:
        answer.append(dictionary[i])
    else:
        answer.append(0)    

print(*answer)