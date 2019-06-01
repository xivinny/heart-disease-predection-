from flask import Flask, render_template, request
import os
app = Flask(__name__)

@app.route('/')
def student():
   return render_template('index.html')

@app.route('/result',methods = ['POST', 'GET'])

def result():
   #if request.method == 'POST':
  result = request.form
  f= open("pythondata.txt","w+")
  f.write(result['Age'])
  f.write(',')
  f.write(result['Gender'])
  f.write(',')
  f.write(result['Chest Pain Type'])
  f.write(',')
  f.write(result['Resting BP'])
  f.write(',')
  f.write(result['Cholestoral'])
  f.write(',')
  f.write(result['Fasting Blood Sugar'])
  f.write(',')
  f.write(result['Rest ECG'])
  f.write(',')
  f.write(result['Maximum Heart Rate Achieved'])
  f.write(',')
  f.write(result['Exercise induced angina'])
  f.write(',')
  f.write(result['Depression Induced by Exercise'])
  f.write(',')
  f.write(result['Slope of peak Exercise'])
  f.write(',')
  f.write(result['Number of vessals'])
  f.write(',')
  f.write(result['Type of defect'])
  f.write('\n')
  f.close()
  
  command = "python right.py"
  os.system(command)
  file = open("result_of_heart-disease.txt", "r") 
  name = file.read() 
  return render_template("result.html",result = result,name = name)

"""def prediction():
  if request.method == 'POST':
        import time
        start_time = time.time()
        file = request.files['file']
 
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
 
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            print(file_path)
            
            
            file = open("Result.txt", "r")
            label = file.read()
            print(label)
            filename = my_random_string(6) + filename
 
            os.rename(file_path, os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print("--- %s seconds ---" % str (time.time() - start_time))
            return render_template('template.html', label=label, imagesource='../uploads/' + filename)
    return jsonify({'error' : 'Missing data!'})
"""
  

if __name__ == '__main__':
   app.run(debug = True)