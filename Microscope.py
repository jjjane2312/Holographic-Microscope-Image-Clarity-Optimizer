from abc import ABC, abstractmethod
import os 
import random
import cv2

class MicroscopeController(ABC):
    @abstractmethod
    def get_image(self):
        pass

    @abstractmethod
    def move(self, move_amount):
        pass

    @abstractmethod
    def is_move_legal(self, move_amount):
        pass

class DummyMicroscopeController(MicroscopeController):
    def __init__(self) -> None:
        super().__init__()
        self.image_focuses = [-3.0, -2.5, -2.0, -1.5, -1.0, -0.5, 0.0 , 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
        self.image_idx = random.randint(1, len(self.image_focuses)-2) #important this should not start with either of the extremes
        self.image = cv2.imread(self.get_image_path())
    
    def get_current_focus(self):
        return self.image_focuses[self.image_idx]
    
    def get_image_path(self):
        if self.image_focuses[self.image_idx] < 0.0:
            return os.path.join("dummy_images", f"haydarpasa{self.image_focuses[self.image_idx]}.jpg")
        else:
            return os.path.join("dummy_images", f"haydarpasa+{self.image_focuses[self.image_idx]}.jpg")
    
    def move(self, move_amount):
        if self.is_move_legal(move_amount):
            new_focus = self.image_focuses[self.image_idx] + move_amount
            self.image_idx = self.image_focuses.index(new_focus)
            self.image = cv2.imread(self.get_image_path())
        else:
            raise Exception("Move is not legal")
    
    def is_move_legal(self, move_amount):
        if self.image_idx + move_amount < 0 or self.image_idx + move_amount >= len(self.image_focuses):
            return False
        else:
            return True
    
    def get_image(self):
        return self.image
    
if __name__ == "__main__":
    controller = DummyMicroscopeController()

    for i in range(13):
        controller.image_idx = i
        print(controller.get_image_path())

    
    
    


