import sys
import os


def pgmRead(filePath):
    file = open(filePath, 'r')
    # Read the pgm file information
    magicNum = file.readline().strip()
    [width, height] = (file.readline().strip()).split()
    width = int(width)
    height = int(height)
    # print("The Width: " + str(width))
    # print("The Height: " + str(height))
    maxVal = int(file.readline().strip())
    # print("Max gray value: " + str(maxVal))

    # Removing all comments from the file
    Pixels = []
    for line in file:
        if line.startswith('#'):
            continue
        Pixels.extend((line.strip()).split())

    # Read the image pixels
    # print("Num of elements: " + str(len(Pixels)))
    if len(Pixels) != width*height:
        print ("Error in number of pixels")
        exit()
    return (Pixels, width, height)


def pgmWrite(image, filePath, width, height, maxVal=4096, magicNum='P2'):
    file = open(filePath, 'w')

    # Writing the pgm file header information
    file.write(magicNum + '\n')
    file.write(str(width) + ' ' + str(height) + '\n')
    file.write(str(maxVal) + '\n')

    # Writing the image pixels
    for i in range(height):
        for j in range(width):
            file.write(str(image[j+i*width]) + ' ')
        file.write('\n')
    file.close()


def main():
    filesNum = 0
    width = 0
    height = 0
    inputImages = []
    averageImage = []
    outputFile = "Average.pgm"

    if len(sys.argv) != 2:
        print("Error: The path of the input files is not specified")
        exit()
    path = sys.argv[1]
    os.chdir(path)
    for file in os.listdir():
        # Check if the file is in pgm format
        if ((file.endswith(".pgm")) and file != outputFile):
            (image, width, height) = pgmRead(f"{path}\{file}")
            inputImages.append(image)
            filesNum = filesNum+1
    print(f"Number of pgm files: {filesNum}")

    # Calculating he average value at each index
    for i in range(width*height):
        sum = 0
        for j in range(filesNum):
            sum += int(inputImages[j][i])
        # Rounding the result after the division operation
        averageValue = round(sum/filesNum)
        averageImage.append(averageValue)

    # Generating the average pgm file
    pgmWrite(averageImage, f"{path}\{outputFile}", width, height)
    print("The average image has been generated successfully")


if __name__ == "__main__":
    main()
