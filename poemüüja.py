import pygame

pygame.init()
aken = pygame.display.set_mode([640, 480])
pygame.display.set_caption("Mängunimi")

taust = pygame.image.load("bg_shop.jpg")

troll = pygame.image.load("seller.png")
troll = pygame.transform.scale(troll, (255, 305))

jutumull = pygame.image.load("chat.png")
jutumull = pygame.transform.scale(jutumull, (255, 200))

aken.blit(taust, [0, 0])
aken.blit(troll, [105, 160])
aken.blit(jutumull, [247, 67])

font = pygame.font.Font(None, 35)
jutt = font.render("Rainer", True, [255, 255, 255])
aken.blit(jutt, [325, 145])
pygame.display.flip()

tootab = True
while tootab:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            tootab = False