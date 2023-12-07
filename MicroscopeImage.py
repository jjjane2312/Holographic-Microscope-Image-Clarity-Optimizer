import cv2

class MicroscopeImage:
    def __init__(self, img_url) -> None:
        self.image = cv2.imread(img_url)
    
    def get_image_tensor(self):
        return self.image

class DummyMicroscopeImage(MicroscopeImage):
    def __init__(self, img_focus, img_url) -> None:
        super().__init__(img_url)
        self.img_focus = img_focus
    
    def get_focus(self):
        return self.img_focus
        