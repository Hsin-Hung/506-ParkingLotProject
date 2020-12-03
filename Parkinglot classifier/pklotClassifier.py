import csv
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import load_model

print(tf.__version__)


model = load_model('my_model.h5')#load the trained model

test_datagen = ImageDataGenerator(rescale=1. / 255)
eval_generator = test_datagen.flow_from_directory("predict",target_size=(224, 224),
                                                  batch_size=1,shuffle=False,seed=42,class_mode=None)

pred = model.predict(eval_generator,verbose=1)

with open('prediction.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    for index, probability in enumerate(pred):

        if (probability[0]>=0.5):

            writer.writerow([eval_generator.filenames[index], "P"])

        else:

            writer.writerow([eval_generator.filenames[index], "NP"])

        


