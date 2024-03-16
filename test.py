from tools.game_id_extractor import GameIDExtractor
from engine.game_loader import GameLoader
from engine.game_description_generator import GameDescriptionGenerator
from gifpgn import CreateGifFromPGN


game_url = 'https://lichess.org/cadc6n8G'

game_id = GameIDExtractor().extract_game_id(game_url=game_url)

game = GameLoader().load_game(game_id=game_id)

moves = game['moves']
print(moves)

description = GameDescriptionGenerator().generate_game_description(game_moves=moves)

print(description)

gif = CreateGifFromPGN(description)


gif.generate(output_file='chess.gif')
