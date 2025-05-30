class Entity(object):
    def __init__(self, node):
        ...
        self.image = None

    def render(self, screen):
        if self.visible:
             if self.image is not None:
                 screen.blit(self.image, self.position.asTuple())
             else:
                p = self.position.asInt()
                pygame.draw.circle(screen, self.color, p, self.radius)

