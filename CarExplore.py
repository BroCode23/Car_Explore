import pygame, math
#COLORS
GREEN = (76, 175, 80)
GREY = (158, 158, 158)
RED = (255, 0, 0)
#Variables to easily change acceleration and turn values
acc = 0.8
turn = 0.06
#Variables for car
tirech = 0
tire = 0
rochange = 0
rotation = 0
a = 0
v = 0
t = -2
paty = 330
patx = 510
yellchx = 0
yellchy = 0
yellturn = 0
yellrot = 0
PlyrC = pygame.image.load("Car.png")
YellC = pygame.image.load("Car4.png")
RedC = pygame.image.load("CarT.png")
City = pygame.image.load("World3.png")
Garden = pygame.image.load("World2.png")
two = math.sqrt(2)
# Function to rotate an image around its center
def rot_center( image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image

pygame.init()

# Set up Window
grass = pygame.display.set_mode([500,500])
pygame.display.set_caption("Car Adventure")

x = -110
y = -260
clock = pygame.time.Clock()
done = False
while not done:
    # Checks each event in the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                tirech = turn
            if event.key == pygame.K_RIGHT:
                tirech = -1 * turn
            if event.key == pygame.K_UP:
                a = acc
            if event.key == pygame.K_DOWN:
                a = -2 * acc / 3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                a = 0
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                tirech = 0
    # Doesn't let car tires turn past 2
    if abs(tire + tirech) > 8 * turn:
        pass
    else:
        tire += tirech
    # Friction and slowdown
    if v != 0:
        if v > 0:
            v -= acc / 5
        if v < 0:
            v += acc / 5
        if abs(v) < acc / 5:
            v = 0
        #Tires move slowly back to straight forwards
        if not tirech:
            if tire > 0:
                tire -= 2 * turn / 5
            if tire < 0:
                tire += 2 * turn / 5
            if abs(tire) < 2* turn / 5:
                tire = 0
    rotation += tire * v
    # Calculate speed and direction
    if abs(v + a) > 15 * acc:
        pass
    else:
        v = v + a
    x -= v * math.cos(-1 * rotation * math.pi / 180)
    y -= v * math.sin(-1 * rotation * math.pi / 180)

    # if the car goes out of bounds
    if not -1713 < x < 230 or not -713 < y < 230:
        if x < -1713:
            x = -1710
        if x > 230:
            x = 225
        if y < -713:
            y = -710
        if y > 230:
            y = 225

    # Yellow Car patrol path
    #patrols between y + 100 and 330, x stays at x + 510
    if t < 45: #90
        yellchx = 0
        yellchy = -6
        yellturn = 0
    elif t < 75: #150
        yellchx = -two
        yellchy = -two
        yellturn = 3
    elif t < 140: #280
        yellchx = -6
        yellchy = 0
        yellturn = 0
    elif t < 170: #340
        yellchx = -two
        yellchy = two
        yellturn = 3
    elif t < 235: #450
        yellchx = 0
        yellchy = 6
        yellturn = 0
    elif t < 265: #510
        yellchx = two
        yellchy = two
        yellturn = 3
    elif t < 330: #640
        yellchx = 6
        yellchy = 0
        yellturn = 0
    elif t < 360: #700
        yellchx = two
        yellchy = -two
        yellturn = 3
    elif t < 381: #720
        yellchx = 0
        yellchy = -6
        yellturn = 0
    elif t >= 370:
        t = 0
        paty = 310
        yellrot = 0
    patx += yellchx
    paty += yellchy
    yellrot += yellturn
    t += 1
    # Draw Everything

    # Fill in Background
    grass.fill(GREEN)
    grass.blit(City,[x,y])
    if x < -520:
        grass.blit(Garden, [x + 1000, y])
    # Draw the player's Car
    grass.blit(rot_center(RedC, rotation), [230, 230])
    # Computer Cars
    #Red Car
    if -45 < x + 350 < 500 and -55 < y + 320 < 500:
        grass.blit(PlyrC, [x + 350, y + 320])
    #Yellow Car
    if -55 < x + patx < 500 and -55 < y + paty < 500:
        grass.blit(pygame.transform.rotate(YellC, yellrot), [x + patx, y + paty])
    #grass.blit(pygame.transform.rotate(pygame.image.load("Car4.png"), 180), [x + patx, y + paty])
    # Mini-Map
    pygame.draw.rect(grass, GREY, [420, 20, 60, 60])
    pygame.draw.rect(grass, RED, [2.8 *(20 - ((x + 713) // 46)) + 420, 2.7 *(20 - ((y + 713) // 46)) + 20, 5, 5])

    # Update Display
    pygame.display.flip()
    clock.tick(50)

pygame.quit()