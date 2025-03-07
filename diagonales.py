'''
3
# # #
  #
#
  #
    #

'''

number=int(input("Ingresa un numero:"))
for a in range(number):
    print("■ ",end="")

print("")


m = number
for e in range(1,number -1):
    for i in range(1,m):
        print(" ", end="")

    print("■")
    m-=1



for o in range(0, number):
    
    for u in range(0,o):
        print("  ",end="")
        
    print("■")