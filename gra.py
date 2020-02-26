import sys
import pygame

from settings import Settings
from postac import Postac
import gra_funkcje as gf
from siatka import Siatka
from gra_status import GraStatus
from faker import Faker
from time import sleep

fake = Faker("pl_PL")

def run_game():
    pygame.init()
    ai_settings = Settings()
    f_name = fake.first_name()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_high))
    pygame.display.set_caption("Fight of man")

    stats = GraStatus(ai_settings)
    postac = Postac(screen, "Heros", rys="ryc_1.png")
    postac1 = Postac(screen,f_name , rys="kolo.png")

    if postac.polozenie == postac1.polozenie:
        postac1 = Postac(screen,f_name , rys="kolo.png")

    print(postac1.moc)
    rzecz = Postac(screen, "rzecz", rys="kolo.png")

    siatka = Siatka(screen)

    while True:

        gf.check_events(postac, rzecz)

        if stats.game_active:
            tekst = gf.spotkanie(postac, postac1, rzecz, stats)
            gf.update_screen(ai_settings, screen, postac, postac1, rzecz, siatka, tekst, stats)


run_game()
