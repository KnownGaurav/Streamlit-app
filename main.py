import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import tensorflow as tf

def main():
    st.title('Cifar-10 Image Classifier')
    st.write('Upload any image that you think fits into the classes and see if the prediction is correct or not')

    file = st.file_uploader('Please upload an image', type=['jpg', 'img'])
    if file:
        Image = Image.open(file)
        st.image(Image, use_column_width=True)

        resized_image = Image.resize((32,32))
        img_array = np.array(resized_image)/255
        img_array = img_array.reshape((1, 32, 32, 3)) #1 image with (32,32,3) size

        model = tf.keras.models.load_model('cifar10_model.h5')

        predictions = model.predict(img_array)
        cifar10_classes = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

        fig, ax=  plt.subplots()
        y_pos = np.arange(len(cifar10_classes))
        ax.barh(y_pos, predictions[0], align='center')
        ax.set_yticks(y_pos)
        ax.set_yticklabels(cifar10_classes)
        ax.invert_yaxis
        ax.set_xlabel("Probability")
        ax.set_title('CIFAR10 Predictions')

        st.pyplot(fig)


    else:
        st.text('You have not uploaded an image yet.')


if __name__ == '__main__':
    main()