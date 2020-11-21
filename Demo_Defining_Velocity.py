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

food_x = 20
food_y = 25

Snake_X = 40
Snake_y = 30
Snake_Size = 10
Snake_Velocity_X =0
Snake_Velocity_Y =0

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
                Snake_Velocity_Y += 10
                Snake_Velocity_X = 0
            if event.key == pygame.K_UP:
                Snake_Velocity_Y -=10
                Snake_Velocity_X = 0
            if event.key == pygame.K_LEFT:
                Snake_Velocity_X-= 10
                Snake_Velocity_Y= 0
                Gamewindow.fill(Red)
                Snake_X -= 5
                pygame.display.update()
            if event.key == pygame.K_RIGHT:
                Snake_Velocity_X += 10
                Snake_Velocity_Y = 0
                Gamewindow.fill(White)
                Snake_X += 5

            Snake_X += Snake_Velocity_X
            Snake_y += Snake_Velocity_Y

        pygame.draw.rect(Gamewindow,Black,[Snake_X,Snake_y,Snake_Size,Snake_Size])
        pygame.draw.rect(Gamewindow, Red, [food_x, food_y, Snake_Size, Snake_Size])

        pygame.display.update()
        clock.tick(fps)



pygame.quit()
quit()

