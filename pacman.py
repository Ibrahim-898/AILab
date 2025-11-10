
from collections import deque


N = 1000
n=m=0
grid =[]  #2D list
  #2D list
 

x = input().split()
n = int(x[0])
m = int(x[1])

for _ in range(n):
    row = list(input().strip())
    grid.append(row)




v = [(0,1),(1,0),(0,-1),(-1,0)] #List  of tuple 

def isvalid(i,j):
    if(i<0 or i>=n or j<0 or j>=m or grid[i][j]=='#'):
        return False
    return True

def bfs(start1,start2):
    visited = [] 
    dist =[]   #2D list
    for _ in range(n):
      row = []
      for _ in range(m):
        row.append(False)
      visited.append(row)

    for _ in range(n):
     row =[]
     for _ in range(m):
        row.append(-1)
     dist.append(row)


    dq = deque()
    dq.append((start1,start2))
    visited[start1][start2]=True
    dist[start1][start2]=0

    while dq:
        x,y = dq.popleft()
     
        for i in range(4):
            a,b = v[i]
            cx = x+a
            cy = y+b
            if(isvalid(cx,cy) and  visited[cx][cy]==False):
                dq.append((cx,cy))
                visited[cx][cy]=True
                dist[cx][cy]=dist[x][y]+1
    return dist
    

Food = []

for i in range(n):
    for j in range(m):
        if grid[i][j]=='P':
            pacman = i,j
        if grid[i][j]=='F':
            Food.append((i,j))

total_cost = 0
print(pacman)       
while Food:
    pos1,pos2=pacman
    dist = bfs(pos1,pos2)
    min_distance = 1e9
    nearest_food = None


    for x,y in Food:
        if dist[x][y]!=-1 and dist[x][y]<min_distance:
            min_distance= dist[x][y]
            nearest_food = (x,y)

    if nearest_food is None:
        print("Some Food cannot be reached due to walls")
        break
    total_cost += min_distance
    px,py=nearest_food
    grid[px][py]='P'
    pacman=nearest_food
    Food.remove(nearest_food)


print("All food collected!")
print(total_cost)
for row in grid:
    print(row)




