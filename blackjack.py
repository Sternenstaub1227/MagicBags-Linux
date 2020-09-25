import pygame, random, os
global color, point, choice, bet, money, B, P, x, y, temp, choose, sumB, sumP, step, CB, CP, chb, chp, flagP, bjB, bjP, doubled, steps
color = [0 for i in range(0, 54)]
point = [0 for i in range(0, 54)]
choice = [1 for i in range(0, 54)]
B = [0 for i in range(0, 10)]
P = [0 for i in range(0, 10)]
CB = 2
CP = 2
chb = 1
chp = 1
flagP = 0
bjB = 0
bjP = 0
doubled = 0
def reset_card():
    for i in range(1, 5):
        for j in range(1, 14):
            color[(i - 1) * 13 + j] = i
            point[(i - 1) * 13 + j] = j
    for i in range(1, 53):
        choice[i] = i
def fresh_card():
    for i in range(1, 53):
        x = random.randint(1, 53)
        y = random.randint(1, 53)
        if x == y:
            y = random.randint(1, 53)
        temp = choice[x]
        choice[x] = choice[y]
        choice[y] = temp
def print_card_B(i, t):
    cards = str(i) + ".jpg"
    screen.blit(pygame.image.load(cards), [200 + 120 * t, 80])
def print_card_P(i, t):
    cards = str(i) + ".jpg"
    screen.blit(pygame.image.load(cards), [200 + 120 * t, 300])
def move_card_P():
    global CP, bet, doubled, flagP, steps

    if doubled == 1:
        screen.blit(my_font.render('Player Double', True, (0, 255, 255)), (700, 500))
        flagP = 1
    else:
        if steps == 1:
            CP += 1
            screen.blit(my_font.render('Player Hit', True, (0, 255, 255)), (700, 500))
        if steps == 2:
            screen.blit(my_font.render('Player Hold', True, (0, 255, 255)), (700, 500))
            flagP = 1
        if steps == 3:
            CP += 1
            screen.blit(my_font.render('Player Double', True, (0, 255, 255)), (700, 500))
            bet *= 2
            doubled = 1
def move_card_B():
    global CB, flagP
    sumB1 = 0
    if B[CB + 1] == 11 or B[CB + 1] == 12 or B[CB + 1] == 13 or B[CB + 1] == 24 or B[CB + 1] == 25 or B[CB + 1] == 26 or \
            B[CB + 1] == 37 or B[CB + 1] == 38 or B[CB + 1] == 39 or B[CB + 1] == 50 or B[CB + 1] == 51 or B[
        CB + 1] == 52:
        sumB1 = sumB + 10
    else:
        sumB1 = sumB + (B[CB + 1] % 13)
    if bjB == 0:
        if sumB1 <= 21:
            CB += 1
            screen.blit(my_font.render('Banker Hit!', True, (0, 255, 255)), (700, 500))
        else:
            screen.blit(my_font.render('Banker Hold', True, (0, 255, 255)), (700, 500))
            flagP = 3
    else:
        if (sumB + 10 > sumP and sumB1 + 10 <= 21) or (sumB + 10 > sumP and bjP == 0):
            screen.blit(my_font.render('Banker Hold', True, (0, 255, 255)), (700, 500))
            flagP = 3
            return 0
        if (sumB1 + 10 < 21) or (sumB1 + 10 > 21 and sumB1 < sumP):
            CB += 1
            screen.blit(my_font.render('Banker Hit!', True, (0, 255, 255)), (700, 500))
            return 0
        if (sumB + 10 > sumP and sumB1 + 10 <= 21) or (sumB + 10 > sumP + 10 and bjP != 0):
            screen.blit(my_font.render('Banker Hold', True, (0, 255, 255)), (700, 500))
            flagP = 3
            return 0
