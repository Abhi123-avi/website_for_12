from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory dictionary to store applications (email used as key)
applications = {}

# Your LPU data (you already had this)
lpu = [
    {'id': 1, 'title': 'Btech admission',
     'requirements': '10+2 with Physics, Chemistry, and Mathematics',
     'description': 'LPU offers Btech programs ...',
     'fees': 'INR 1,50,000 per year'},
    {'id': 2, 'title': 'Mtech admission',
     'requirements': 'Btech degree ...',
     'description': 'LPU offers Mtech programs ...',
     'fees': 'INR 1,80,000 per year'},
    {'id': 3, 'title': 'MBA admission',
     'requirements': 'Graduation degree ...',
     'description': 'LPU offers MBA programs ...',
     'fees': 'INR 2,00,000 per year'},
    {'id': 4, 'title': 'BBA admission',
     'requirements': '10+2 with minimum 50% marks',
     'description': 'LPU offers BBA programs ...',
     'fees': 'INR 1,20,000 per year'}
]

@app.route('/')
def home():
    # Pass applications dict so index.html can list received applications
    return render_template('index.html', lpu=lpu, applications=applications)

@app.route('/next')
def next_page():
    return render_template('next.html', lpu=lpu)

@app.route('/apply', methods=['GET', 'POST'])
def apply():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip().lower()
        phone = request.form.get('phone', '').strip()

        # Basic validation
        if not name or not email or not phone:
            # in production you'd return an error; here we simply reload form
            return render_template('apply.html', error="All fields are required.")

        # Save application (email used as unique key)
        applications[email] = {
            "name": name,
            "email": email,
            "phone": phone
        }

        print("Current applications:", applications)  # shows in terminal for debug
        return redirect(url_for('home'))

    return render_template('apply.html')

if __name__ == '__main__':
    app.run(debug=True)
