n,k = map(int,input().split())
a = list(map(int,input().split()))
arr = ['A','B','C','D']
abc = {}
main = []
for j in range(4):
    abc[arr[j]] = a[j]
card = []
for i in range(n):
    t,u = input().split()
    u = int(u)
    card.append([t,u])
card.sort(key = lambda x : (x[0],-x[1]))
for i in card:
    main.append([i[0],i[1],(i[1] / abc[i[0]])])
    abc[i[0]] += i[1]
main.sort(key = lambda x : (-x[2]))
for i in range(k):
    print(main[i][0],main[i][1])