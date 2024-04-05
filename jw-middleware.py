from flask import Flask, request, jsonify,render_template

from dataclasses import dataclass

from flask_sqlalchemy import SQLAlchemy

 

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:torontomet123@localhost/jwfoods'

db = SQLAlchemy(app)

 

@dataclass

class Coefficient(db.Model):

     __tablename__ = 'coefficient'

   

     id : int

     name: str
     
     value: float

   

     id = db.Column( db.Integer(), primary_key=True )

     name = db.Column( db.String(100) )
     
     value =db.Column(db.Float())
     
@app.route('/list')

def list_all() :

     all_Coefficient = Coefficient.query.all()
     return all_Coefficient
     
@app.route('/start' ,methods=['GET'])

def loadStartPage():

	return render_template('jwfoods.html')
	

 
     
@app.route('/distancecalculator', methods=['POST'])

def DistanceCalculator():

   

     distanceValue = request.form.get('distance')

     weightValue = request.form.get('weight')
      
     query = db.session.query(Coefficient)

     distanceQuery = query.filter(Coefficient.name=='distance')
     distanceCoefficient=distanceQuery.first()
      
     weightQuery = query.filter(Coefficient.name=='weight')
     weightCoefficient=weightQuery.first()
     
     print(distanceCoefficient, weightCoefficient)
     
      
     CostCalculation=int(distanceValue)*distanceCoefficient.value + int(weightValue)*weightCoefficient.value
     
     return (str(CostCalculation) )
 
      
      
# should always be at the end of your file

if __name__ == '__main__' :

  app.run(debug=True)