def check_card():
    global bet
    if sumB > sumP and bjP == 0 and bjB == 0:
        screen.blit(backGround4, [0, 0])
        screen.blit(my_font.render('You lose!!!', True, (0, 255, 255)), (500, 250))
        bet *= (-1)
    if sumB < sumP and bjP == 0 and bjB == 0:
        screen.blit(backGround4, [0, 0])
        screen.blit(my_font.render('You win!!!', True, (0, 255, 255)), (500, 250))
        bet *= 1
    if sumB == sumP and bjP == 0 and bjB == 0:
        screen.blit(backGround4, [0, 0])
        screen.blit(my_font.render('Draw', True, (0, 255, 255)), (500, 250))
        bet *= 0
    if sumB + 10 > sumP and bjP == 0 and bjB != 0:
        screen.blit(backGround4, [0, 0])
        screen.blit(my_font.render('You lose!!!', True, (0, 255, 255)), (500, 250))
        bet *= (-1)
    if sumB + 10 < sumP and bjP == 0 and bjB != 0:
        screen.blit(backGround4, [0, 0])
        screen.blit(my_font.render('You win!!!', True, (0, 255, 255)), (500, 250))
        bet *= 1
    if sumB + 10 == sumP and bjP == 0 and bjB != 0:
        screen.blit(backGround4, [0, 0])
        screen.blit(my_font.render('Draw', True, (0, 255, 255)), (500, 250))
        bet *= 0
    if sumB > sumP + 10 and bjP != 0 and bjB == 0:
        screen.blit(backGround4, [0, 0])
        screen.blit(my_font.render('You lose!!!', True, (0, 255, 255)), (500, 250))
        bet *= (-1)
    if sumB < sumP + 10 and bjP != 0 and bjB == 0:
        screen.blit(backGround4, [0, 0])
        screen.blit(my_font.render('You win!!!', True, (0, 255, 255)), (500, 250))
        bet *= 1
    if sumB == sumP + 10 and bjP != 0 and bjB == 0:
        screen.blit(backGround4, [0, 0])
        screen.blit(my_font.render('Draw', True, (0, 255, 255)), (500, 250))
        bet *= 0
    if sumB + 10 > sumP + 10 and bjP != 0 and bjB != 0:
        screen.blit(backGround4, [0, 0])
        screen.blit(my_font.render('You lose!!!', True, (0, 255, 255)), (500, 250))
        bet *= (-1)
    if sumB + 10 < sumP + 10 and bjP != 0 and bjB != 0:
        screen.blit(backGround4, [0, 0])
        screen.blit(my_font.render('You win!!!', True, (0, 255, 255)), (500, 250))
        bet *= 1
    if sumB + 10 == sumP + 10 and bjP != 0 and bjB != 0:
        screen.blit(backGround4, [0, 0])
        screen.blit(my_font.render('Draw', True, (0, 255, 255)), (500, 250))
        bet *= 0
def blackjack_card_B(a):
    global bjB
    if a == 1 or a == 14 or a == 27 or a == 40:
        bjB += 1
def blackjack_card_P(a):
    global bjP
    if a == 1 or a == 14 or a == 27 or a == 40:
        bjP += 1
