if __name__ == '__main__':
    n = int(input())

def newstr(m):
    a = ""

    for i in range(1, m+1):
        a = a+str(i)
    return a

print(newstr(n))
