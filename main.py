import pygame

pygame.init()  # inicializar o pygame

display = pygame.display.set_mode([500, 500])  # resolução de janela

pygame.display.set_caption("Meu Jogo")  # alterar titulo da janela


drawGroup = pygame.sprite.Group()

maça = pygame.sprite.Sprite(drawGroup) #sprite são objetos na tela
maça.image = pygame.image.load("data/maça.png.png") #citamos a img
maça.image = pygame.transform.scale(maça.image, [100,100]) #largura x altura
maça.rect = pygame.Rect(50,50,100,100) #retangulo criado na tela



gameLoop = True  # game loop para continuar a ser executada a janela
while gameLoop:

    for event in pygame.event.get():  # retronará a lista de todas as pessoas do pygame
        if event.type == pygame.QUIT:  # dessa forma a janela poderá ser fechada sem erros
            gameLoop = False

        keys = pygame.key.get_pressed() #vai pegar todas as teclas pressionadas

        if keys[pygame.K_w]:
            maça.rect.y -= 4 #ao pressionar w o eixo x soma 1 pixel ali
            print('indo para cima')
        if keys[pygame.K_s]:
            maça.rect.y += 4 # subtrai os pixels fazendo voltar
            print('Indo pra baixo')
        if keys[pygame.K_a]:
            maça.rect.x -= 4
            print('Indo para esquerda')
        if keys[pygame.K_d]:
            maça.rect.x += 4
            print('indo para direita')

    #draw
    display.fill([93, 178, 227])# cores de fundo

    drawGroup.draw(display)

    pygame.display.update()  # sempre que tiver game loop vai ficar com a janela até ocorrer algo
