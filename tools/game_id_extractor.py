class GameIDExtractor:

    def extract_game_id(self, game_url: str) -> str:
        return game_url.split("/")[-1]