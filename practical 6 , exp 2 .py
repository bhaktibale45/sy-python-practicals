
width = int(input("Enter frame width: "))
height = int(input("Enter frame height: "))

print("\n--- INVOICE FRAME BORDER ---\n")


for i in range(height):
    for j in range(width):
        
        if i == 0 or i == height - 1 or j == 0 or j == width - 1:
            print("*", end="")
        else:
            print(" ", end="")
    8
    8
    print()