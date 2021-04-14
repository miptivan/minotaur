import pygame
import pygame_gui


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def find_game_menu():
    pygame.init()
    pygame.display.set_caption('Quick Start')
    window_surface = pygame.display.set_mode((800, 600))

    background = pygame.Surface((800, 600))
    background.fill(pygame.Color('#000000'))

    manager = pygame_gui.UIManager((800, 600))

    text_element = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((300, 200), (200, 50)), 
                                                    manager=manager)

    hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 270), (100, 50)),
                                                text='Say Hello',
                                                manager=manager)

    clock = pygame.time.Clock()
    is_running = True

    while is_running:
        time_delta = clock.tick(60)/1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

            manager.process_events(event)

            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == hello_button:
                        ip, port = text_element.text.split(':')
                        is_running = False

        manager.update(time_delta)

        window_surface.blit(background, (0, 0))
        manager.draw_ui(window_surface)

        pygame.display.update()


def main_menu():
    pygame.init()
    pygame.display.set_caption('Quick Start')
    window_surface = pygame.display.set_mode((800, 600))
    background = pygame.Surface((800, 600))
    background.fill(pygame.Color('#000000'))

    manager = pygame_gui.UIManager((800, 600))
    nick_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((310, 180), (85, 50)),
                                             text='Nickname: ',
                                             manager=manager)
    nickname_textBox = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((390, 190), (100, 50)),
                                                    manager=manager)
    new_game_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 250), (100, 50)),
                                                text='New game',
                                                manager=manager)
    find_game_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 310), (100, 50)),
                                                    text='Find game',
                                                    manager=manager)
    clock = pygame.time.Clock()
    is_running = True

    while is_running:
        time_delta = clock.tick(60)/1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

            manager.process_events(event)

            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == find_game_button:
                        find_game_menu()
                        is_running = False
                    if event.ui_element == new_game_button:
                        res = new_game_menu()
                        if res == 'go':
                            return 'go'

        manager.update(time_delta)

        window_surface.blit(background, (0, 0))
        manager.draw_ui(window_surface)

        pygame.display.update()


def new_game_menu():
    pygame.init()
    pygame.display.set_caption('Quick Start')
    window_surface = pygame.display.set_mode((800, 600))

    background = pygame.Surface((800, 600))
    background.fill(pygame.Color('#000000'))

    manager = pygame_gui.UIManager((800, 600))

    schetchik = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((350, 190), (100, 50)),
                                            text='1 user',
                                            manager=manager)

    start_game_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 310), (100, 50)),
                                                text='Start game',
                                                manager=manager)

    clock = pygame.time.Clock()
    is_running = True

    while is_running:
        time_delta = clock.tick(60)/1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

            manager.process_events(event)

            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == start_game_button:
                        print('The game is coming!!!')
                        # is_running = False
                        return 'go'

        manager.update(time_delta)

        window_surface.blit(background, (0, 0))
        manager.draw_ui(window_surface)
        draw_text('main menu', pygame.font.SysFont(None, 20), (255, 0, 0), window_surface, 20, 20)

        pygame.display.update()
