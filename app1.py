from flask import *
import os
from werkzeug.utils import secure_filename
import label_image
import PreProcessing

def load_image(image):
    text = label_image.main(image)
    return text

app = Flask(__name__)

pp = PreProcessing
@app.route('/')
@app.route('/first')
def first():
    return render_template('first.html')

 
  
    
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/chart')
def chart():
    return render_template('chart.html')


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/index1')
def index1():
    #return "Index Page"
    return render_template('index1.html')

@app.route('/',methods = ['POST'])
def result():
    grains = request.form['grains']
    vegetables = request.form['vegetables']
    fruits = request.form['fruits']
    protein = request.form['protein']
    grains = float(grains)
    vegetables = float(vegetables)
    fruits = float(fruits)
    protein = float(protein)
    predictedResult = pp.healthy_diet(grains,vegetables,fruits,protein)
    print('Experience is ',predictedResult)
    predictedResult1 = pp.protein_diet(grains,vegetables,fruits,protein)
    print('Experience is ',predictedResult1)
    predictedResult2 = pp.grains_diet(grains,vegetables,fruits,protein)
    print('Experience is ',predictedResult2)    
    predictedResult3 = pp.vegetables_diet(grains,vegetables,fruits,protein)
    print('Experience is ',predictedResult3)    
    return render_template('result.html', PredictedResult = predictedResult,PredictedResult1 = predictedResult1,PredictedResult2 = predictedResult2,PredictedResult3 = predictedResult3,)

@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']
        file_path = secure_filename(f.filename)
        f.save(file_path)
        # Make prediction
        result = load_image(file_path)
        result = result.title()
        d = {"Chicken Curry":" → Nutrition Data- Protein 12g, Carbs 3.2g, Fat 5.2g, Fiber 1.1g Calories 108cal",
	'Fried Rice':" → Nutrition Data- Protein 2g, Carbs 20g, Fat 3.4g, Fiber 0.8g Calories 110cal",
        "Dosai":" → Nutrition Data- Protein 2g, Carbs 20g, Fat 3.4g, Fiber 0.8g Calories 110cal",
        "Chicken Briyani":" → Nutrition Data- Protein 2g, Carbs 20g, Fat 3.4g, Fiber 0.8g Calories 110cal",
        "Rice":" → Nutrition Data- Protein 2g, Carbs 20g, Fat 3.4g, Fiber 0.8g Calories 110cal",
        "Vada":" → Nutrition Data- Protein 2g, Carbs 20g, Fat 3.4g, Fiber 0.8g Calories 110cal",
        "Poori":" → Nutrition Data- Protein 2g, Carbs 20g, Fat 3.4g, Fiber 0.8g Calories 110cal",
        "Idly":" → Nutrition Data- Protein 8.1g, Carbs 46.2g, Fat 13.4g, Fiber 7.8g Calories 335cal"}
        result = result+d[result]
        #result2 = result+d[result]
        #result = [result]
        #result3 = d[result]        
        print(result)
        #print(result3)
        os.remove(file_path)
        return result
        #return result3
    return None

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')
