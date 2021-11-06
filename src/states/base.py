class Base:
    """ This is a class template. All the other classes will be made according to this templae """
    
    def __init__(self) -> None:
        """ constructor function """
        pass
    
    def enter(self, **param) -> None:
        """ This function is called first when we change a group """
        pass
        
    def render(self) -> None:
        """ This function will render all the current objects on the screen """
        pass
    
    def update(self, param) -> None:
        """ This function will be called once per frame"""
        
        pass
        
    def leave(self) -> None:
        """ This function will be called during changing state. It helps in leaving the current state """
        pass