#############################################################################
# COMP4423 – Computer Vision                                                #
# Group Project: Fashion Image Generation                                   #
#                                                                           #
# Group 1                                                                   #
#                                                                           #
# JIANG Yiyang (21095707d)                                                  # 
# YE Haowen (21098829d)                                                     #
# ZHANG Wengyu (21098431d)                                                  #
#                                                                           #
# This is the entrance program for the Project                              #
#                                                                           #
# The app will run on localhost (http://127.0.0.1:5000),                    #
#   please use the browser to access the web page                           #
#                                                                           #
#   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!   #
#   !! Please carefully read User_Manual.pdf file first before running !!   #
#   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!   #
#                                                                           #
#############################################################################

from flask import Flask, render_template, Response, request
from Fashion_Image_Generator_Algo import generateFromLabel, Discriminator, Generator
from PIL import Image
import time
import numpy as np
import os

labelMap = ['T-Shirt', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
UPLOAD_FOLDER = os.path.join('static')

# Using Flask to build a web application
app = Flask(__name__)

def clear():
    # Clearing the folder, no uploaded file will be stored in the server once the prediction is done
    dir = 'static'
    for f in os.listdir(UPLOAD_FOLDER):
        os.remove(os.path.join(dir, f))

@app.route('/')
def index(): 
    return render_template('index.html', gen_text = 'Please first Select a Label and then click "Generate"')

@app.route('/', methods=("POST", "GET"))
def process_form():
    
    clear()
    text_input = eval(request.form['text_input'])
    if text_input in range(0,10):
        print(text_input)
        img = generateFromLabel(text_input, 10)
        # temporary storage for display
        ts = str(int(time.time()))
        img_filename = ts +'.jpeg'
        fname = 'static/'+img_filename
        img = Image.fromarray((img * 255).astype(np.uint8)) 
        img.save(fname)
        result = render_template('index.html', gen_image = fname, gen_text = '10 generated fashion clothing images on '+labelMap[text_input])
        return result
    else:
        result = render_template('index.html')
        return result

if __name__ == '__main__':
    # run the app on localhost (http://127.0.0.1:5000), use the browser to access the web page
    app.run(debug=True)