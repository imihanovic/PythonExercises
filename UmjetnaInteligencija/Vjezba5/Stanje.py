class Stanje:
    P1 = "Human"
    P2 = "Bot"
    def __init__(self):
        self.sticks = 11
        self.turn = self.P1
        
    def __str__(self):
        return f"""Sticks left: {str(self.sticks)}
Winner: {self.get_winner()}
"""
    def all_actions(self):
        return [1,2]
    
    def change_turn(self):
        self.turn = self.P1 if self.turn == self.P2 else self.P2
        
    def do_action(self, raised):
        self.sticks -= raised
        self.change_turn()
    
    def undo_action(self, raised):
        self.sticks += raised
        self.change_turn()
        
    def get_winner(self):
        if self.turn == self.P1:
            return self.P2
        return self.P1
    
    def game_over(self):
        if self.sticks == 0 or self.sticks == 1:
            return self.get_winner()
        return False
        