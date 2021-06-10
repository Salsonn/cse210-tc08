from game import output_service
from game.action import Action

class DrawActorsAction(Action):
    
    def __init__(self, output_service):
        self._outputService = output_service

    def execute(self, cast):
        self._outputService.clear_screen()
        for i in cast.values():
            self._outputService.draw_actors(i)
        self._outputService.flush_buffer()