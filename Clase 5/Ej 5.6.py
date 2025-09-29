def propagar(lista):
    res = lista.copy()
    for i in range(1, len(res)):
        if res[i-1] == 1 and res[i] == 0:
            res[i] = 1
    for i in range(len(res)-2, -1, -1):
        if res[i+1] == 1 and res[i] == 0:
            res[i] = 1
    return res

if __name__ == "__main__":
    print(propagar([0,0,0,-1,1,0,0,0,-1,0,1,0,0]))
    print(propagar([0,0,0,1,0,0]))
