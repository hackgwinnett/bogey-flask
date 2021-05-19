
from flask import Flask, render_template, request, send_file
import csv
import pandas as pd
import rank_algo

fields = ['Project Name', 'Creativity', 'Appearance', "Complexity", "Efficiency","Execution","Composite Score"]
rank1 = ""
total = ""
data = []
creativity_weight = 0.05
complexity_weight = 0.3
efficiency_weight = 0.3
execution_weight = 0.3
appearance_weight = 0.3



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


@app.route("/")
def appfunc():
    return render_template('app.html')

@app.route("/customization")
def customization():
    return render_template('customization.html')

@app.route("/customize",  methods=['POST'])
def customize(total=total):
    global creativity_weight
    global appearance_weight
    global complexity_weight
    global efficiency_weight
    global execution_weight
    if request.method == "POST":
        check = float(request.form['Creativity Weight']) + float(request.form['Appearance Weight']) + float(request.form['Complexity Weight']) + float(request.form['Efficiency Weight']) + float(request.form['Execution Weight'])
        if check == 1:
            creativity_weight = float(request.form['Creativity Weight'])
            appearance_weight = float(request.form['Appearance Weight'])
            complexity_weight = float(request.form['Complexity Weight'])
            efficiency_weight = float(request.form['Efficiency Weight'])
            execution_weight = float(request.form['Execution Weight'])
            total = "Success"
            return render_template('customization.html', total=total)

        else:
            total = "ERROR: Weights Did Not Add to 1"
            return render_template('customization.html', total=total)




            
   
    
@app.route('/send', methods=['POST'])
def send(sum=sum):
    if request.method == "POST":
        project_name = request.form['Project Name']
        Creativity = float(request.form['Creativity'])
        Appearance = float(request.form['Appearance'])
        Complexity = float(request.form['Complexity'])
        Efficiency = float(request.form['Efficiency'])
        Execution = float(request.form['Execution'])


        composite = (creativity_weight * Creativity) + (complexity_weight * Complexity) + (efficiency_weight * Efficiency) + (execution_weight * Execution) + (appearance_weight * Appearance)


        data = [project_name, Creativity, Appearance, Complexity, Efficiency, Execution, composite]

        with open('database.csv', mode='a', newline='') as csv_file:
           csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
           csv_writer.writerow(data)
        sum = "Successful"
        return render_template('app.html',sum=sum)

@app.route('/rank', methods=['POST'])
def rank(rank1=rank1):
    if request.method == "POST":
        rank1 = rank_algo.rank_pd('database.csv')
        textfile = open("static/rankings.txt", "w")
        for element in rank1:
            textfile.write(str(element) + "\n")
        textfile.close()
        #rank1 = str(first[0])
        #return render_template('app.html', rank1=rank1)
        return send_file('static/rankings.txt',
                     mimetype='text/plain',
                     attachment_filename='rankings.txt',
                     as_attachment=True)
    
