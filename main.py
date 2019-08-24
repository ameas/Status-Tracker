from utils import dataframe
from flask import Flask , render_template , request, session
app = Flask(__name__)

@app.route('/index')
def func1():
    if 'username' in session:
        return render_template("index.html",  x2=dataframe.x2, y2=dataframe.y2, c=dataframe.c,   z=dataframe.z,  t1=dataframe.start_date, t2=dataframe.end_date,   u=dataframe.u,
                           r2=dataframe.r2,s2=dataframe.s2, s22=dataframe.s22,z1=dataframe.z1,  t11=dataframe.start_date1, t22=dataframe.end_date1,
         x3=dataframe.x3, y3=dataframe.y3, r3=dataframe.r3,s3=dataframe.s3, a=dataframe.x4, b=dataframe.y4, y=dataframe.y, r4=dataframe.r4,s4=dataframe.s4, ya=dataframe.ya, 
         x1=dataframe.x1, y1=dataframe.y1, r1=dataframe.r1, s1=dataframe.s1,x5=dataframe.x5, y5=dataframe.y5, q=dataframe.q, r5=dataframe.r5,s5=dataframe.s5, q1=dataframe.q1)
    return render_template("sub.html")
@app.route('/table')
def func2():
    if 'username' in session:
        return render_template("table.html",  u=dataframe.u,data=dataframe.df.to_html(classes=["table-bordered", "table-striped", "table-hover"], table_id='myTable1'), data1=dataframe.dfo.to_html(classes=["table-bordered", "table-striped", "table-hover"], table_id='myTable2') )
    return render_template("sub.html")

@app.route('/doc')
def func3():
    if 'username' in session:
        return render_template("doc.html") 
    return render_template("sub.html")
@app.route('/assi')
def func4():
    if 'username' in session:
        return render_template("assi.html",   u=dataframe.u, x2=dataframe.x2, y2=dataframe.y2, c=dataframe.c,   zassi=dataframe.zassi, zup = dataframe.zup,  t11=dataframe.start_date1, t22=dataframe.end_date1,
                           r2=dataframe.r2,s2=dataframe.s2, s22=dataframe.s22,z1=dataframe.z1, zup1 = dataframe.zup1, t1=dataframe.start_date, t2=dataframe.end_date, suma= dataframe.suma , suma1=dataframe.suma1)
    return render_template("sub.html")

@app.route('/sta')
def func5():
    if 'username' in session:
        return render_template("sta.html",     u=dataframe.u, x3=dataframe.x3, y3=dataframe.y3, r3=dataframe.r3,s3=dataframe.s3,  t1=dataframe.start_date, t2=dataframe.end_date,  t11=dataframe.start_date1, t22=dataframe.end_date1)
    return render_template("sub.html")

@app.route('/rel')
def func6():
    if 'username' in session:
        return render_template("rel.html", u=dataframe.u,     a=dataframe.x4, b=dataframe.y4, ye=dataframe.ye,  t1=dataframe.start_date, t2=dataframe.end_date,  t11=dataframe.start_date1, t22=dataframe.end_date1,r4=dataframe.r4,s4=dataframe.s4, ya=dataframe.ya)
    return render_template("sub.html")

@app.route('/story')
def func7():
    if 'username' in session:
        return render_template("story.html",  u=dataframe.u,    x1=dataframe.x1, y1=dataframe.y1,   r1=dataframe.r1, s1=dataframe.s1, t1=dataframe.start_date, t2=dataframe.end_date, 
                           t11=dataframe.start_date1, t22=dataframe.end_date1, x6=dataframe.x6, y6=dataframe.y6, r6=dataframe.r6, s6=dataframe.s6)
    return render_template("sub.html")

@app.route('/epic')
def func8():
    if 'username' in session:
        return render_template("epic.html",  u=dataframe.u,    x5=dataframe.x5, y5=dataframe.y5, q=dataframe.q,   r5=dataframe.r5,s5=dataframe.s5, q1=dataframe.q1,t1=dataframe.start_date, t2=dataframe.end_date,  t11=dataframe.start_date1, t22=dataframe.end_date1)
    return render_template("sub.html")

@app.route('/')
def func9():
    session.pop('username', None)
    return render_template('login.html')

@app.route('/', methods=['POST'])
def func10():
    session['username'] = request.form['uid']
    return render_template('welcome.html')

@app.route('/pro')
def func11():
    if 'username' in session:
        return render_template('pro.html')
    return render_template("sub.html")

@app.route('/pro', methods=['POST'])
def func12():
    dataframe.list_issues() 
    return render_template("index.html",  x2=dataframe.x2, y2=dataframe.y2, c=dataframe.c,   z=dataframe.z,  t1=dataframe.start_date, t2=dataframe.end_date,   u=dataframe.u,
                           r2=dataframe.r2,s2=dataframe.s2, s22=dataframe.s22,z1=dataframe.z1,  t11=dataframe.start_date1, t22=dataframe.end_date1,
         x3=dataframe.x3, y3=dataframe.y3, r3=dataframe.r3,s3=dataframe.s3, a=dataframe.x4, b=dataframe.y4, y=dataframe.y, r4=dataframe.r4,s4=dataframe.s4, ya=dataframe.ya, 
         x1=dataframe.x1, y1=dataframe.y1, r1=dataframe.r1, s1=dataframe.s1,x5=dataframe.x5, y5=dataframe.y5, q=dataframe.q, r5=dataframe.r5,s5=dataframe.s5, q1=dataframe.q1)

if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.run()