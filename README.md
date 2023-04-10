# Predicting Breast Cancer from tissue samples
<br />[Breast cancer prediction from histopathology images](https://singarajup-histopathology-breastcancer-prediction-app-3ey2vh.streamlit.app/)
This is a final Data Science project at Lighthouse labs

Overview:
The most common type of cancer is Breast cancer impacting 2.1 million women worldwide every year. About 80% of all breast cancers are invasive ductal carcinomas. Invasive means that the cancer has spread to the surrounding breast tissues. Over time, invasive ductal carcinoma can spread to the lymph nodes and possibly to other areas of the body.
Doctors prescribe biopsy after physical examination and the sample will be observed by pathologists under microscope. Depending on the size, color, texture and other things, the type of the cancer and the grade of the cancer is known. And the treatment will be based on this information.
The automatic detection of tumor cells will help pathologists save time by evaluating the results faster. 

Aim:
To build a classifier that identifies the breast cancer from the images of tissue samples


Data source:

https://www.kaggle.com/paultimothymooney/breast-histopathology-images

## Usage
Clone repo 
```bash
 git clone https://github.com/SingarajuP/histopathology_breastcancer-prediction.git
```
<br />Setup a virtual environment
```bash
conda create -n yourenvname python=3.8.16
```
<br />Activate the virtual environment

```bash
conda activate yourenvname
```
<br />Install all requirements using pip:
```bash
pip install -r requirements.txt
```
<br />To run web application stay in the main directory and run the command:
```bash
streamlit run app.py
# It will open a web page in the browser 

```

<br />To test the images, open testimages folder and load them in the streamlit app:
<br />The image will be split into 50x50x3 patches and cancer will be predicted for individual patches. If the cancer is predicted the output image will show the area where cancer is present in blue colour. 
<br /> Bigger images will take more time. For example, in testimages folder test_image_patient.png is a whole slide image and will take ~5-10min for the prediction.
