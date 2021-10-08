#!/home/mr-alden/pythonenvs/visionenv/bin/python3
import cv2
import numpy as np
from skimage import io
from utilities import Image


# Conf.
cards = Image('img/cards.jpg')
converted = cards.conversion('rgb')
converted2 = cards.conversion('rgb')

# Tamanho da carta
width, height = 250, 350

# Coordenadas atuais dos 4 vértices das cartas
pts1 = np.float32([[10,127],[149,40],[144,300],[257,205]])
pts1_2 = np.float32([[192,11],[355,31],[155,283],[335,277]])
pts1_3 = np.float32([[281,123],[450,134],[278,358],[456,370]])
pts1_4 = np.float32([[114,223],[289,193],[155,483],[352,440]])

# Coordenadas desejadas da projeção
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

# Definindo circulo para os pontos atuais
#cv2.circle(converted,(10,127),2,(255,255,0),5)
#cv2.circle(converted,(149,40),2,(255,255,0),5)
#cv2.circle(converted,(257,205),2,(255,255,0),5)
#cv2.circle(converted,(144,300),2,(255,255,0),5)

#Marcação das 4 linhas (VERDE)
#cv2.line(converted,(0,0),(10,127),(0,255,0),3)
#cv2.line(converted,(width,0),(149,40),(0,255,0),3)
#cv2.line(converted,(0,height),(144,300),(0,255,0),3)
#cv2.line(converted,(width,height),(257,205),(0,255,0),3)

# Retângulo representando a posição desejada (VERMELHO)
#cv2.rectangle(converted,(0,0),(width,height),(0,0,255),3)

# Matriz de Transformação de Perspectiva
matrix = cv2.getPerspectiveTransform(pts1_2,pts2)

# Distorção de Perspectiva
imgOutput = cv2.warpPerspective(converted,matrix,(width,height))

imgCropped = imgOutput[0:160,0:250]
imgCropped_k = imgOutput[0:160,0:250]
imgCropped180 = cv2.rotate(imgCropped, cv2.ROTATE_180)
imgCropped_k180 = cv2.rotate(imgCropped_k, cv2.ROTATE_180)

v_img = cv2.vconcat([imgCropped, imgCropped_k180])

if __name__ == '__main__':
    #cv2.imshow('converted', converted)
    #cv2.imshow('perespectiva copas', imgOutput)
    #cv2.imshow('cropped', imgCropped)
    cv2.imshow('vertical', v_img)
    #cv2.imshow('cropped k', imgCropped_k180)


    cv2.waitKey(0)
    cv2.destroyAllWindows()
