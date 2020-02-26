import pygame

from faker import Faker

fake = Faker("pl_PL")


class Postac:
    def __init__(self, screen, name, rys):
        self.rys = rys
        self.name = name
        self.screen = screen
        self.moc = fake.random.randint(1, 100)
        self.image = pygame.image.load(rys)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.polozenie = Polozenie.random()
        fake_name = fake.name()


        self.rect.x = self.polozenie.x
        self.rect.y = self.polozenie.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)



    @property
    def moc(self):
        return self._moc

    @moc.setter
    def moc(self, moc):
        self._moc = moc


class Polozenie:
    def __init__(self, x, y):
        self.x = x * 60 #+ 5
        self.y = y * 60

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"({self.x}, {self.y})"

    @classmethod
    def random(cls):
        return cls(fake.random.randint(1, 9), fake.random.randint(1, 9, ))


