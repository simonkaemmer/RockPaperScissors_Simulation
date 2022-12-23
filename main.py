from src.RPSObject import RPSCircle, Window, RPSType, kill_dead_sprites
import pygame
import time
import ctypes
import random

def go():
    ws = Window(800, 800) # Window Size
   
    pygame.init()
    pygame.display.set_caption("Rock Paper Scissors")
    window = pygame.display.set_mode(ws.getTupel())
    clock = pygame.time.Clock()

    all_groups = pygame.sprite.Group()
    stone = RPSCircle(RPSType.Stone, (250, 250), 5, (random.random(), random.random()), "./img/Stein.png")
    scissor = RPSCircle(RPSType.Scissors, (699, 699), 5, (random.random(), random.random()), "./img/Schere.png")
    paper = RPSCircle(RPSType.Paper, (101, 699), 5, (random.random(), random.random()), "./img/Papier.png")

    paper2 = RPSCircle(RPSType.Paper, (101, 699), 5, (random.random(), random.random()), "./img/Papier.png")
    paper3 = RPSCircle(RPSType.Paper, (101, 699), 5, (random.random(), random.random()), "./img/Papier.png")
    paper4 = RPSCircle(RPSType.Paper, (101, 699), 5, (random.random(), random.random()), "./img/Papier.png")

    all_groups.add(stone, scissor, paper)

    run = True
    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        all_groups.update()

        window.fill((144, 144, 144))
        all_groups.draw(window)

        for circle in all_groups:

            circle.reflect_if_collided(ws)
            kill_dead_sprites(all_groups)

            if not circle.alive:
                circle.kill()
                if len(all_groups.sprites()) == 1:
                    if ctypes.windll.user32.MessageBoxW(0, all_groups.sprites().pop().get_name()+ " won!!! Again?", "Rock Paper Scissors", 4) == 6:
                        pygame.display.quit()
                        pygame.quit()
                        run = True
                        go()
                    else:
                        quit()

        pygame.display.flip()
    

def main():
    if ctypes.windll.user32.MessageBoxW(0, "Go?", "Rock Paper Scissors", 4) == 6:
        go()

if __name__ == "__main__":
    main()
