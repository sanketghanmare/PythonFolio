import csv

from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)
print(__name__)


def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def htm_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['GET', 'POST'])
def submitform():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return "Did not save to database"
    else:
        return 'something went wrong. Try Again!'
