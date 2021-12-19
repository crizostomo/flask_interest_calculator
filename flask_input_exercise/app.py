from flask import Flask, request
import math

#Documentar de uma forma simplificado o que faz e como faz no readme
#mudar as regras e explicar passo a passo como faz

# create the Flask app
app = Flask(__name__)

@app.route('/calculator', methods=['GET', 'POST'])
def interest_calculator():
    # handle the POST request = receber
    if request.method == 'POST':
        principal = int(request.form.get('principal'))
        interest = int(request.form.get('interest'))/100
        time = int(request.form.get('time'))
        total = int(principal * ((1 + interest) ** time))
        return '''
                
                  <h1>The amount of money accumulated in {} year(s) is: R$ {:.2f}</h1>
                  '''.format(time, total)

    # otherwise handle the GET request
    return '''
           <form method="POST">
               <div><label>Principal:       <input type="int" name="principal">         </label></div>
               <div><label>Annual Interest: <input type="int" name="interest">          </label></div>
               <div><label>Time:            <input type="int" name="time">              </label></div>
               <input type="submit" value="Calculate">
           </form>'''


if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)