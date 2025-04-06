import pygame # impordib vajalikud andmebaasid

pygame.init() #alustab mängu
aken = pygame.display.set_mode([640, 480]) #akna seaded
pygame.display.set_caption("Poemüüja - Rainer Hints ISK24")

taust = pygame.image.load("bg_shop.jpg") #taustapilt

troll = pygame.image.load("seller.png")#myyja seaded
troll = pygame.transform.scale(troll, (255, 305))

jutumull = pygame.image.load("chat.png") #jutumulli seaded
jutumull = pygame.transform.scale(jutumull, (255, 200))

aken.blit(taust, [0, 0]) #asukohad
aken.blit(troll, [105, 160])
aken.blit(jutumull, [247, 67])

font = pygame.font.Font(None, 35) #tekst
jutt = font.render("Rainer", True, [255, 255, 255])
aken.blit(jutt, [325, 145])
pygame.display.flip()

tootab = True #hoiab akent töös kuni aken suletakse
while tootab:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            tootab = False