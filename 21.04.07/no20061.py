blue = [[0 for _ in range(6)] for _ in range(4)]
green = [[0 for _ in range(4)] for _ in range(6)]

def drop_green(t, y):
    x = 0
    if t == 1 or t == 3:
        for i in range(6):
            if green[i][y] == 1:
                break
            x += 1
        x -= 1
        green[x][y] = 1
        if t == 3:
            green[x-1][y] = 1
    else:
        for i in range(6):
            if green[i][y] == 1 or green[i][y+1] == 1:
                break
            x += 1
        x -= 1
        green[x][y] = 1
        green[x][y+1] = 1

def drop_blue(t,x):
    y = 0
    if t == 1 or t == 2:
        for j in range(6):
            if blue[x][j] == 1:
                break
            y += 1
        y -= 1
        blue[x][y] = 1
        if t == 2:
            blue[x][y-1] = 1
    else:
        for j in range(6):
            if blue[x][j] == 1 or blue[x+1][j] == 1:
                break
            y += 1
        y -= 1
        blue[x][y] = 1
        blue[x+1][y] = 1

def check():
    global answer
    for i in range(2,6):
        cnt = 0
        for j in range(4):
            if green[i][j] == 1:
                cnt += 1
        
        if cnt == 4:
            # print(cnt)
            # print(green)
            # print('after{}'.format(i))
            remove('green',i)
            answer += 1

    for j in range(2,6):
        cnt = 0
        for i in range(4):
            if blue[i][j] == 1:
                cnt += 1
        if cnt == 4:
            remove('blue',j)
            answer += 1


def remove(color,index):
    if color == 'green':
        for i in range(index,-1,-1):
            if i == 0:
                for j in range(4):
                    green[i][j] = 0
                return
            for j in range(4):
                green[i][j] = green[i-1][j]
    else:
        for j in range(index,-1,-1):
            if j == 0:
                for i in range(4):
                    blue[i][j] = 0
                return
            for i in range(4):
                blue[i][j] = blue[i][j-1]

def check_light_area():
    for i in range(2):
        for j in range(4):
            if green[i][j] == 1:
                remove('green',5)
                break
    for j in range(2):
        for i in range(4):
            if blue[i][j] == 1:
                remove('blue',5)
                break

n = int(input())
answer = 0
for _ in range(n):
    t,x,y = map(int,input().split())

    drop_green(t,y)
    drop_blue(t,x)

    check()
    check_light_area()

blockcnt = 0
for i in range(2,6):
    for j in range(4):
        if green[i][j] == 1:
            blockcnt += 1
for i in range(4):
    for j in range(2,6):
        if blue[i][j] == 1:
            blockcnt += 1

print(answer)
print(blockcnt)