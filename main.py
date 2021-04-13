import gui
import game_loop

res = gui.main_menu()
print(res)
if res == 'go':
    game_loop.game_loop()