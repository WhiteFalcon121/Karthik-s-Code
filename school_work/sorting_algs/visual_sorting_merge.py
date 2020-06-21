import pygame
pygame.init()

#variables
running = True
list1 = [2, 5, 1, 3, 4, 2, 9, 1]
num1 = 0
y = 10
space_counter = 20
color_counter = 0
canvas_x = len(list1)*20 + 80
canvas_y = max(list1)*10 + 30
reverse = False
#drawlist function
def drawlist(listname, space_counter, color_counter):
    """This function draws the list from the listname given, color and space counter"""
    for i in listname:
        if color_counter > 255:
            color_counter = 0
        if space_counter == (len(listname) * 20) + 100:
            space_counter = 100
            color_counter = 0
        if i < 0:  #for gaps - (they are negative)
            pygame.draw.rect(gameDisplay, (0, 0, 1), [space_counter, y, 20, 20])
        else:
            pygame.draw.rect(gameDisplay, (color_counter, 100, 100), [space_counter, y, 20, i*10])
        pygame.display.flip()
        space_counter = space_counter + 20
        color_counter = color_counter + 30

    pygame.time.wait(300)
    gameDisplay.fill((0, 0, 1))

#merge_sort function
def merge_sort(list_name):
    if len(list_name) > 1:
        mid = len(list_name)//2
        left = list_name[:mid]
        right = list_name[mid:]
        newlist = left+[-1, -1]+right # negatives are gaps
        drawlist(newlist, space_counter, color_counter)

        # recursive
        merge_sort(left)
        merge_sort(right)

        # to go through halves
        i = 0
        j = 0

        # to go through main list
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list_name[k] = left[i]
                i+=1
            else:
                list_name[k] = right[j]
                j+= 1
            k+=1

        while i < len(left):
            list_name[k] = left[i]
            i+=1
            k+=1
        while j < len(right):
            list_name[k] = right[j]
            j+=1
            k+=1
    if reverse == True:
        list_name = list_name[::-1]
    drawlist(list_name, space_counter, color_counter)
    return list_name

gameDisplay = pygame.display.set_mode((canvas_x, canvas_y))
gameDisplay.fill((0, 0, 1))

drawlist(list1, space_counter, color_counter)

while running == 1:
    for i in range(0, len(list1)-1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    merge_sort(list1)
    pygame.time.wait(100)
    running = False
