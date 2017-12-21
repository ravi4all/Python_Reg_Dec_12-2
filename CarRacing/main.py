import pygame
import random

pygame.init()

red = (255,150,100)
black = (0,0,0)

width = 900
height = 600

screen = pygame.display.set_mode((width, height))

# bg_img = pygame.image.load("assets/bg_1.jpg")
bg_img_2 = pygame.image.load("assets/bg_3.jpg")

bg_img = pygame.image.load("assets/bg_3.jpg")

my_car = pygame.image.load("assets/car_1.png")
car_1 = pygame.image.load("assets/car_2.png")
car_2 = pygame.image.load("assets/car_3.png")

clock = pygame.time.Clock()
FPS = 80

def game():

    move_bg_y = -8400
    move_y = 0

    move_bg2_y = -8400 - 8400

    car_x = width/2 - 50
    move_car = 0

    e_car_x = width/2 - 125
    e_car2_x = width/2 + 25

    move_enemy = 0

    e_car_y = random.randint(-height, height - 100)
    e_car2_y = random.randint(-height, height - 100)

    race = True

    while True:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    move_y += 15
                    move_enemy += 2
                elif event.key == pygame.K_RIGHT:
                    move_car = 5
                elif event.key == pygame.K_LEFT:
                    move_car = -5
                elif event.key == pygame.K_DOWN:
                    move_y -= 5
            # elif event.type == pygame.KEYUP:
            #     move_y -= 5

        # keystate = pygame.key.get_pressed()
        # if race:
        #     if keystate[pygame.K_UP]:
        #         move_y += 0.1
        #         e_car_y += 0.5
        #         e_car2_y += 0.5
        #     elif keystate[pygame.K_DOWN]:
        #         move_y -= 0.5
        #
        # if move_y >= 30:
        #     move_y = 30
        #     race = False

        # Screen Blit
        screen.fill(black)
        screen.blit(bg_img, (0,0))
        screen.blit(bg_img, (0,move_bg_y))
        screen.blit(bg_img_2, (0,move_bg2_y))
        screen.blit(my_car, (car_x, height - 200))
        screen.blit(car_1, (e_car_x, e_car_y))
        screen.blit(car_2, (e_car2_x, e_car2_y))

        move_bg_y += move_y
        move_bg2_y += move_y

        e_car_y += move_enemy
        e_car2_y += move_enemy

        car_x += move_car

        if move_bg_y > height:
            move_bg_y = -8400
        elif move_bg2_y > height:
            move_bg2_y = -8400 -8400

        if car_x > width/2 + 50:
            move_car = 0
        elif car_x < width/2 - 130:
            move_car = 0

        if e_car_y > height:
            e_car_y = random.randint(-height, -100)
            e_car_x = random.randint(width/2 - 125, width/2 - 60)
        elif e_car2_y > height:
            e_car2_y = random.randint(-height, -100)
            e_car2_x = random.randint(width/2 - 50, width/2 + 25)

        pygame.display.update()
        clock.tick(FPS)

game()
