from flask import Flask, render_template, request
from offline import range_set_finder, lgnv, rs_avg 
app: Flask = Flask(__name__)
all_results = []
runnin_avg = 0
qbc = 0
result = 0
student_overall = 0
course_overall = 0

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/questions', methods=['GET', 'POST'])
def questions():
    if request.method == 'POST':
        wet: str = request.form['wet']
        tta: str = request.form['tta']
        ssq: str = request.form['ssq']

        tc: str = request.form['tc']
        rmp: str = request.form['rmp']
        bot: str = request.form['bot']

        global student_overall
        global course_overall
        student_overall = int(wet) + int(tta) + int(ssq)
        course_overall = float(tc) - float(rmp) + float(bot)
        if course_overall < 0.0:
            course_overall = 0.0
    return render_template('questions.html')

@app.route('/qbridge')
def qbridge():
    rs = range_set_finder(student_overall, course_overall)
    global result
    result = lgnv(rs)
    global all_results
    all_results.append(result)
    global qbc
    qbc = 1
    return render_template('questions.html')

@app.route('/results')
def results():
    if qbc != 1:
        rs = range_set_finder(student_overall, course_overall)
        result = lgnv(rs)
        all_results.append(result)
    global running_avg 
    running_avg = rs_avg(all_results)
    return render_template('results.html', running_avg=running_avg)
    
@app.route('/bridge')
def bridge():
    if running_avg < 1.8:
        return render_template('final1.html')
    if running_avg < 2.5:
        return render_template('final2.html')
    if running_avg < 3.4:
        return render_template('final3.html')
    else:
        return render_template('final4.html')    


if __name__ == '__main__':
    app.run(debug=True)