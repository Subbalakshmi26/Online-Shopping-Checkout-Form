from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def checkout():
    if request.method == 'POST':
        full_name = request.form.get('full_name')
        address = request.form.get('address')
        city = request.form.get('city')
        state = request.form.get('state')
        postal_code = request.form.get('postal_code')
        phone = request.form.get('phone')
        email = request.form.get('email')
        payment_method = request.form.get('payment_method')


        return render_template('success.html', name=full_name)
    return render_template('checkout.html')

if __name__ == '__main__':
        app.run(debug=True)