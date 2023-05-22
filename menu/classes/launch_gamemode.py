from menu.tools.cnf_load import load as cnf_load
from menu.classes.gamemode import Gamemode
from menu.interfaces.game_interface import GameInterface
from menu.classes.piece import Piece
from menu.classes.matrix import Matrix

class GamemodeLauncher:
    def __init__(self, gamemode_index: int):
        self.matrix = Matrix()

        config = cnf_load()

        shapes = config["shapes"]

        try:
            raw_gamemode = config["gamemodes"][gamemode_index]
        except IndexError:
            raise IndexError("Gamemode index out of range")

        # Convert the list of shapes index into a valid list of shapes
        list_pieces = [
            Piece(shapes[shape_index]["color"], shapes[shape_index]["scheme"], self.matrix) for shape_index in raw_gamemode["shapes"]
        ]

        self.gamemode = Gamemode(
            name=raw_gamemode["name"],
            id=raw_gamemode["id"],
            default_speed=raw_gamemode["default_speed"],
            speed_multiplier=raw_gamemode["speed_multiplier"],
            speed_increment_every=raw_gamemode["speed_increment_every"],
            max_speed=raw_gamemode["max_speed"],
            pieces=list_pieces,
            invisible_pieces=raw_gamemode["invisible"],
            xp_multiplier=raw_gamemode["xp_multiplier"]
        )

    def launch(self):
        self.gamemode.start()

        game_interface = GameInterface(self.gamemode, self.matrix)

        game_interface.process()
