import pygame
firstValue = pygame.init()
print(firstValue)

#Defining Colors
White = (255,255,255)
Red = (255,0,0)
Black = (0,0,0)

Message = "******My First Snake Game******"
screenWidth = 900
ScreenHeight = 900
Gamewindow = pygame.display.set_mode((screenWidth,ScreenHeight))
pygame.display.set_caption(Message)
Gamewindow.fill(White)
pygame.display.update()

Snake_X = 40
Snake_y = 30
Snake_Size = 10
exit_Game = False
gameOver = False
fps = 30
clock = pygame.time.Clock()

while not exit_Game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_Game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                Snake_y += 5
            if event.key == pygame.K_UP:
                Snake_y -= 5
            if event.key == pygame.K_LEFT:
                print("You are pressing Left Arrow Key")
                Gamewindow.fill(Red)
                Snake_X -= 5
                pygame.display.update()
            if event.key == pygame.K_RIGHT:
                print("You have pressed Right Arrow key")
                Gamewindow.fill(White)
                Snake_X += 5
        pygame.draw.rect(Gamewindow,Black,[Snake_X,Snake_y,Snake_Size,Snake_Size])
        pygame.display.update()
        clock.tick(fps)



pygame.quit()
quit()

