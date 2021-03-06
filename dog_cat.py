import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import os


def predict(fp: str):
    model = load_model(os.path.join(os.path.dirname(__file__), "model/dog_cat.h5"))

    temp_img = load_img(fp, target_size=(224, 224))
    temp_img_array = img_to_array(temp_img)
    img_array = temp_img_array[tf.newaxis]

    pred = model.predict(img_array)[0]

    classes = ["cat", "dog"]
    max_index = np.argmax(pred)
    ans = classes[max_index]
    print("Answer: " + ans)
    print("Confidence: " + str(pred[max_index]))
    print("=" * 30)
    results = pd.DataFrame(pred, index=classes, columns=["confidence"]).sort_values("confidence", ascending=False)
    print(results)
    return results
