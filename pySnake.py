import curses
import random

screen = curses.initscr() # Inicia uma janela
curses.curs_set(0) 
alt, lar = screen.getmaxyx()
newScreen = curses.newwin(alt, lar, 0 ,0)
newScreen.keypad(True)
newScreen.timeout(100)

snk_x = int(lar/2)
snk_y = int(alt/2)

snake = [[snk_y, snk_x], 
        [snk_y-1, snk_x], 
        [snk_y-2, snk_x]
        ] 
# Cria uma cobra, descendo em Y

food = [int(alt/2), int(lar/4)]
newScreen.addch(food[0], food[1], 'x')
key = curses.KEY_RIGHT

while(True):
    next_key = newScreen.getch()
    key = key if next_key == -1 else next_key

           # Se a cobra estiver em lugar proibido fecha o programa
    
    new_head = [snake[0][0], snake[0][1]] # cria a primeira cobra
    
    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    snake.insert(0, new_head)

    if snake[0] == food:
        food = None
        while food is None:
            new_food = [
                random.randint(1, alt-1),
                random.randint(1, lar-1)
            ]
            food = new_food if new_food not in snake else None
        newScreen.addch(food[0], food[1], 'x')
    else:
        tail = snake.pop()
        newScreen.addch(tail[0], tail[1], ' ')
    if snake[0][0] in [0, alt] or snake[0][1] in [0,lar] or snake[0] in snake[1:]:
        curses.endwin()
        quit()
    newScreen.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)



# import random
# import curses

# s = curses.initscr()
# curses.curs_set(0)
# sh, sw = s.getmaxyx()
# w = curses.newwin(sh, sw, 0, 0)
# w.keypad(1)
# w.timeout(100)

# snk_x = int(sw/4)
# snk_y = int(sh/2)
# snake = [
#     [snk_y, snk_x],
#     [snk_y, snk_x-1],
#     [snk_y, snk_x-2]
# ]

# food = [int(sh/2), int(sw/2)]
# w.addch(food[0], food[1], curses.ACS_PI)
# while True:
#     w.addch(food[0], food[1], curses.ACS_PI)