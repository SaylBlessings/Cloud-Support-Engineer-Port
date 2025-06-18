from flask import Flask, render_template, request
import cmath

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = None

    if request.method == 'POST':
        try:
            a = float(request.form['a'])
            b = float(request.form['b'])
            c = float(request.form['c'])

            if a == 0:
                raise ValueError("Coefficient 'a' cannot be zero.")

            discriminant = cmath.sqrt(b**2 - 4*a*c)
            root1 = (-b + discriminant) / (2*a)
            root2 = (-b - discriminant) / (2*a)

            result = {
                'root1': root1,
                'root2': root2
            }

        except ValueError as ve:
            error = str(ve)
        except Exception:
            error = "Invalid input. Please enter numeric values."

    return render_template('index.html', result=result, error=error)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
