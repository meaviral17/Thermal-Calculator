from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/",methods=['POST','GET'])
def home():
	if request.method == 'POST':
		
		T1 = float(request.form['T1'])
		T2 = float(request.form['T2'])
		T3 = float(request.form['T3'])
		T4 = float(request.form['T4'])
		K = float(request.form['K'])
		P = float(request.form['P'])
		C = float(request.form['C'])
		K_un = K * ((T1-T2)/(T3-T4))
		A = (K_un*(P*C))

		return render_template("home.html",T1=T1,T2=T2,T3=T3,T4=T4,K=K,P=P,C=C,K_un=K_un,A=A)
	else:
		return render_template("home.html")

if __name__ == "__main__":
	app.run(debug=True)
