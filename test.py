def initMaze():
    """
    :return: 初始化迷宫
    """
    maze = [[0] * 7 for _ in range(5 + 2)]  # 用列表解析创建一个7*7的二维数组，为了确保迷宫四周都是墙
    walls = [  # 记录了墙的位置
        (1, 3),
        (2, 1), (2, 5),
        (3, 3), (3, 4),
        (4, 2),  # (4, 3),  # 如果把(4, 3)点也设置为墙，那么整个迷宫是走不出去的，所以会返回一个空列表
        (5, 4)
    ]
    for i in range(7):  # 把迷宫的四周设置成墙
        maze[i][0] = maze[i][-1] = 1
        maze[0][i] = maze[-1][i] = 1
    for i, j in walls:  # 把所有墙的点设置为1
        maze[i][j] = 1
    return maze
"""
[1, 1, 1, 1, 1, 1, 1]
[1, 0, 0, 1, 0, 0, 1]
[1, 1, 0, 0, 0, 1, 1]
[1, 0, 0, 1, 1, 0, 1]
[1, 0, 1, 0, 0, 0, 1]
[1, 0, 0, 0, 1, 0, 1]
[1, 1, 1, 1, 1, 1, 1]
"""
def path(maze, start, end):
    """
    :param maze: 迷宫
    :param start: 起始点
    :param end: 结束点
    :return: 行走的每个点
    """
    i, j = start  # 分解起始点的坐标
    ei, ej = end  # 分解结束点的左边
    stack = [(i, j)]  # 创建一个栈，并让老鼠站到起始点的位置
    maze[i][j] = 1  # 走过的路置为1
    while stack:  # 栈不为空的时候继续走，否则退出
        i, j = stack[-1]  # 获取当前老鼠所站的位置点
        if (i, j) == (ei, ej): break  # 如果老鼠找到了出口
        for di, dj in [(0, -1), (0, 1), (-1, 0), (1, 0)]:  # 左右上下
            if maze[i + di][j + dj] == 0:  # 如果当前点可走
                maze[i + di][j + dj] = 1  # 把当前点置为1
                stack.append((i + di, j + dj))  # 把当前的位置添加到栈里面
                break
        else:  # 如果所有的点都不可走
            stack.pop()  # 退回上一步
    return stack  # 如果迷宫不能走则返回空栈
Maze = initMaze()  # 初始化迷宫
result = path(maze=Maze, start=(1, 1), end=(5, 5))  # 老鼠开始走迷宫
print(result)
