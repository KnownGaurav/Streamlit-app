![Streamlit-UI](Streamlit-UI.jpg)


**🖼️ CIFAR-10 Image Classifier (Streamlit)**

A Streamlit-based web application that uses a trained CNN model on the CIFAR-10 dataset to classify uploaded images into one of 10 categories. Upload an image and visualize prediction probabilities in real time.

**🚀 Features**

📤 Upload images (.jpg, .png recommended)<br>
🧠 CNN model trained on CIFAR-10 dataset<br>
📊 Horizontal bar chart showing class probabilities<br>
⚡ Fast, interactive Streamlit UI<br>
🔍 Displays confidence for all 10 classes<br>

**🧠 CIFAR-10 Classes**

The model predicts one of the following classes:
airplane<br>
automobile<br>
bird<br>
cat<br>
deer<br>
dog<br>
frog<br>
horse<br>
ship<br>
truck<br>

**🛠️ Tech Stack**

Python 3.13.7<br>
Streamlit – Web interface<br>
TensorFlow / Keras – Model loading & inference<br>
NumPy – Image preprocessing<br>
Matplotlib – Probability visualization<br>
Pillow (PIL) – Image handling<br>

**⚙️ Installation & Setup**


1️⃣ Clone the Repository<br>
git clone https://github.com/your-username/cifar10-streamlit-classifier.git<br>
cd cifar10-streamlit-classifier<br>
2️⃣ Create a Virtual Environment (Recommended)<br>
python -m venv venv<br>
source venv/bin/activate      # Linux / macOS<br>
venv\Scripts\activate         # Windows<br>
3️⃣ Install Dependencies<br>
pip install -r requirements.txt<br>
▶️ Run the Application<br>
streamlit run app.py<br>

**🧪 How It Works**

User uploads an image using Streamlit<br>
Image is resized to 32×32 pixels<br>
Pixel values are normalized to [0, 1]<br>
Image reshaped to (1, 32, 32, 3)<br>
Pre-trained CIFAR-10 CNN predicts probabilities<br>
Results are displayed as a horizontal bar chart<br>

Author: Gaurav
KnownGaurav