# 初始化
pygame.init()
# 设定窗口大小、标题、背景图片
size = width, height = 1280, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Gambling')
pngFileName_1 = 'cards-casino-chance-chip-269630.jpg'
pngFileName_2 = '1-us-bank-note-47344.jpg'
pngFileName_3 = 'ace-cards-casino-deck-279009.jpg'
backGround1 = pygame.image.load(pngFileName_1)
backGround2 = pygame.image.load(pngFileName_2)
backGround3 = pygame.image.load(pngFileName_3)
backGround4 = pygame.transform.scale(pygame.image.load("logo2.jpg"), (1280, 600))
screen.blit(backGround1, [0, 0])
my_font = pygame.font.Font('bb.otf', 50)
my_font1 = pygame.font.Font('bb.otf', 30)
text_surface1 = my_font.render("Welcome to THE ABYSS OF CRAZY GAMBLING", True, (255, 255, 0))
text_surface2 = my_font.render("Press Any Button to Continue", True, (255, 255, 0))
text_surface3 = my_font.render("The Chips You Have Are: ", True, (25, 25, 235))
text_surface19 = my_font.render("1000", True, (255, 0, 0))
text_surface4 = my_font.render("So let's start unrestrained gambling", True, (25, 25, 235))
text_surface5 = my_font.render("Enter the bet: ", True, (255, 255, 0))
text_surface6 = my_font.render("The bet for this turn: ", True, (255, 255, 0))
text_surface7 = my_font.render("Banker:", True, (255, 255, 0))
text_surface8 = my_font.render("Player:", True, (255, 255, 0))
text_surface9 = my_font.render("The Player's sum is: ", True, (255, 255, 0))
text_surface10 = my_font.render("The Banker's sum is: ", True, (255, 255, 0))
text_surface11 = my_font.render("You lose!!!", True, (255, 255, 0))
text_surface12 = my_font.render("You win!!!", True, (255, 255, 0))
text_surface13 = my_font.render("Draw", True, (255, 255, 0))
text_surface14 = my_font.render("Your income: ", True, (255, 255, 0))
text_surface15 = my_font.render("Your property now: ", True, (255, 255, 0))
text_surface20 = my_font.render("100", True, (255, 255, 0))
text_surface21 = my_font1.render("Press 1:Player Hit", True, (255, 255, 0))
text_surface22 = my_font1.render("Press 2:Player Hold", True, (255, 255, 0))
text_surface23 = my_font1.render("Press 3:Player Double", True, (255, 255, 0))
screen.blit(text_surface1, (150, 100))
screen.blit(text_surface2, (300, 400))
file=r'Michael Hunter - Theme From San Andreas.mp3'		# 音乐的路径
track = pygame.mixer.music.load(file)
pygame.mixer.music.play(-1,0)
# 创建Clock的实例
clock = pygame.time.Clock()
# 主循环
step = 1
mRunning = True
while mRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mRunning = False
        if event.type == pygame.MOUSEBUTTONDOWN and step == 1:
            screen.blit(backGround2, [0, 0])
            screen.blit(text_surface3, (90, 100))
            screen.blit(text_surface19, (700, 100))
            money = 1000
            step = 2
            continue
        if event.type == pygame.MOUSEBUTTONDOWN and step == 2:
            screen.blit(text_surface4, (200, 300))
            reset_card()
            fresh_card()
            flagP = 0
            bjB = 0
            bjP = 0
            CB = 2
            CP = 2
            chb = 1
            chp = 1
            choose, doubled = 1, 0
            step = 3
            continue
        if event.type == pygame.MOUSEBUTTONDOWN and step == 3:
            screen.blit(backGround1, [0, 0])
            screen.blit(text_surface5, (200, 200))
            screen.blit(text_surface20, (520,200))
            bet = 100
            step = 4
            continue
        if event.type == pygame.MOUSEBUTTONDOWN and step == 4:
            text_surface6 = my_font.render("The bet for this turn: " + str(bet), True, (255, 255, 0))
            screen.blit(text_surface6, (200, 400))
            step = 5
            continue
        if event.type == pygame.MOUSEBUTTONDOWN and step == 5:
            screen.blit(backGround3, [0, 0])
            screen.blit(text_surface7, (90, 50))
            screen.blit(text_surface8, (90, 250))
            screen.blit(text_surface9, (90, 500))
            screen.blit(text_surface21, (900, 50))
            screen.blit(text_surface22, (900, 100))
            screen.blit(text_surface23, (900, 150))
            sumP = 0
            sumB = 0
            #banker
            for i in range(chb, CB + 1 + 1):
                B[i] = choice[choose]
                choose += 1
            chb = CB + 2
            for i in range(1, CB + 1):
                if i == 1 and flagP == 0:
                    backs = pygame.transform.scale(pygame.image.load("53.jpg"), (110, 150))
                    screen.blit(backs, [300 + 20 * i, 80])
                else:
                    print_card_B(B[i], i)
                blackjack_card_B(B[i])
                if B[i] == 11 or B[i] == 12 or B[i] == 13 or B[i] == 24 or B[i] == 25 or B[i] == 26 or B[i] == 37 or B[
                    i] == 38 or B[i] == 39 or B[i] == 50 or B[i] == 51 or B[i] == 52:
                    sumB += 10
                else:
                    sumB += (B[i] % 13)
            if flagP != 0:
                if bjB != 0 and sumB <= 11:
                    text_surface16 = my_font.render('The banker:' + str(sumB) + '/' + str(sumB + 10), True,
                                                    (255, 255, 0))
                    screen.blit(text_surface16, (600, 250))
                else:
                    text_surface16 = my_font.render('The banker:' + str(sumB), True, (255, 255, 0))
                    screen.blit(text_surface16, (600, 250))
                    bjB = 0
            #player
            for i in range(chp, CP + 1):
                P[i] = choice[choose]
                choose += 1
            chp = CP + 1
            for i in range(1, CP + 1):
                blackjack_card_P(P[i])
                if P[i] == 11 or P[i] == 12 or P[i] == 13 or P[i] == 24 or P[i] == 25 or P[i] == 26 or P[i] == 37 or P[
                    i] == 38 or P[i] == 39 or P[i] == 50 or P[i] == 51 or P[i] == 52:
                    sumP += 10
                else:
                    sumP += (P[i] % 13)
                print_card_P(P[i], i)
            if bjP != 0 and sumP <= 11:
                text_surface17 = my_font.render(str(sumP) + '/' + str(sumP + 10), True, (255, 255, 0))
                screen.blit(text_surface17, (600, 500))
            else:
                text_surface16 = my_font.render(str(sumP), True, (255, 255, 0))
                screen.blit(text_surface16, (600, 500))
                bjP = 0
            if sumP > 21:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    screen.blit(backGround4, [0, 0])
                    text_surface18 = my_font.render('The Player is BlustedYou lose!!!', True, (0, 255, 255))
                    screen.blit(text_surface18, (300, 300))
                    bet *= (-1)
                    money += bet
                    break
            step = 6
            continue
        if event.type == pygame.KEYDOWN and step == 6:
            if event.key == pygame.K_1:
                steps = 1
            elif event.key == pygame.K_2:
                steps = 2
            elif event.key == pygame.K_3:
                steps = 3
            if flagP == 0:
                move_card_P()
            if flagP == 2:
                move_card_B()
            if flagP == 1:
                flagP = 2
            if flagP == 3:
                check_card()
            step = 5
        clock.tick(30)
        pygame.display.flip()
pygame.quit()