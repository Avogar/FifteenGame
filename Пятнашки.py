import pygame
import random

pygame.init()

def Win(screen):
    screen.fill(green)
    font = pygame.font.Font(None, 75)
    font2 = pygame.font.Font(None, 25)
    text = font.render('Вы СОБРАЛИ!', True, black)
    text3 = font2.render('Счёт: ' + str(count),True,black)
    text4 = font2.render(time_output,True,black)
    text2 = font2.render('Чтобы начать заново, нажмите ПРОБЕЛ.', True, black)
    screen.blit(text, [70, 200])
    screen.blit(text2, [90, 400])
    screen.blit(text3, [210, 270])
    screen.blit(text4, [200, 300])


black = (0,0,0)
white = (255,255,255)
green = (0,255,0)
red = (255,0,0)
blue = (0,0,255)
yellow = (255,255,0)
cyan = (100,230,230)
fon = grey = (100,100,100)
orange = (255,165,0)
brown = (139,69,19)
purple = (160,32,240)
DarkGreen = (0,128,0)
color = (150,150,250)

size = [505,520]
screen = pygame.display.set_mode(size)
done2 = True
end = [i+1 for i in range(16)]
while done2 == True:
    time = 0
    count = 0
    win = 0
    rebro = 120
    xx = yy = 5
    x = []
    y = []
    d = 1
    for i in range(16):
        x.append(xx)
        y.append(yy)
        if (i+1) % 4 == 0:
            d = 0
        else: d = 1
        if d == 1:
            xx += rebro + 5
        if d == 0 :
            yy += rebro + 5
            xx = 5
    summ = 1
    mass = [i+1 for i in range(16)]
    while summ%2 != 0:
        random.shuffle(mass)
        e = (mass.index(16) + 1) // 4
        if (mass.index(16) + 1) % 4 != 0: e += 1
        summ = e
        k = 0
        for i in range(16):
            j = i + 1
            if mass[i] != 16:
                for j in range(j,16):
                    if mass[i] > mass[j]:
                        k += 1
            summ += k
            k = 0
    pust = mass.index(16)
    
    pygame.display.set_caption('Пятнашки')

    mus = pygame.mixer.Sound('1380.wav')

    done = True

    clock = pygame.time.Clock()

    while done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = False
                done2 = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE and win == 1:
                    done = False
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and win != 1:
                    for i in range(16):
                        if x_mouse >= x[i] and x_mouse <= x[i] + rebro and y_mouse >= y[i] and y_mouse <= y[i] + rebro:
                            if (abs(x[i] - x[pust]) == rebro + 5 and y[i] == y[pust]) or (
                                    abs(y[i] - y[pust]) == rebro + 5 and x[i] == x[pust]):
                                mass[i], mass[pust] = mass[pust], mass[i]
                                mus.play()
                                count += 1

        pos = pygame.mouse.get_pos()
        x_mouse = pos[0]
        y_mouse = pos[1]

        if mass == end:
            win = 1
        pust = mass.index(16)

        total_sec = time // 60
        minutes = total_sec // 60
        seconds = total_sec % 60
        time_output = 'Время: {0:02}:{1:02}'.format(minutes, seconds)
        
        screen.fill(fon)

        for i in range(16):
            if i != pust:
                pygame.draw.rect(screen,color,[x[i],y[i],rebro,rebro],0)
        for i in range(16):
            if mass[i]//10 == 1:
                a = 19
                b = 30
            if mass[i] == 11:
                a = 25
                b = 30
            if mass[i]//10 == 0:
                a = 40
                b = 30
            if i != pust:
                font = pygame.font.Font(None, 100)
                text = font.render(str(mass[i]), True, black)
                screen.blit(text, [x[i]+a, y[i]+b])
        font = pygame.font.Font(None, 25)
        text = font.render('Счёт: '+str(count), True, white)
        screen.blit(text, [10,503])

        text = font.render(time_output,True, white)
        screen.blit(text,[390,503])

        if win == 1:
            Win(screen)

        if win != 1:
            time += 1

        pygame.display.flip()

        clock.tick(60)

pygame.quit()
