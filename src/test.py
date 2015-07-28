import sys, pygame
pygame.init()

size = width, height = 1024, 768
speed = [0, 0]
black = 0, 0 ,0

screen = pygame.display.set_mode(size)

bee = pygame.image.load("src/bee.png")
beerect = bee.get_rect()


def move_bee_to_position(beerect, position):
  speed = [0, 0]
  if beerect.x < position[0]: speed[0] = 1
  elif beerect.x > position[0]: speed[0] = -1
  else: speed[0] = 0
  if beerect.y < position[1]: speed[1] = 1
  elif beerect.y > position[1]: speed[1] = -1
  else: speed[1] = 0
  return speed

target = [beerect.x, beerect.y]
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: sys.exit()
    if event.type == pygame.MOUSEBUTTONDOWN:
      target = event.pos
  speed = move_bee_to_position(beerect, target)
  beerect = beerect.move(speed)

  print "Target", target
  print "Current speed", speed
  print "Current position", beerect.x, beerect.y
  beerect.move(speed)
  screen.fill(black)
  screen.blit(bee, beerect)
  pygame.display.flip()
