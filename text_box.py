import pygame

# create input boxes
class InputBox:
    def __init__(self, width, height, x, y, font, window, text, update_text, index):
        self.rect = pygame.Rect(width, height, x, y)
        self.text = text
        self.color = '#FFFFFF'
        self.box_color = '#354B5E'
        self.font = font
        self.window = window
        self.active = False
        self.update_text = update_text
        self.index = index


    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False

        if event.type == pygame.KEYDOWN:
            if self.active:
                self.text = event.unicode
                self.update_text(self.index, self.text)


    def draw_textbox(self):
        pygame.draw.rect(self.window, self.box_color, self.rect, 5)
        font_surface = self.font.render(self.text, True, self.color)
        self.window.blit(font_surface, (self.rect.x + 75, self.rect.y + 14))


    def reset(self):
        self.text = ''
