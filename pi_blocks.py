#Python Institute while loop excersise
#A simpleprogram that return theheight of a pyramid made of blocks, each layer contains 1 block morathan the previus

def height_pyramid (blocks):
    count = 0
    height = 0
    layers = []

    while count < blocks:
        count += 1
        layer = count
        layers.append(layer)

        if sum (layers) == blocks:
            height = layer
            break
        elif sum (layers) <= blocks:
            height = layer

    return height
    
def main ():
    blocks = int (input ("Enterthe number of blocks: "))
    h = height_pyramid (blocks)
    print (f"The height of the pyramid will be: {h}")

if __name__ == "__main__":
    main ()