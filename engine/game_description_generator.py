from typing import List

class GameDescriptionGenerator:
    def generate_game_description(self, game_moves: str) -> List[str]:
        moves = list(game_moves.split(' '))

        pairs = []
        for i in range(0, len(moves), 2):
            if i + 1 < len(moves):
                pairs.append(f'{moves[i]} {moves[i + 1]}')
            else:
                pairs.append(moves[i])

        description = ''

        for i, pair in enumerate(pairs):
            description += f'{i + 1}. {pair} '

        return description
