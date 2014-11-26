def gen(n=21):
    glist = []
    for i in range(n-1):
        for j in range(n-1):
            glist.append([n*i+j+1,n*i+j+n])
        glist.append([n*i+n+n-1])
    # last row
    for i in range(n-1):
        glist.append([n*(n-1)+i+1])
    return glist


def dfs(root, t=440, graph=gen(), visited={}):
    if root == t:
        return 1
    if root in visited:
        return visited[root]
    counter = 0
    for node in graph[root]:
        counter += dfs(node)
    visited[root] = counter
    return counter
