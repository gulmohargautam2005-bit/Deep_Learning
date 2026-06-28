import numpy as np 
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os


class PredictionPipeline:
    def __init__(self,filename):
        self.filename=filename
    
    def predict(self):
        model=load_model(os.path.join("model","training_model.h5"))

        class_indices = {0: 'Cyst', 1: 'Normal', 2: 'Stone', 3: 'Tumor'}
        imagename=self.filename
        test_image =image.load_img(imagename,target_size=(224,224))
        test_image=image.img_to_array(test_image)
        test_image = test_image / 255.0 
        test_image=np.expand_dims(test_image,axis=0)
        result=np.argmax(model.predict(test_image),axis=1)
        predicted_class = class_indices[result[0]]
        return [{"image": predicted_class}]

 