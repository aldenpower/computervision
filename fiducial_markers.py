import numpy as np
import cv2, PIL
from cv2 import aruco
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import os

from skimage import io 

# EXEPLO DE DICIONARIO
# DICT_[4 a 7]X[4 a 7]_[50, 100, 250, 1000]
# ex : aruco.DICT_6X6_250 (6 x 6 pixels com ids de 0 a 249)
# aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
# tag_id = 10
# n_pixels = 200
# #aruco.drawMarker(dicionario, ID do marcador, tamanho da imagem pixels x pixels)
# img = aruco.drawMarker(aruco_dict, tag_id, n_pixels)
# cv2.imshow('aruco', img)
# # Digite qualquer tecla para fechar a imagem
# cv2.waitKey(0)
# cv2.destroyAllWindows()


frame = io.imread('img/arucotest.png') # Carrega imagem a partir de uma URL
frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # Função responsável por converter do formato BGR para RGB
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # converte para a escala de cinza
aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250) # escolhe o dicionario
parameters =  aruco.DetectorParameters_create() 
corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters = parameters) #detecta os marcadores
frame_markers = aruco.drawDetectedMarkers(frame.copy(), corners, ids) # desenha os ids, marcadores e  orientação

cv2.imshow('result', frame_markers)
cv2.waitKey(0)
cv2.destroyAllWindows()