import pygame
from game import Game

pygame.init()

# creer la seconde classs game


# generer la fenetre
pygame.display.set_caption("SnowGame")
screen = pygame.display.set_mode((1080, 720))

# charger le jeux
game = Game()

# background
background = pygame.image.load('assets/bg.jpg')

running = True
# boucle pour laisser la fentetre ouverte
while running:
    # appliquer la fenetre
    screen.blit(background, (0, -200))

    # appliquer l'image du joueur
    screen.blit(game.player.image, game.player.rect)

    # recuperer les projectiles du joueur
    for projectile in game.player.all_projectile:
        projectile.move()

    # appliquer les imageds du projectile
    game.player.all_projectile.draw(screen)

    # verifier si le joueur souhaite aller a gauche ou a droite
    if game.pressed.get(pygame.K_a) and game.player.rect.x > 0:
        game.player.move_left()
    elif game.pressed.get(pygame.K_d) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()

    # maj
    pygame.display.flip()

    for event in pygame.event.get():
        # verifier que l'evenement est la fermeture de la fenetre
        if event.type == pygame.QUIT:
            running = False
            print("Fermeture du jeux")
            pygame.quit()

        # detecter si touche enclencher
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            #detecter si la touche espace est enclenche
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
