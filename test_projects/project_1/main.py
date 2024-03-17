import pygame
from game_model import GameModel
from game_view import GameView
from game_controller import GameController

def main():
    pygame.init()
    model = GameModel()
    view = GameView(model)
    controller = GameController(model)

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                controller.handle_event(event)

        controller.update()
        view.render()
        clock.tick(10)  # Run the game at 10 frames per second

    pygame.quit()

if __name__ == "__main__":
    main()