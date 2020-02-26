import sys
import pygame



def check_events(postac, rzecz):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                postac.rect.y -= 60
                if postac.rect.y == -60:
                    postac.rect.y = 0

            if event.key == pygame.K_s:
                postac.rect.y += 60
                if postac.rect.y == 600:
                    postac.rect.y = 540

            if event.key == pygame.K_a:
                postac.rect.x -= 60
                if postac.rect.x == -60:
                    postac.rect.x = 0

            if event.key == pygame.K_d:
                postac.rect.x += 60
                if postac.rect.x == 600:
                    postac.rect.x = 540



def spotkanie(postac, postac1, rzecz, stats):

    if postac.rect.x == postac1.rect.x and postac.rect.y == postac1.rect.y:

        if postac.moc > postac1.moc:

            tekst1 = "Wygraleś"

            postac1.rect.x = 1000
            postac.moc = postac.moc - postac1.moc
            postac1.moc = 0
            stats.game_active = False
            return tekst1
        else:
            print("przegrałeś")
            tekst1 = "Przegrałeś"

            postac.rect.x = 1000
            postac.moc1 = postac1.moc - postac.moc
            postac.moc = 0
            stats.game_active = False
            return tekst1



    if postac.rect.x == rzecz.rect.x and postac.rect.y == rzecz.rect.y:

        rzecz.rect.x = 1000
        rzecz.rect.y = 1000
        postac.moc += 50



def update_screen(ai_settings, screen, postac, postac1, rzecz, siatka, tekst, stats):

    czcionka = pygame.font.SysFont(None, 30)
    screen.fill(ai_settings.bg_color)
    screen.blit(czcionka.render(f"Gracz 1: {postac.name}", 1, (0, 0, 0,)), (620, 10))
    screen.blit(czcionka.render(f"Moc : {postac.moc}", 1, (0, 0, 0,)), (620, 50))
    screen.blit(czcionka.render(f"Gracz 2: {postac1.name}", 1, (0, 0, 0,)), (620, 90))
    screen.blit(czcionka.render(f"Moc : {postac1.moc}", 1, (0, 0, 0,)), (620, 130))
    screen.blit(czcionka.render(tekst, 1, (0, 0, 0,)), (620, 170))
    postac.blitme()
    postac1.blitme()
    rzecz.blitme()
    siatka.draw_net()
    pygame.display.flip()
