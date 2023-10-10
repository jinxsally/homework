#分析原岸的状态，只能为10种
left = [['狼',1],['羊',1],['菜',1]]
right = [['狼',0],['羊',0],['菜',0]]#保存两岸的状态
l = len(left)#计算可行性的个数
count = 0#计算步数
number = -1

def judge(left):#判断能不能共存
    if left[1][1]==1 and left[0][1] + left[2][1] == 1:#判断羊能不能与其他两个共存
        return False
    else:
        return True
def left_to_right():
    global number
    global count
    for i in range(l):
        if left[i][1]==1 and i!=number:#判断能不能从左岸到右岸
            left[i][1] -= 1#进行移动操作
            if judge(left):#如果可以进行移动
                right[i][1]+=1
                number = i
                print("%s,left -> right"%left[i][0])
                count+=1#步数加一
                break#停止
            else:#不能移动就加回来
                left[i][1] += 1
                continue
        else:
            continue

def right_to_left():#另一方案是对称的
    global number
    global count
    if judge(right) == False:#只有不能共存的时候才需要从右岸移动到左岸
        for j in range(l):
            if right[j][1] == 1 and  j!=number:#不能刚刚移过来又再移过去
                right[j][1]-=1
                left[j][1]+=1
                number = j
                print("%s,right->left"%right[j][0])
                count+=1
                break
    else:
        if right[0][1]+right[1][1]+right[2][1]==3:
            print('over')
        else:
            print('right->left')
            count+=1

def sucess(right):
     if right[0][1]+right[1][1]+right[2][1]==3:
         return True
     else:
         return False

while 1:
    left_to_right()
    right_to_left()
    if sucess(right):
        print('程序需要%d步'%count)
        break


def is_valid_state(state):
    # 检查是否有不安全的状态，即狼吃羊或羊吃菜
    if (state[1] == state[2] and state[0] != state[1]) or (state[2] == state[3] and state[0] != state[2]):
        return False
    return True

def dfs(state, path, visited):
    if state == (0, 0, 0, 0):
        # 找到了解决方案
        print("找到解决方案：", path)
        return

    for move in moves:
        new_state = tuple(state[i] + move[i] for i in range(4))
        if all(0 <= new_state[i] <= 1 for i in range(4)) and is_valid_state(new_state) and new_state not in visited:
            visited.add(new_state)
            dfs(new_state, path + [new_state], visited)
            visited.remove(new_state)

# 初始状态：(1, 1, 1, 1) 表示人、狼、羊、菜都在起始岸
initial_state = (1, 1, 1, 1)
# 移动方式
moves = [
    (-1, 0, 0, 0),
    (-1, -1, 0, 0),
    (-1, 0, -1, 0),
    (-1, 0, 0, -1),
    (1, 0, 0, 0),
    (1, 1, 0, 0),
    (1, 0, 1, 0),
    (1, 0, 0, 1)
]

visited = set()
visited.add(initial_state)

dfs(initial_state, [initial_state], visited)





