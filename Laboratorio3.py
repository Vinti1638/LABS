def knapsack(W, weight, cost, n): 
    K = [[0 for x in range(W + 1)] for x in range(n + 1)] 
    for i in range(n + 1): 
        for w in range(W + 1): 
            if i == 0 or w == 0: 
                K[i][w] = 0 
            elif weight[i - 1] <= w: 
                K[i][w] = max(cost[i - 1][0] + K[i - 1][w - weight[i - 1]], K[i - 1][w]) 
            else: 
                K[i][w] = K[i - 1][w] 
    return K 
 
 
stuffdict = {'в': (3, 25, 0), 
             'п': (2, 15), 
             'б': (2, 15), 
             'а': (2, 20), 
             'н': (1, 15), 
             'т': (3, 20), 
             'о': (1, 25), 
             'ф': (1, 15), 
             'д': (1, 10), 
             'к': (2, 20), 
             'р': (2, 20) 
             } 
 
backpack = {} 
 
 
Y = [] 
X = [] 
for key in stuffdict: 
    Y.append([stuffdict[key][1], key]) 
    X.append(stuffdict[key][0]) 
 
W = 8 
n = len(Y) 
K = knapsack(W, X, Y, n) 
 
 
w, i, total_weight = W, n, 0 
res = K[n][W] 
while i > 0 and res > 0: 
    if res != K[i - 1][w]: 
        backpack[Y[i - 1][1]] = [Y[i - 1][0], X[i - 1]] 
        stuffdict.pop(Y[i - 1][1]) 
        total_weight += X[i - 1] 
        res -= Y[i - 1][0] 
        w -= X[i - 1] 
    i -= 1 
 
 
L = 0 
for key in backpack: 
    for k in range(backpack[key][1]): 
        if L == 2: 
            print("\b\b") 
            L = 0 
        print(key, end=', ') 
        L += 1 
 
start = 15 
s = 0 
for key in stuffdict: 
    s += stuffdict[key][1] 
print(' ') 
itog = K[n][W] - s + start 
print("Итоговые очки выживания: ", itog) 
if itog > 0: 
    print('Том будет жить') 
else: 
    ('Том умрёт в муках') 
 
 
 
 
print('Доп задание') 
def knapsack(W, weight, cost, n): 
    K = [[0 for x in range(W + 1)] for x in range(n + 1)] 
    for i in range(n + 1): 
        for w in range(W + 1): 
            if i == 0 or w == 0: 
                K[i][w] = 0 
            elif weight[i - 1] <= w: 
                K[i][w] = max(cost[i - 1][0] + K[i - 1][w - weight[i - 1]], K[i - 1][w]) 
            else: 
                K[i][w] = K[i - 1][w] 
    return K 
 
 
stuffdict = {'в': (3, 25, 0), 
             'п': (2, 15), 
             'б': (2, 15), 
             'а': (2, 20), 
             'н': (1, 15), 
             'т': (3, 20), 
             'о': (1, 25), 
             'ф': (1, 15), 
             'д': (1, 10), 
             'к': (2, 20), 
             'р': (2, 20) 
             } 
 
backpack = {} 
 
 
Y = [] 
X = [] 
for key in stuffdict: 
    Y.append([stuffdict[key][1], key]) 
    X.append(stuffdict[key][0]) 
 
W = 7 
n = len(Y) 
K = knapsack(W, X, Y, n) 
 
 
w, i, total_weight = W, n, 0 
res = K[n][W] 
while i > 0 and res > 0: 
    if res != K[i - 1][w]: 
        backpack[Y[i - 1][1]] = [Y[i - 1][0], X[i - 1]] 
        stuffdict.pop(Y[i - 1][1]) 
        total_weight += X[i - 1] 
        res -= Y[i - 1][0] 
        w -= X[i - 1] 
    i -= 1 
 
 
L = 0 
for key in backpack: 
    for k in range(backpack[key][1]): 
        if L == 7: 
            print("\b\b") 
            L = 0 
        print(key, end=', ') 
        L += 1 
 
start = 15 
s = 0 
for key in stuffdict: 
    s += stuffdict[key][1] 
print(' ') 
itog = K[n][W] - s + start 
print("Итоговые очки выживания: ", itog) 
if itog > 0: 
    print('Том будет жить') 
else: 
    ('Том умрёт в муках')