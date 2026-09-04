import pygame 
import sys

#1. Initialize Pygame subsystems 
pygame.init()

#2. Window Setup 
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sunken Crypt - 2D Prototype")

#3. Framerate Controller 
clock = pygame.time.Clock() 

#Color definitions(Red, Green, Blue)
DARK_GRAY =(30, 30, 30)
HERO_BLUE =(50, 150, 255)

#Use a 2D Vector for position 
player_pos = pygame.math.Vector2(300, 200)
player_speed = 5 

#Controller for the loop 
running = True
# --- The Main Pygame Loop --- 
while running:
    #A EVENT HANDLING 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #B. INPUT & STATE UPDATES 
    keys = pygame.key.get_pressed()
    
    direction = pygame.math.Vector2(0, 0)
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        direction.x -= 1
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        direction.x += 1
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        direction.y -= 1
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        direction.y += 1

    #2 Normalize if the player is actully moving 
    if direction.length() > 0:
        direction = direction.normalize()

    #3 Apply normalized direction scaled by speed
    player_pos += direction * player_speed 

    
    #C. DRAWING / RENDERING 
    # Fill the screen with backgroud color to wipe the previous frame 
    screen.fill(DARK_GRAY)

    pygame.draw.rect(screen, HERO_BLUE, (int(player_pos.x), int(player_pos.y), 32, 32))


    #Display the newly draw frame on the monitor 
    pygame.display.flip()

    #D. CAP FRAMERATE 
    clock.tick(60)

#Clean shutdown
pygame.quit()
sys.exit()
