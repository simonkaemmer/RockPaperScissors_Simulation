from src.RPSObject import RPSCircle, Window, RPSType, find_collisions, reflectBalls, window_collisions
import pygame
import itertools
import ctypes
import random

def go():
    ws = Window(800, 800) # Window Size
   
    pygame.init()
    pygame.display.set_caption("Rock Paper Scissors")
    window = pygame.display.set_mode(ws.getTupel())
    clock = pygame.time.Clock()

    all_groups = pygame.sprite.Group()

    stone = RPSCircle(RPSType.Stone, (250, 250), 5, (random.random(), random.random()))
    stone2 = RPSCircle(RPSType.Stone, (350, 350), 5, (random.random(), random.random()))
    scissor = RPSCircle(RPSType.Scissors, (699, 699), 5, (random.random(), random.random()))
    scissor2 = RPSCircle(RPSType.Scissors, (599, 599), 5, (random.random(), random.random()))
    paper = RPSCircle(RPSType.Paper, (101, 699), 5, (random.random(), random.random()))

    paper2 = RPSCircle(RPSType.Paper, (201, 699), 5, (random.random(), random.random()))
    paper3 = RPSCircle(RPSType.Paper, (301, 699), 5, (random.random(), random.random()))
    paper4 = RPSCircle(RPSType.Paper, (401, 699), 5, (random.random(), random.random()))

    all_groups.add(stone, stone2, scissor, scissor2, paper, paper2)

    run = True
    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        all_groups.update()

        window.fill((144, 144, 144))
        all_groups.draw(window)

        window_collisions(all_groups, ws)

        for a, b in itertools.permutations(all_groups, 2):
            reflectBalls(a, b)
        
        if all(sprite.type.name == all_groups.sprites()[0].type.name for sprite in all_groups):
            winner = all_groups.sprites()[0].type.name
            ctypes.windll.user32.MessageBoxW(0, winner + " won!", "Winner: " + winner, 0)
            pygame.display.quit()
            pygame.quit()
            quit()
        pygame.display.flip()
    

def main():
    if ctypes.windll.user32.MessageBoxW(0, "Go?", "Rock Paper Scissors", 4) == 6:
        go()

if __name__ == "__main__":
    main()
