#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, send_file
import csv
import pandas as pd
import rank_algo

fields = [
    'Project Name',
    'Creativity',
    'Appearance',
    'Complexity',
    'Efficiency',
    'Execution',
    'Composite Score',
    ]
rank1 = ''
total = ''
data = []

cat1 = ''
cat2 = ''
cat3 = ''
cat4 = ''
cat5 = ''

cat1_cus = ''
cat2_cus = ''
cat3_cus = ''
cat4_cus = ''
cat5_cus = ''

creativity_list = {}
appearance_list = {}
complexity_list = {}
efficiency_list = {}
execution_list = {}

name1_global = 'Creativity'
name2_global = 'Appearance'
name3_global = 'Complexity'
name4_global = 'Efficiency'
name5_global = 'Execution'

name1 = ''
name2 = ''
name3 = ''
name4 = ''
name5 = ''

alt = ''
change = ''
creativity_weight = 0.05
complexity_weight = 0.3
efficiency_weight = 0.3
execution_weight = 0.3
appearance_weight = 0.3

# Declare App

app = Flask(__name__)


@app.route('/')
def main(
    cat1=cat1,
    cat2=cat2,
    cat3=cat3,
    cat4=cat4,
    cat5=cat5,
    ):
    with open('database.csv', mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"',
                                quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(fields)

    print name1_global
    cat1 = name1_global
    cat2 = name2_global
    cat3 = name3_global
    cat4 = name4_global
    cat5 = name5_global
    return render_template(
        'app.html',
        cat1=cat1,
        cat2=cat2,
        cat3=cat3,
        cat4=cat4,
        cat5=cat5,
        )

if __name__ == '__main__':
    app.run(debug=True)


@app.route('/')
def appfunc():
    return render_template('app.html')


@app.route('/customization')
def customization(
    cat1_cus=cat1_cus,
    cat2_cus=cat2_cus,
    cat3_cus=cat3_cus,
    cast4_cus=cat4_cus,
    cat5_cus=cat5_cus,
    ):
    cat1_cus = name1_global + ' Weight'
    cat2_cus = name2_global + ' Weight'
    cat3_cus = name3_global + ' Weight'
    cat4_cus = name4_global + ' Weight'
    cat5_cus = name5_global + ' Weight'

    return render_template(
        'customization.html',
        cat1_cus=cat1_cus,
        cat2_cus=cat2_cus,
        cat3_cus=cat3_cus,
        cat4_cus=cat4_cus,
        cat5_cus=cat5_cus,
        )


@app.route('/onecat')
def cat(
    cat1=cat1,
    cat2=cat2,
    cat3=cat3,
    cat4=cat4,
    cat5=cat5,
    ):
    cat1 = name1_global
    cat2 = name2_global
    cat3 = name3_global
    cat4 = name4_global
    cat5 = name5_global
    return render_template(
        'onecat.html',
        cat1=cat1,
        cat2=cat2,
        cat3=cat3,
        cat4=cat4,
        cat5=cat5,
        )


@app.route('/cat1method', methods=['POST'])
def cat1method():
    cur = 0
    cat1List = sorted(creativity_list.items(), key=lambda x: x[1],
                      reverse=True)
    textfile = open('static/cat1.txt', 'w')
    for element in cat1List:
        cur += 1
        textfile.write(str(cur) + '. ' + str(element) + '\n')
    textfile.close()
    return send_file('static/cat1.txt', mimetype='text/plain',
                     attachment_filename=name1_global + ' Sort' + '.txt'
                     , as_attachment=True)


@app.route('/cat2method', methods=['POST'])
def cat2method():
    cur = 0
    cat2List = sorted(appearance_list.items(), key=lambda x: x[1],
                      reverse=True)
    textfile = open('static/cat2.txt', 'w')
    for element in cat2List:
        cur += 1
        textfile.write(str(cur) + '. ' + str(element) + '\n')
    textfile.close()
    return send_file('static/cat2.txt', mimetype='text/plain',
                     attachment_filename=name2_global + ' Sort' + '.txt'
                     , as_attachment=True)


@app.route('/cat3method', methods=['POST'])
def cat3method():
    cur = 0
    cat3List = sorted(complexity_list.items(), key=lambda x: x[1],
                      reverse=True)
    textfile = open('static/cat3.txt', 'w')
    for element in cat3List:
        cur += 1
        textfile.write(str(cur) + '. ' + str(element) + '\n')
    textfile.close()
    return send_file('static/cat3.txt', mimetype='text/plain',
                     attachment_filename=name3_global + ' Sort' + '.txt'
                     , as_attachment=True)


@app.route('/cat4method', methods=['POST'])
def cat4method():
    cur = 0
    cat4List = sorted(efficiency_list.items(), key=lambda x: x[1],
                      reverse=True)
    textfile = open('static/cat4.txt', 'w')
    for element in cat4List:
        cur += 1
        textfile.write(str(cur) + '. ' + str(element) + '\n')
    textfile.close()
    return send_file('static/cat4.txt', mimetype='text/plain',
                     attachment_filename=name4_global + ' Sort' + '.txt'
                     , as_attachment=True)


@app.route('/cat5method', methods=['POST'])
def cat5method():
    cur = 0
    cat5List = sorted(execution_list.items(), key=lambda x: x[1],
                      reverse=True)
    textfile = open('static/cat5.txt', 'w')
    for element in cat5List:
        cur += 1
        textfile.write(str(cur) + '. ' + str(element) + '\n')
    textfile.close()
    return send_file('static/cat5.txt', mimetype='text/plain',
                     attachment_filename=name5_global + ' Sort' + '.txt'
                     , as_attachment=True)


@app.route('/customize2', methods=['POST'])
def customize2(
    name1=name1,
    name2=name2,
    name3=name3,
    name4=name4,
    name5=name5,
    ):
    global name1_global
    global name2_global
    global name3_global
    global name4_global
    global name5_global
    if request.method == 'POST':
        name1_global = request.form['Category 1']
        name2_global = request.form['Category 2']
        name3_global = request.form['Category 3']
        name4_global = request.form['Category 4']
        name5_global = request.form['Category 5']

        name1 = request.form['Category 1']
        name2 = request.form['Category 2']
        name3 = request.form['Category 3']
        name4 = request.form['Category 4']
        name5 = request.form['Category 5']
        print name5
    return render_template(
        'customization.html',
        name1=name1,
        name2=name2,
        name3=name3,
        name4=name4,
        name5=name5,
        )


@app.route('/customize', methods=['POST'])
def customize(total=total):
    global creativity_weight
    global appearance_weight
    global complexity_weight
    global efficiency_weight
    global execution_weight
    if request.method == 'POST':
        check = float(request.form['Creativity Weight']) \
            + float(request.form['Appearance Weight']) \
            + float(request.form['Complexity Weight']) \
            + float(request.form['Efficiency Weight']) \
            + float(request.form['Execution Weight'])
        if check == 1:
            creativity_weight = float(request.form['Creativity Weight'])
            appearance_weight = float(request.form['Appearance Weight'])
            complexity_weight = float(request.form['Complexity Weight'])
            efficiency_weight = float(request.form['Efficiency Weight'])
            execution_weight = float(request.form['Execution Weight'])
            total = 'Success'
            return render_template('customization.html', total=total)
        else:

            total = 'ERROR: Weights Did Not Add to 1'
            return render_template('customization.html', total=total)


@app.route('/send', methods=['POST'])
def send(sum=sum):
    global creativity_list
    global appearance_list
    global complexity_list
    global efficiency_list
    global execution_list
    if request.method == 'POST':

        project_name = request.form['Project Name']
        Creativity = float(request.form['Creativity'])
        Appearance = float(request.form['Appearance'])
        Complexity = float(request.form['Complexity'])
        Efficiency = float(request.form['Efficiency'])
        Execution = float(request.form['Execution'])

        creativity_list[project_name] = Creativity
        appearance_list[project_name] = Appearance
        complexity_list[project_name] = Complexity
        efficiency_list[project_name] = Efficiency
        execution_list[project_name] = Execution

        composite = creativity_weight * Creativity + complexity_weight \
            * Complexity + efficiency_weight * Efficiency \
            + execution_weight * Execution + appearance_weight \
            * Appearance

        data = [
            project_name,
            Creativity,
            Appearance,
            Complexity,
            Efficiency,
            Execution,
            composite,
            ]

        with open('database.csv', mode='a', newline='') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',',
                                    quotechar='"',
                                    quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow(data)
        sum = 'Successful'
        return render_template('app.html', sum=sum)


@app.route('/rank', methods=['POST'])
def rank(rank1=rank1):
    if request.method == 'POST':
        rank1 = rank_algo.rank_pd('database.csv')
        textfile = open('static/rankings.txt', 'w')
        for element in rank1:
            textfile.write(str(element) + '\n')
        textfile.close()
        return send_file('static/rankings.txt', mimetype='text/plain',
                         attachment_filename='rankings.txt',
                         as_attachment=True)

			
