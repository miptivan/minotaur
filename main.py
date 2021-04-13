import gui
import game_loop

res = gui.main_menu()
print(res)
if res == 'go':
    print('yeah!!')
    game_loop.game_loop()