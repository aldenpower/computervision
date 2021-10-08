import cv2
from numpy.core.numeric import count_nonzero
from skimage import io

class Image():
    def __init__(self, img):
        self.img_ = io.imread(img)

    def shape(self):
        print("(largura, altura, canais)")
        print(self.img_.shape)

    def conversion(self, tipo):
        if tipo == 'rgb':
            converted = cv2.cvtColor(self.img_, cv2.COLOR_BGR2RGB)
        if tipo == 'gray':
            converted = cv2.cvtColor(self.img_, cv2.COLOR_RGB2GRAY)

        return converted

    def showimage(self, name = 'image'):
        cv2.imshow(name, self.img_)
        # Digite qualquer tecla para fechar a imagem
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    def blur(self):
        blur = cv2.GaussianBlur(self.img_, (7,7), 10)

        return blur

    def gray_blur(self):
        gray = self.conversion('gray')

        blur = cv2.GaussianBlur(gray, (7,7), 10)

        return blur
