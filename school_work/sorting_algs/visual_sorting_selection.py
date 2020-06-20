#a program to show how sorting works visually
import pygame
pygame.init()

#variables
running = True
list1 = [3, 1, 4, 5, 2, 10, 2, 55, 23, 67, 81, 12, 21, 20, 15, 22, 13, 32]
num1 = 0
y = 10
space_counter = 20
color_counter = 0
canvas_x = len(list1)*20 + 40
canvas_y = max(list1)*10 + 20
compars = 1
i = 0
list2 = list(list1)

def find_lowest(list_name):
    """This function finds the lowest value in a given list"""
    compars = 1
    lowest = list_name[0]
    for x in list_name:
        if compars == len(list_name):
            break
        next_index = list_name.index(x) + 1
        if list_name[next_index] < x and list_name[next_index] < lowest:
            lowest = list_name[next_index]
        compars += 1
    return lowest

def selection_sort(list1):
    i = 0
    list2 = list(list1)
    for i in range(len(list1)):
        list2 = list1[i:]
        lowest = find_lowest(list2)
        lowest_index = list1.index(lowest)
        if lowest_index!= i:
            list1[i], list1[lowest_index] = list1[lowest_index], list1[i]
        i +=1

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

    pygame.time.wait(100)
    gameDisplay.fill((0, 0, 1))

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
    selection_sort(list1)

    pygame.time.wait(100)
    running = False
