import tensorflow as tf
import numpy as np

def classify(model,img):
    x=tf.stack([img],axis=0)
    Y_pred = model.predict(x)
    y_pred = (Y_pred > 0.5).astype(np.int64)
    print(y_pred)
    if y_pred == 1:
        pred = "Cancer"
    else:
        pred ="Not Cancer"
    return pred