from keras.models import load_model


def model_bc():
    model=load_model("./models/final_imbalance_best_sgd2.hdf5")
    return model