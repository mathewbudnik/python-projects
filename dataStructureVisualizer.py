import pygame

# Initialize Pygame
pygame.init()

# Set the window dimensions
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1200

# Create the window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the window title
pygame.display.set_caption("Data Structure Visualizer")

# Define the text font
font = pygame.font.SysFont(None, 36)

# Define the colors
textColor = (255, 255, 255)
arrayColor = (255, 0, 0) 
linkedListColor = (0, 255, 0)   
stackColor = (0, 0, 255)         
queueColor = (0, 255, 255)       
hashTableColor = (255, 255, 0)  
heapColor = (255, 165, 0)        

# Define the positions and labels for the data structures
labels = {
    "Array: ": (50, 50),
    "Linked List: ": (50, 200),
    "Stack: ": (50, 310),           
    "Queue: ": (50, 590),           
    "Hash Table: ": (50, 690),
    "Heap: ": (50, 850),
}
# Define the positions and definitions for the data structures

dataDefinitions = {
    "Fixed-size, indexed collection of elements": (135, 50),
    "Nodes containing values, linked by pointers.": (200, 200),
    "Last IN First OUT way to structure elements.": (135, 310),           
    "First IN First OUT way to structure elements.": (150, 590),           
    "Key-value pairs with fast lookup.": (200, 690),
    "Tree with ordered parent-child nodes.": (125, 850),
}

# Define example data for each data structure
arrayVisual = [3, 7, 4, 2, 8, 9, 2, 5]
linkedList = [3, 7, 4, 2, 8, 9, 2, 5]
stackVisual = [5, 3, 7, 2]
queueVisual = [2, 7, 3, 5]
hashTable = {3: 'A', 7: 'B', 4: 'C', 2: 'D', 8: 'E'}
heapVisual = [3, 7, 4, 2, 8, 9, 5]

# Main loop
running = True
while running:
    # Clear the screen (black background)
    screen.fill((0, 0, 0))

    # Array Visualization
    arrayLabel = font.render("Array: ", True, textColor)
    arrayDef = font.render("Fixed-size, indexed collection of elements", True, textColor)

    screen.blit(arrayLabel, labels["Array: "])
    screen.blit(arrayDef, dataDefinitions["Fixed-size, indexed collection of elements"])
    
    barWidth = 50
    maxHeight = 100  

    for i, value in enumerate(arrayVisual):
        barHeight = (value / max(arrayVisual)) * maxHeight
        pygame.draw.rect(screen, arrayColor, (50 + i * (barWidth + 10), 100, barWidth, barHeight))

    # Linked List Visualization 
    linkedListLabel = font.render("Linked List: ", True, textColor)
    linkedListDef = font.render("Nodes containing values, linked by pointers.", True, textColor)

    screen.blit(linkedListLabel, labels["Linked List: "])
    screen.blit(linkedListDef, dataDefinitions["Nodes containing values, linked by pointers."])


    nodeRadius = 20

    for i, node in enumerate(linkedList):
        pygame.draw.circle(screen, linkedListColor, (100 + i * 100, 250), nodeRadius)
        nodeText = font.render(str(node), True, (0, 0, 0))
        screen.blit(nodeText, (90 + i * 100, 240))

        if i < len(linkedList) - 1:
            pygame.draw.line(screen, (255, 255, 255), (140 + i * 100, 250), (160 + i * 100, 250), 5)

    # Stack Visualization
    stackLabel = font.render("Stack: ", True, textColor)
    stackDef = font.render("Last IN First OUT way to structure elements.", True, textColor)

    screen.blit(stackLabel, labels["Stack: "])
    screen.blit(stackDef, dataDefinitions["Last IN First OUT way to structure elements."])
    
    rectWidth, rectHeight = 80, 50

    for i, value in enumerate(stackVisual):
        pygame.draw.rect(screen, stackColor, (50, 340 + i * rectHeight, rectWidth, rectHeight))  
        stackText = font.render(str(value), True, (255, 255, 255))
        screen.blit(stackText, (70, 350 + i * rectHeight))  

    # Queue Visualization
    queueLabel = font.render("Queue: ", True, textColor)
    queueDef = font.render("First IN First OUT way to structure elements.", True, textColor)

    screen.blit(queueLabel, labels["Queue: "])
    screen.blit(queueDef, dataDefinitions["First IN First OUT way to structure elements."])

    rectWidth, rectHeight = 80, 50

    for i, value in enumerate(queueVisual):
        pygame.draw.rect(screen, queueColor, (50 + i * (rectWidth + 10), 630, rectWidth, rectHeight))  
        queueText = font.render(str(value), True, (0, 0, 0))
        screen.blit(queueText, (70 + i * (rectWidth + 10), 640))  

    # Hash Table Visualization
    hashLabel = font.render("Hash Table: ", True, textColor)
    hashDef = font.render("Key-value pairs with fast lookup.", True, textColor)

    screen.blit(hashLabel, (labels["Hash Table: "][0], labels["Hash Table: "][1] + 50))
    screen.blit(hashDef, (dataDefinitions["Key-value pairs with fast lookup."][0], dataDefinitions["Key-value pairs with fast lookup."][1] + 50))
   

    for i, (key, value) in enumerate(hashTable.items()):
        pygame.draw.rect(screen, hashTableColor, (50 + i * 150, 790, 100, 50))  
        hashText = font.render(f"{key}: {value}", True, (0, 0, 0))
        screen.blit(hashText, (75 + i * 150, 795))

    # Heap Visualization
    heapLabel = font.render("Heap: ", True, textColor)
    heapDef = font.render("Tree with ordered parent-child nodes.", True, textColor)
    
    screen.blit(heapLabel, labels["Heap: "])
    screen.blit(heapDef, dataDefinitions["Tree with ordered parent-child nodes."])

    heapNodeRadius = 20

    for i, value in enumerate(heapVisual):
        pygame.draw.circle(screen, heapColor, (100 + i * 100, 920), heapNodeRadius)
        heapText = font.render(str(value), True, (0, 0, 0))
        screen.blit(heapText, (90 + i * 100, 910))

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the display
    pygame.display.flip()

pygame.quit()
