import sys, pygame

class Speed:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def vector(self):
        return [self.x, self.y]
        
    def recalculate_for(self, current_position, destination):
        self.x = self._x_for(current_position, destination)
        self.y = self._y_for(current_position, destination)

    def _x_for(self, current_position, destination):
        if current_position[0] < destination[0]: return 1
        elif current_position[0] > destination[0]: return -1
        return 0

    def _y_for(self, current_position, destination):
        if current_position[1] < destination[1]: return 1
        elif current_position[1] > destination[1]: return -1
        return 0

class Bee:
    def __init__(self, rectangle):
        self.rectangle = rectangle
        self.speed = Speed(0, 0)

    def move_to(self, destination):
        self.speed.recalculate_for(self.current_position(), destination)
        self.rectangle = self.rectangle.move(self.speed.vector())

    def get_rectangle(self):
        return self.rectangle

    def current_position(self):
        return [self.rectangle.x, self.rectangle.y]

pygame.init()

size = width, height = 1024, 768
speed = [0, 0]
black = 0, 0 ,0

screen = pygame.display.set_mode(size)

bee_icon = pygame.image.load("src/bee.png")
beerect = bee_icon.get_rect()
bee = Bee(beerect)

target = bee.current_position()

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: sys.exit()
    if event.type == pygame.MOUSEBUTTONDOWN:
      target = event.pos
  bee.move_to(target)
  screen.fill(black)
  screen.blit(bee_icon, bee.get_rectangle())
  pygame.display.flip()
