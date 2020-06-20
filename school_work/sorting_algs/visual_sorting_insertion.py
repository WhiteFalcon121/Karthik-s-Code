#a program to show how sorting works visually
import pygame
pygame.init()

#variables
running = True
list1 = [8, 4, 5, 1, 22, 25, 11, 15, 67, 13, 17, 3, 90, 24, 12, 12, 39, 20, 21, 20, 45, 5, 2, 3, 0]
num1 = 0
y = 10
space_counter = 20
color_counter = 0
canvas_x = len(list1)*20 + 40
canvas_y = max(list1)*10 + 20

# drawlist function
def drawlist(listname, space_counter, color_counter):
    """This function draws the list from the listname given, color and space counter"""
    for i in listname:
        if color_counter > 255:
            color_counter = 0
        if space_counter == (len(listname) * 20) + 100:
            space_counter = 100
            color_counter = 0
        pygame.draw.rect(gameDisplay, (color_counter, 100, 100), [space_counter, y, 20, i*10])
        pygame.display.flip()
        space_counter = space_counter + 20
        color_counter = color_counter + 30

    #pygame.time.wait(100)
    gameDisplay.fill((0, 0, 1))

def insertion_sort(list1):
    num1 = 0
    for x in list1:
        numsbefore = list1.index(x)
        currentnum = x
        if numsbefore != 0:
            for x in list1[:numsbefore]:
                if currentnum < x:
                    num1 = num1 + 1
                if num1 == len(list1[:numsbefore]):
                    list1.remove(currentnum)
                    list1.insert(0, currentnum)
                    num1 = 0
                    continue
                if currentnum < x and list1.index(currentnum) > list1.index(x):
                    list1.remove(currentnum)
                    list1.insert(list1.index(x), currentnum)
                num1 = 0

        newlist = []
        num = 0
        for i in list1:
            if list1.count(i) > 1 and i in newlist:
                list1.pop(num)
                list1.insert(list1.index(i)+1, i)
            newlist.append(i)
            num += 1

        drawlist(list1, space_counter, color_counter)

    return list1
#set up

gameDisplay = pygame.display.set_mode((canvas_x, canvas_y))
gameDisplay.fill((0, 0, 1))

drawlist(list1, space_counter, color_counter)

while running == 1:
    for i in range(0, len(list1)-1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    insertion_sort(list1)

    #print(list1)
    pygame.time.wait(100)
    print("Result: ", list1)
    running = False
