
from flask import Flask, render_template, request
import csv
import pandas as pd
import rank_algo

fields = ['Project Name', 'Creativity', 'Appearance', "Complexity", "Efficiency","Execution","Composite Score"]
rank1 = ""
data = []
# Declare App

app = Flask(__name__)

# Start routes
@app.route('/')
def main():
    with open('database.csv', mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(fields)
    return render_template('app.html')
    

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/send', methods=['POST'])
def send(sum=sum):
    if request.method == "POST":
        project_name = request.form['Project Name']
        Creativity = float(request.form['Creativity'])
        Appearance = float(request.form['Appearance'])
        Complexity = float(request.form['Complexity'])
        Efficiency = float(request.form['Efficiency'])
        Execution = float(request.form['Execution'])


        composite = (0.05 * Creativity) + (0.3 * Complexity) + (0.3 * Efficiency) + (0.3 * Execution) + (0.05 * Appearance)


        data = [project_name, Creativity, Appearance, Complexity, Efficiency, Execution, composite]

        with open('database.csv', mode='a', newline='') as csv_file:
           csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
           csv_writer.writerow(data)
        sum = "successful"
        return render_template('app.html',sum=sum)

@app.route('/rank', methods=['POST'])
def rank(rank1=rank1):
    if request.method == "POST":
        first = rank_algo.rank_pd('database.csv')
        rank1 = list(first.keys())[0]
        return render_template('app.html', rank1=rank1)




        # if operation == 'add':
        #     sum = float(num1) + float(num2)
        #     return render_template('app.html', sum=sum)
        # elif operation == 'subtraction':
        #     sum = float(num1) - float(num2)
        #     return render_template('app.html', sum=sum)
        # elif operation == 'multiply':
        #     sum = float(num1) * float(num2)
        #     return render_template('app.html', sum=sum)
        # elif operation == 'divide':
        #     sum = float(num1) / float(num2)
        #     return render_template('app.html', sum=sum)
        # else:
        #     return render_template('app.html', sum=sum)
    