COMP4423 – Computer Vision

Group Project: Fashion Image Generation

Group 1

JIANG Yiyang (21095707d)  
YE Haowen (21098829d)  
ZHANG Wengyu (21098431d)  

April 2023

---

# User Manual


## Preparation

1. Python version: `3.10.10`
2. Make sure following package are install for python3:
   - `OpenCV`, `Flask`, `numpy`, `pandas`, `sklearn`, `torch`, `torchvision`, `torchaudio`, `matplotlib`, `seaborn`, `PIL`

---

## File Checklist

The `Project_Group_1.zip` contains following files and folders:
- [x] `A_User_Manual.pdf`, this file, please read it first before using the programme;
- [x] `Project_Group_1.pdf`, project report;
- [x] `Project_Group_1.py`, entrance program for the project;
- [x] `Fashion_Image_Generator_Algo.py`, the backend algorithm for the project.
- [x] `templates`, `static`, two folder for the frontend UI of the project; 
- [x] `fashion-mnist`, folder containing the fashion-mnist dataset;
- [x] `ACGAN.ipynb`, the Jupyter Notebook for ACGAN model training and validation, which is our final model;
- [x] `ACGAN6_G_30_1.pth`, the saved trained ACGAN model;
- [x] `ACGAN_images`, folder containing the generated images by ACGAN model;
- [x] `originalGAN`, `cGAN`, `cDCGAN`, `cPCGAN`, folders containing models we have tried, including the saved trained models and generated images;

---

### How to run and use the Fashion Clothing Image Generator?

- Make sure you have installed all the required packages mentioned in the **Preparation** section above; 
- Run the `Project_Group_1.py` file by
  `python3 Project_Group_1.py`
- Check your terminal says `Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)`;
- Use your browser to visit the web page on your localhost: [http://127.0.0.1:5000/](http://127.0.0.1:5000/);
- follow the instruction on the web page (step1, step2);
- Press `CTRL+C` in terminal to quit.

---

### How view dataset, train and validate models?

> **Note**: 
> We have tried 5 different models, **original provided GAN**, **Conditional GAN**, **Conditional Deep Convolutional GAN (cDCGAN)**, **Conditional 'Partial' Convolutional GAN (c'P'CGAN)**, **Auxiliary Classifier GAN (ACGAN)**. 
> The **ACGAN** model is our final model, which is used in the project.


1. Open the `ACGAN.ipynb` Jupyter Notebook on local machine;
2. In the **first code cell**, please **set proper `device`** according to your machine.
3. Run all cells in the `ACGAN.ipynb` file;
4. You may also try other models which are in the `originalGAN`, `cGAN`, `cDCGAN`, `cPCGAN` folders.

