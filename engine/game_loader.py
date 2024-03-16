from core.client import client


class GameLoader:
    def load_game(self, game_id: str):
        return client.games.export(game_id=game_id, as_pgn=False, moves=True, tags=False)