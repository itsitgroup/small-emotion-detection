from keras.models import load_model
from sklearn.preprocessing import LabelEncoder
from preprocess import preprocessing
from model import model

def evaluate():
    twodim = preprocessing()
    livepreds = model.predict(twodim, batch_size=32, verbose=1)
    livepreds1 = livepreds.argmax(axis=1)
    return livepreds1
