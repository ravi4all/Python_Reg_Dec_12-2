import pygame
import random
from pygame.locals import  *

pygame.init()

red = (255,150,100)
green = (0,255,0)
yellow = (255,255,0)
black = (0,0,0)
white = (255,255,255)

width = 900
height = 600

screen = pygame.display.set_mode((width, height))

# bg_img = pygame.image.load("assets/bg_1.jpg")
bg_img_2 = pygame.image.load("assets/bg_3.jpg")

bg_img = pygame.image.load("assets/bg_3.jpg")

my_car = pygame.image.load("assets/car_1.png")
car_1 = pygame.image.load("assets/car_2.png")
car_2 = pygame.image.load("assets/car_3.png")

main_bg = pygame.image.load("assets/mainBg.jpg")

main_bg_sound = pygame.mixer.Sound('assets/racing_theme.ogg')
main_bg_sound.play(-1)

clock = pygame.time.Clock()
FPS = 80


def splashScreen():
    font = pygame.font.Font('assets/font_2.ttf', 55)
    text = font.render("Press Space to Start", True, white)
    while True:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game()

        screen.blit(main_bg, (0,0))
        screen.blit(text, (width/2 - 200, 30))

        pygame.display.update()


def carDestroy(carHealth):
    if carHealth <= 70:
        color = yellow
    elif carHealth <= 50:
        color = red
    else:
        color = green

    pygame.draw.rect(screen, color, (width - 200, 50, carHealth, 25))

def timer(seconds):
    font = pygame.font.SysFont(None, 45)
    text = font.render("Time : "+str(seconds), True, white)
    screen.blit(text, (width - 200, 10))

def gameOver():
    font = pygame.font.Font('assets/font_2.ttf', 55)
    text = font.render("Game Over", True, white)
    text_2 = font.render("Press SPACE to Restart", True, white)
    while True:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game()

        screen.blit(text, (width/2 - 200, 30))
        screen.blit(text_2, (width/2 - 300, 100))

        pygame.display.update()

def game():

    move_bg_y = -8400
    move_y = 0

    move_bg2_y = -8400 - 8400

    car_x = width/2 - 50
    car_y = height - 200
    move_car = 0

    e_car_x = width/2 - 125
    e_car2_x = width/2 + 25

    move_enemy = 0

    left_hit = False
    right_hit = False

    e_car_y = random.randint(-height, height - 100)
    e_car2_y = random.randint(-height, height - 100)

    seconds = 10
    pygame.time.set_timer(USEREVENT + 1, 1000)

    carHealth = 150

    while True:

        if left_hit:
            move_car += 1
            car = pygame.transform.rotate(my_car,45)
            print("Left Hit")
            carHealth -= 1
        elif right_hit:
            move_car -= 1
            car = pygame.transform.rotate(my_car,-45)
            print("Right Hit")
            carHealth -= 1
        else:
            car = pygame.transform.rotate(my_car,0)

        if car_x > width/2 + 50:
            move_car = 0
            left_hit = False
            right_hit = False
            car = pygame.transform.rotate(my_car,0)
            print("Left Hit_2")
        elif car_x < width/2 - 130:
            move_car = 0
            left_hit = False
            right_hit = False
            car = pygame.transform.rotate(my_car,0)
            print("Right Hit_2")

        if carHealth <= 0:
            carHealth = 0

        if carHealth == 0 or seconds == -1:
            gameOver()
            break

        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif event.type == USEREVENT + 1:
                seconds -= 1

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
            elif event.type == pygame.KEYUP:
                move_car = 0

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
        screen.blit(car_1, (e_car_x, e_car_y))
        screen.blit(car_2, (e_car2_x, e_car2_y))

        screen.blit(car, (car_x, car_y))

        my_rect = pygame.Rect(car_x, car_y, my_car.get_width(), my_car.get_height())
        rect_1 = pygame.Rect(e_car_x, e_car_y, car_1.get_width(), car_1.get_height())
        rect_2 = pygame.Rect(e_car2_x, e_car2_y, car_2.get_width(), car_2.get_height())

        if my_rect.colliderect(rect_1):
            left_hit = True
        elif my_rect.colliderect(rect_2):
            right_hit = True

        move_bg_y += move_y
        move_bg2_y += move_y

        e_car_y += move_enemy
        e_car2_y += move_enemy

        car_x += move_car

        if move_bg_y > height:
            move_bg_y = -8400
        elif move_bg2_y > height:
            move_bg2_y = -8400 -8400

        if e_car_y > height:
            e_car_y = random.randint(-height, -100)
            e_car_x = random.randint(width/2 - 125, width/2 - 60)
        elif e_car2_y > height:
            e_car2_y = random.randint(-height, -100)
            e_car2_x = random.randint(width/2 - 50, width/2 + 25)


        timer(seconds)
        carDestroy(carHealth)
        pygame.display.update()
        clock.tick(FPS)

#game()
splashScreen()
