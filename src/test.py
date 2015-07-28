import sys, pygame

class Speed:
    GO_FORWARD = 1
    GO_BACKWARD = -1
    STOP = 0
    X = 0
    Y = 1

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def vector(self):
        return [self.x, self.y]
        
    def recalculate_for(self, current_position, destination):
        self.x = self._direction_for(current_position[self.X], destination[self.X])
        self.y = self._direction_for(current_position[self.Y], destination[self.Y])

    def _direction_for(self, current, destination):
        if current < destination: return self.GO_FORWARD
        elif current > destination: return self.GO_BACKWARD
        return self.STOP 

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
