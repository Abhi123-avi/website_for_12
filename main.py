from flask import Flask, render_template, url_for

app = Flask(__name__)

lpu = [
    {
        'id': 1,
        'title': 'Btech admission',
        'requirements': '10+2 with Physics, Chemistry, and Mathematics',
        'description': 'LPU offers Btech programs in various specializations including Computer Science, Mechanical, Civil, and Electrical Engineering.',
        'fees': 'INR 1,50,000 per year'
    },
    {
        'id': 2,
        'title': 'Mtech admission',
        'requirements': 'Btech degree in relevant field with minimum 60% marks',
        'description': 'LPU offers Mtech programs in various specializations including Computer Science, Mechanical, Civil, and Electrical Engineering.',
        'fees': 'INR 1,80,000 per year'
    },
    {
        'id': 3,
        'title': 'MBA admission',
        'requirements': 'Graduation degree with minimum 50% marks and valid entrance exam score (CAT/MAT/XAT)',
        'description': 'LPU offers MBA programs with specializations in Marketing, Finance, Human Resource Management, and International Business.',
        'fees': 'INR 2,00,000 per year'
    },

    {
        'id': 4,
        'title': 'BBA admission',
        'requirements': '10+2 with minimum 50% marks',
        'description': 'LPU offers BBA programs with specializations in Marketing, Finance, Human Resource Management, and International Business.',
        'fees': 'INR 1,20,000 per year'
    }

]

@app.route('/')
def home():
    return render_template('index.html', lpu=lpu)

@app.route('/next')
def next_page():
    return render_template('next.html', lpu=lpu)

if __name__ == '__main__':
    app.run(debug=True)