#First step is to import and initialize pygame modules with the help of init() function.
import pygame,sys
pygame.init()
#We now set up Pygame display window of preferred size, and give it a caption.
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Atoms")
white = (255,255,255)
while True:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         pygame.quit()
         sys.exit()
   pygame.draw.circle(screen, white, (180,180), 60,2)
   pygame.draw.circle(screen, white, (0,180), 60,2)

  # pygame.draw.circle(screen, white, (180,180), 120,2)
   pygame.display.update()