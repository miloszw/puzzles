def gen(n=20):
    glist = []
    for i in range(n-1):
        for j in range(n-1):
            glist.append([n*i+j+1,n*i+j+n])
        glist.append([n*i+n+n-1])
    # last row
    for i in range(n-1):
        glist.append([n*(n-1)+i+1])
    return glist


def dfs(root, s=0, t=399, graph=gen()):
    if root == t:
        return 1
    queue = graph[root]
    counter = 0
    for node in queue:
        counter += dfs(node)

    return counter

