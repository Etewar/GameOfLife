import pygame, sys
from pygame.locals import *

pygame.init()
pygame.display.set_caption("Game of life")

rows = 30
cols = 50
cell_size = 20

screen = pygame.display.set_mode((cell_size*cols, cell_size*rows))
W = (255, 255, 255)
B = (0, 0, 0)

pause = -1

def clear_console():
    print("\033[H\033[J")

def input(events):
    for event in events:
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            sys.exit(0)
        if event.type == KEYDOWN and event.key == K_p:
            App.p *= -1
        else:
            clear_console()
            print(event)

class Cell:

    def __init__(self, pos_x, pos_y, state = 0):
        self.x = pos_x
        self.y = pos_y
        self.state = state

    def alive(self):
        self.state = 1
        pos = (self.x*cell_size, self.y*cell_size)
        pygame.draw.rect(screen, W, (*pos, cell_size, cell_size))
        #screen.set_at(pos, W)
        pygame.display.update(pos, (cell_size, cell_size))

    def dead(self):
        self.state = 0
        pos = (self.x*cell_size, self.y*cell_size)
        pygame.draw.rect(screen, B, (*pos, cell_size, cell_size))
        #screen.set_at(pos, B)
        pygame.display.update(pos, (cell_size, cell_size))







class App:
    board = [[Cell(x, y) for x in range(cols)] for y in range(rows)]
    p = 1
    def check_cells():
        new_board = [[Cell(x, y) for x in range(cols)] for y in range(rows)]

        for y in range(rows):
            for x in range(cols):
                neighbours = 0
                for h in range(-1, 2):
                    for w in range(-1, 2):
                        neighbours += App.board[(y+h) % rows][(x+w) % cols].state
                neighbours -= App.board[y][x].state
                if App.board[y][x].state == 1 and (neighbours == 2 or neighbours == 3):
                    new_board[y][x].state = 1
                    pygame.draw.rect(screen, W, (x*cell_size, y*cell_size, cell_size, cell_size))
                elif App.board[y][x].state == 0 and neighbours == 3:
                    new_board[y][x].state = 1
                    pygame.draw.rect(screen, W, (x*cell_size, y*cell_size, cell_size, cell_size))
                else:
                    new_board[y][x].state = 0
                    pygame.draw.rect(screen, B, (x*cell_size, y*cell_size, cell_size, cell_size))

        pygame.display.update()
        App.board = new_board


    def run():
        i = 0
        sec = .2
        while True:
            input(pygame.event.get())
            mouseX, mouseY = pygame.mouse.get_pos()

            if pygame.mouse.get_pressed()[0]:
                App.board[mouseY//cell_size][mouseX//cell_size].alive()

            elif pygame.mouse.get_pressed()[2]:
                App.board[mouseY//cell_size][mouseX//cell_size].dead()

            if App.p == 1:
                if i == 1000*sec:
                    App.check_cells()
                    i = 0
                i += 1
                #pygame.display.update()
            pygame.time.delay(1)

if __name__ == "__main__":
    App.run()
