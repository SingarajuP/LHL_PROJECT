import streamlit as st
import pickle
import numpy as np
#import cv2
from PIL import Image
from src.predict import classify
from src.process import output_image
from src.utils import model_bc
import sys
sys.path.append("src/")

upload= st.file_uploader('Insert image for classification', type=['png','jpg']) 
c1, c2= st.columns(2)
if upload is not None:
  im= Image.open(upload)
  img= np.asarray(im)
  #image= cv2.resize(img,(50, 50))
  #img= preprocess_input(image)
#  img= np.expand_dims(img, 0)
  c1.header('Input Image')
  c1.image(im)
  c1.write(img.shape)  
  model=model_bc()
  prediction,imagesize=classify(model,img) 

  prediction_image=output_image(prediction,imagesize)
  c2.header('Output')
  #c2.subheader('Predicted class :')
  #c2.write("prediction image: ")
  c2.image(prediction_image)
