# Assignment Three for Python - Arush Mahajan (Div:13)

def rightangledtriangle(x1,x2,x3):
    lenghtlist = [int(x1),int(x2),int(x3)]
    lenghtlist.sort()
    if lenghtlist[0]**2 + lenghtlist[1]**2 == lenghtlist[2]**2:
        print("\nIts a right angled triangle")
        return True
    else:
        print("\nIt is not a right angled triangle")
        return False

print("Right Angled Triangle Checker")
print(rightangledtriangle(input("Please enter first side: "),input("Please enter second side: "),input("Please enter third side: ")))