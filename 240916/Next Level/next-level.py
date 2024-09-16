class Player:
    def __init__(self, id_, lv):
        self.id_ = id_
        self.lv = lv

player1 = Player('codetree', '10')
print(f'user {player1.id_} lv {player1.lv}')
id_, lv_ = input().split()
player2 = Player(id_, lv_)
print(f'user {player2.id_} lv {player2.lv}')