form flask import*
app=Flask(__name__)

@app.route('/login',methods=['POST'])
def login():
    unname=request.form['unname']
    passwrd=request.form['pass']
    if unname=="ayush" and passwrd=="google":
        return "Welcome %s"%unname
        
if__name__=='__main__':
    app.run(debug=True)
    
