import pygame

class Siatka:
    def __init__(self, screen):
        self.screen = screen

    def draw_net(self):
        """
        Rysuje siatkę linii na planszy
        """
        color = (0, 0, 0)
        width = self.screen.get_width()
        for i in range(1, 10):
            pos = (width - 300) / 10 * i
            # linia pozioma
            pygame.draw.line(self.screen, color, (0, pos), ((width - 300), pos), 1)
            # linia pionowa
        for i in range(11):
            pos = (width - 300) / 10 * i
            pygame.draw.line(self.screen, color, (pos, 0), (pos, width), 1)