from patchify import unpatchify


def output_image(prediction,imagesize):
    image_height, image_width, channel_count = imagesize
    patch_height, patch_width, step = 50, 50, 50


    if prediction.shape == (50,50,3):
        return prediction
        #output_image = Image.fromarray(output_patches)
    else:
        output_height = image_height - (image_height - patch_height) % step
        output_width = image_width - (image_width - patch_width) % step
        output_shape = (output_height, output_width, channel_count)
        output_image = unpatchify(prediction, output_shape)
        #output_image = Image.fromarray(output_image)

    return output_image

