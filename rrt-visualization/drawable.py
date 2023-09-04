from abc import ABC, abstractmethod
from pygame.surface import Surface


class Drawable(ABC):  # ??? ABC 
    def __init__(self) -> None:
        super().__init__() # İnit ?

    @abstractmethod  # ???
    def draw(self, screen: Surface) -> None: # bu method nasıl çalışıyor ??? 
        ...
