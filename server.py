from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/works')
def works():
    return render_template('works.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')


# def write_to_file(data):
#     with open('database.txt', mode='a') as database_txt:
#         email = data['email']
#         subject = data['subject']
#         message = data['message']
#         file = database_txt.write(
#             f'\n email: {email}, subject: {subject}, message: {message}')


def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database_csv:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(
            database_csv,
            delimiter=',',
            quotechar='|',
            quoting=csv.QUOTE_MINIMAL
        )
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou')
        except:
            return 'a problem occurred'
    else:
        "something went wrong"
