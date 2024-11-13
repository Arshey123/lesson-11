# Activity 1
# def printno(n):
#     iteration=0
#     print("Number by user:",n)
#     iteration+=1
#     print("iteration:",iteration)
# printno(10)
# printno(60)
# Activity 2
# def printno(n):
#     iteration=0
#     for i in range(1,n+1):
#         iteration+=1
#     print("When n is",n,"iteration is",iteration)
# printno(10)
# printno(60)
# Activity 3
def printno(n):
    iteration=0
    for i in range(0,n):
        for j in range (0,n):
            print("*",end="")
            iteration+=1
        print("")
    print("When n is",n,"iteration is",iteration)
printno(10)
printno(5)