import tensorflow as tf
import numpy as np
from patchify import patchify


def classify(model,img):
    img = np.asarray(img)
    if len(img.shape) > 2 and img.shape[2] == 4:
        img = img[:, :, :3]
    #image_height, image_width, channel_count = img.shape

    if img.shape == (50,50,3):
        patches = img.copy()
        result=img.copy()
        output_patches = np.empty(patches.shape).astype(np.uint8)
        pic=patches/255
        x=tf.stack([pic],axis=0)
        Y_pred = model.predict(x)
        y_pred = (Y_pred > 0.5).astype(np.int64)
    
        if y_pred == 1:
            output_patches = np.full((50,50, 3), (0,0,255), dtype=np.uint8)  
        else:
            output_patches = patches.copy()

    else:

        old_image_height, old_image_width, channels = img.shape
        new_image_height = img.shape[0]+50-img.shape[0]%50
        new_image_width = img.shape[1]+50-img.shape[1]%50
        color = (255,255,255)
        result = np.full((new_image_height,new_image_width, channels), color, dtype=np.uint8)

# compute center offset
        x_center = (new_image_width - old_image_width) // 2
        y_center = (new_image_height - old_image_height) // 2

# copy img image into center of result image
        result[y_center:y_center+old_image_height,x_center:x_center+old_image_width] = img

        image_height, image_width, channel_count = result.shape
        patch_height, patch_width, step = 50, 50, 50
        patch_shape = (patch_height, patch_width, channel_count)

        patches = patchify(result, patch_shape, step=step)

        output_patches = np.empty(patches.shape).astype(np.uint8)
        for i in range(patches.shape[0]):
            for j in range(patches.shape[1]):
                patch = patches[i, j, 0]
                pic=patch/255
                x=tf.stack([pic],axis=0)
        
                Y_pred = model.predict(x)
                y_pred = (Y_pred > 0.5).astype(np.int64)

                if y_pred == 1:
                    patch = np.full((50,50, 3), (0,0,255), dtype=np.uint8)  
                    output_patches[i, j, 0] = patch
                else:
                    output_patches[i, j, 0] = patch
    return output_patches,result.shape