

class Statemachine:
    """
        This class will help keep track of different states in the game.
        It will also be useful while changing the states
    """
    
    def __init__(self, states) -> None:
    
        """
            Contructor function
        """
        
        self.states = states
        self.current = None
        
    def change(self, state, **param) -> None:
    
        """ This function is called while changing the state """
        
        if not state in states: return
        
        if self.current:
            self.current.leave()
        
        self.current = states[state]
        self.current.enter(**param)
        
    def render(self) -> None:
        """ This function will render all the current objects on screen"""
        
        self.current.render()
    
    def update(self, events) -> None:
        """ This function will update the current function """
        
        self.current.update()