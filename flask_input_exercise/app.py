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
        principal = float(request.form.get('principal'))
        interest = float(request.form.get('interest'))/100
        time = float(request.form.get('time'))
        total = float(principal * ((1 + interest/100) ** time))
        return '''
                
                  <h1>The amount of money accumulated in {} year(s) is: R$ {:.2f}</h1>
                  '''.format(time, total)

    # otherwise handle the GET request
    return '''
           <form method="POST">
               <div><label>Principal:       <input type="float" name="principal">         </label></div>
               <div><label>Annual Interest: <input type="float" name="interest">          </label></div>
               <div><label>Time:            <input type="float" name="time">              </label></div>
               <input type="submit" value="Calculate">
           </form>'''


@app.route('/json-calculator', methods = ["POST", "GET"])
def json_example():
    request_data = request.get_json()

    principal = None
    interest = None
    time = None
    total = None

    if request_data:
        if 'principal' in request_data:
            principal = float(request_data['principal'])

        if 'interest' in request_data:
            interest = float(request_data['interest'])

        if 'time' in request_data:
            time = float(request_data['time'])

        total = float(principal * ((1 + interest/100) ** time))


    return '''
           The principal value is: {}
           The interest value is: {}
           The Amount of time is: {}
           Based on these data, you are going to have R$ {} 
           '''.format(principal, interest, time, total)

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)