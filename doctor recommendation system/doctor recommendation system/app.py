# # from flask import Flask, render_template, request
# # import pickle
# # import string
# # import re
# # import nltk
# # from nltk.corpus import stopwords
# # from nltk.tokenize import word_tokenize
# #
# # app = Flask(__name__)
# #
# # # Download NLTK resources (uncomment the next two lines if not downloaded)
# # # nltk.download('punkt')
# # # nltk.download('stopwords')
# #
# # stop_words = set(stopwords.words('english'))
# #
# # # Function to clean and tokenize text
# # def clean_and_tokenize(text):
# #     text = text.translate(str.maketrans('', '', string.punctuation))  # Remove Punctuation
# #     text = re.sub(r'\d+', '', text)  # Remove Digits
# #     text = text.replace('\n', ' ')  # Remove New Lines
# #     text = text.strip()  # Remove Leading White Space
# #     text = re.sub(' +', ' ', text)  # Remove multiple white spaces
# #
# #     # Tokenize text using NLTK
# #     tokens = [word for word in word_tokenize(text) if word.lower() not in stop_words]
# #     return ' '.join(tokens)
# #
# # # Load the trained model from the saved file
# # with open('best_model.pkl2', 'rb') as model_file:
# #     loaded_model = pickle.load(model_file)
# #
# # @app.route('/')
# # def index():
# #     return render_template('index.html')
# #
# # @app.route('/recommend', methods=['POST'])
# # def recommend():
# #     if request.method == 'POST':
# #         user_input = request.form['symptoms']
# #         cleaned_user_input = clean_and_tokenize(user_input)
# #         predicted_disease = loaded_model.predict([cleaned_user_input])[0]
# #         return render_template('result.html', predicted_disease=predicted_disease)
# #
# # if __name__ == '__main__':
# #     app.run(debug=True)
#


# successful code
#
# import base64
# import pandas as pd
# from flask import Flask, render_template, request
# import csv
# import pickle
# import string
# import re
# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize
#
# app = Flask(__name__)
#
# # Download NLTK resources (uncomment the next two lines if not downloaded)
# # nltk.download('punkt')
# # nltk.download('stopwords')
#
# stop_words = set(stopwords.words('english'))
#
# # Load the trained model from the saved file
# with open('best_model.pkl2', 'rb') as model_file:
#     loaded_model = pickle.load(model_file)
#
# doctors = []
#
#
# # Load doctors from CSV file
# def load_doctors():
#     with open('doctors.csv', 'r') as csvfile:
#         reader = csv.DictReader(csvfile)
#         for row in reader:
#             doctors.append(row)
#
#
# # Populate doctors list at the start
# load_doctors()
#
#
# # Function to clean and tokenize text
# def clean_and_tokenize(text):
#     text = text.translate(str.maketrans('', '', string.punctuation))  # Remove Punctuation
#     text = re.sub(r'\d+', '', text)  # Remove Digits
#     text = text.replace('\n', ' ')  # Remove New Lines
#     text = text.strip()  # Remove Leading White Space
#     text = re.sub(' +', ' ', text)  # Remove multiple white spaces
#
#     # Tokenize text using NLTK
#     tokens = [word for word in word_tokenize(text) if word.lower() not in stop_words]
#     return ' '.join(tokens)
#
#
# @app.route('/')
# def index():
#     return render_template('index.html')
#
#
# @app.route('/recommend', methods=['POST'])
# def recommend():
#     if request.method == 'POST':
#         user_input = request.form['symptoms']
#         cleaned_user_input = clean_and_tokenize(user_input)
#         predicted_disease = loaded_model.predict([cleaned_user_input])[0]
#
#         # Match the recommended disease with doctors' specialization (case-insensitive)
#         matched_doctors = [doctor for doctor in doctors if
#                            predicted_disease.lower() in doctor['specialization'].lower()]
#
#         return render_template('result.html', predicted_disease=predicted_disease, matched_doctors=matched_doctors)
#
#
#
# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         # Handle doctor registration form data
#         full_name = request.form.get('full_name')
#         degree = request.form.get('degree')
#         specialization = request.form.get('specialization')
#         disease_specialist = request.form.get('disease_specialist')
#         email = request.form.get('email')
#         contact = request.form.get('contact')
#         address = request.form.get('address')
#         country = request.form.get('country')
#         gender = request.form.get('gender')
#
#         # Handle image upload
#         file = request.files['file-input']
#         if file:
#             # Convert image to base64
#             image_data = base64.b64encode(file.read()).decode('utf-8')
#
#             # Save the doctor details to an Excel file
#             data = {
#                 'Full Name': [full_name],
#                 'Degree': [degree],
#                 'Specialization': [specialization],
#                 'Disease Specialist': [disease_specialist],
#                 'Email': [email],
#                 'Contact': [contact],
#                 'Address': [address],
#                 'Country': [country],
#                 'Gender': [gender],
#                 'Image Data': [image_data]
#             }
#
#             df = pd.DataFrame(data)
#
#             # Check if the file exists
#             try:
#                 existing_df = pd.read_excel('doctors.xlsx')
#                 df = pd.concat([existing_df, df], ignore_index=True)
#             except FileNotFoundError:
#                 pass
#
#             df.to_excel('doctors.xlsx', index=False)
#
#             # Add the doctor to the list
#             doctors.append({
#                 'full_name': full_name,
#                 'degree': degree,
#                 'specialization': specialization,
#                 'disease_specialist': disease_specialist,
#                 'email': email,
#                 'contact': contact,
#                 'address': address,
#                 'country': country,
#                 'gender': gender,
#                 'image_data': image_data
#             })
#
#         return render_template('index.html', message='Registration successful!')
#     return render_template('register.html')
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
#
#


# Test data 3


# import os
# import sqlite3

#
# import base64
# import pandas as pd
# from flask import Flask, render_template, request
# import csv
# import pickle
# import string
# import re
# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize
#
# app = Flask(__name__)
#
# # Admin credentials
# ADMIN_USERNAME = 'admin'
# ADMIN_PASSWORD = 'admin_password'
# # Admin authentication function
# def authenticate_admin(username, password):
#     return username == ADMIN_USERNAME and password == ADMIN_PASSWORD
#
#
# # Display all registered doctors in the admin panel
# @app.route('/admin', methods=['GET', 'POST'])
# def admin_panel():
#     if request.method == 'POST':
#         username = request.form.get('username')
#         password = request.form.get('password')
#
#         if authenticate_admin(username, password):
#             # Admin authentication successful
#             return render_template('admin_panel.html', doctors=doctors)
#         else:
#             # Admin authentication failed
#             return render_template('admin_login.html', message='Invalid credentials')
#
#     return render_template('admin_login.html')
#
#
# # Update doctor data
# @app.route('/admin/update/<int:doctor_id>', methods=['GET', 'POST'])
# def update_doctor(doctor_id):
#     # Ensure that only the admin can access this route
#     username = request.form.get('username')
#     password = request.form.get('password')
#
#     if not authenticate_admin(username, password):
#         return render_template('admin_login.html', message='Authentication required to update doctor data.')
#
#     if request.method == 'POST':
#     # Implement doctor data update logic here
#     # Make sure to update the 'doctors' list and the SQL database
#
#      return render_template('update_doctor.html', doctor=doctors[doctor_id])
#
#
# # Delete doctor data
# @app.route('/admin/delete/<int:doctor_id>')
# def delete_doctor(doctor_id):
#     # Ensure that only the admin can access this route
#     username = request.form.get('username')
#     password = request.form.get('password')
#
#     if not authenticate_admin(username, password):
#         return render_template('admin_login.html', message='Authentication required to delete doctor data.')
#
#     # Implement doctor data deletion logic here
#     # Make sure to update the 'doctors' list and the SQL database
#
#     return redirect(url_for('admin_panel'))
#
#
# # Download NLTK resources (uncomment the next two lines if not downloaded)
# # nltk.download('punkt')
# # nltk.download('stopwords')
#
# stop_words = set(stopwords.words('english'))
#
# # Load the trained model from the saved file
# with open('best_model.pkl2', 'rb') as model_file:
#     loaded_model = pickle.load(model_file)
#
# doctors = []
#
#
# # Load doctors from CSV file
# def load_doctors():
#     with open('doctors.csv', 'r') as csvfile:
#         reader = csv.DictReader(csvfile)
#         for row in reader:
#             doctors.append(row)
#
#
# # Populate doctors list at the start
# load_doctors()
#
#
# # Function to clean and tokenize text
# def clean_and_tokenize(text):
#     text = text.translate(str.maketrans('', '', string.punctuation))  # Remove Punctuation
#     text = re.sub(r'\d+', '', text)  # Remove Digits
#     text = text.replace('\n', ' ')  # Remove New Lines
#     text = text.strip()  # Remove Leading White Space
#     text = re.sub(' +', ' ', text)  # Remove multiple white spaces
#
#     # Tokenize text using NLTK
#     tokens = [word for word in word_tokenize(text) if word.lower() not in stop_words]
#     return ' '.join(tokens)
#
#
# @app.route('/')
# def index():
#     return render_template('index.html')
#
#
# @app.route('/recommend', methods=['POST'])
# def recommend():
#     if request.method == 'POST':
#         user_input = request.form['symptoms']
#         cleaned_user_input = clean_and_tokenize(user_input)
#         predicted_disease = loaded_model.predict([cleaned_user_input])[0]
#
#         # Retrieve doctors from the SQL database based on the "Disease Specialist" field
#         with sqlite3.connect('your_database.db') as connection:
#             cursor = connection.cursor()
#
#             # Use the "Disease Specialist" field for matching
#             cursor.execute("SELECT * FROM doctors WHERE disease_specialist = ?", (predicted_disease,))
#
#             matched_doctors = [dict(zip([column[0] for column in cursor.description], row)) for row in
#                                cursor.fetchall()]
#
#         return render_template('result.html', predicted_disease=predicted_disease, matched_doctors=matched_doctors)
#
#
# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         # Handle doctor registration form data
#         full_name = request.form.get('full_name')
#         degree = request.form.get('degree')
#         specialization = request.form.get('specialization')
#         disease_specialist = request.form.get('disease_specialist')
#         email = request.form.get('email')
#         contact = request.form.get('contact')
#         address = request.form.get('address')
#         country = request.form.get('country')
#         gender = request.form.get('gender')
#
#         # Handle image upload
#         file = request.files['file-input']
#         if file:
#             # Convert image to base64
#             image_data = base64.b64encode(file.read()).decode('utf-8')
#
#             # Save the doctor details to the SQL database
#             database_file = 'your_database.db'
#
#             # Create the database file if it doesn't exist
#             if not os.path.exists(database_file):
#                 with sqlite3.connect(database_file) as connection:
#                     cursor = connection.cursor()
#                     cursor.execute(
#                         """
#                         CREATE TABLE doctors (
#                             id INTEGER PRIMARY KEY AUTOINCREMENT,
#                             full_name TEXT,
#                             degree TEXT,
#                             specialization TEXT,
#                             disease_specialist TEXT,
#                             email TEXT,
#                             contact TEXT,
#                             address TEXT,
#                             country TEXT,
#                             gender TEXT,
#                             image_data TEXT
#                         );
#                         """
#                     )
#                     connection.commit()
#
#             with sqlite3.connect(database_file) as connection:
#                 cursor = connection.cursor()
#                 cursor.execute(
#                     """
#                     INSERT INTO doctors (full_name, degree, specialization, disease_specialist, email, contact, address, country, gender, image_data)
#                     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
#                     """,
#                     (full_name, degree, specialization, disease_specialist, email, contact, address, country, gender,
#                      image_data)
#                 )
#                 connection.commit()
#
#             # Add the doctor to the list
#             doctors.append({
#                 'full_name': full_name,
#                 'degree': degree,
#                 'specialization': specialization,
#                 'disease_specialist': disease_specialist,
#                 'email': email,
#                 'contact': contact,
#                 'address': address,
#                 'country': country,
#                 'gender': gender,
#                 'image_data': image_data
#             })
#
#         return render_template('index.html', message='Registration successful!')
#     return render_template('register.html')
#
#
# # Display all registered doctors in the admin panel
# @app.route('/admin', methods=['GET', 'POST'])
# def admin_panel():
#     if request.method == 'POST':
#         username = request.form.get('username')
#         password = request.form.get('password')
#
#         if authenticate_admin(username, password):
#             # Admin authentication successful
#             return render_template('admin_panel.html', doctors=doctors)
#         else:
#             # Admin authentication failed
#             return render_template('admin_login.html', message='Invalid credentials')
#
#     return render_template('admin_login.html')
#
#
# # Update doctor data
# @app.route('/admin/update/<int:doctor_id>', methods=['GET', 'POST'])
# def update_doctor(doctor_id):
#     # Ensure that only the admin can access this route
#     username = request.form.get('username')
#     password = request.form.get('password')
#
#     if not authenticate_admin(username, password):
#         return render_template('admin_login.html', message='Authentication required to update doctor data.')
#
#     if request.method == 'POST':
#         # Implement doctor data update logic here
#     # Make sure to update the 'doctors' list and the SQL database
#
#          return render_template('update_doctor.html', doctor=doctors[doctor_id])
#
#
# # Delete doctor data
# @app.route('/admin/delete/<int:doctor_id>')
# def delete_doctor(doctor_id):
#     # Ensure that only the admin can access this route
#     username = request.form.get('username')
#     password = request.form.get('password')
#
#     if not authenticate_admin(username, password):
#         return render_template('admin_login.html', message='Authentication required to delete doctor data.')
#
#     # Implement doctor data deletion logic here
#     # Make sure to update the 'doctors' list and the SQL database
#
#     return redirect(url_for('admin_panel'))
#
#
# # ... (existing code)
# if __name__ == '__main__':
#     app.run(debug=True)
#
#
#
#
#
#
# try4

import os
import sqlite3
import base64
import pandas as pd
from flask import Flask, render_template, request, redirect, url_for
import csv
import pickle
import string
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

app = Flask(__name__)

# Admin credentials
ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'admin_password'


# Admin authentication function
def authenticate_admin(username, password):
    return username == ADMIN_USERNAME and password == ADMIN_PASSWORD


# Load the trained model from the saved file
with open('best_model.pkl2', 'rb') as model_file:
    loaded_model = pickle.load(model_file)

# Download NLTK resources (uncomment the next two lines if not downloaded)
# nltk.download('punkt')
# nltk.download('stopwords')

stop_words = set(stopwords.words('english'))


# Function to clean and tokenize text
def clean_and_tokenize(text):
    text = text.translate(str.maketrans('', '', string.punctuation))  # Remove Punctuation
    text = re.sub(r'\d+', '', text)  # Remove Digits
    text = text.replace('\n', ' ')  # Remove New Lines
    text = text.strip()  # Remove Leading White Space
    text = re.sub(' +', ' ', text)  # Remove multiple white spaces

    # Tokenize text using NLTK
    tokens = [word for word in word_tokenize(text) if word.lower() not in stop_words]
    return ' '.join(tokens)


# Display all registered doctors in the admin panel
@app.route('/admin', methods=['GET', 'POST'])
def admin_panel():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if authenticate_admin(username, password):
            # Admin authentication successful
            doctors = load_doctors_from_database()
            return render_template('admin_panel.html', doctors=doctors)
        else:
            # Admin authentication failed
            return render_template('admin_login.html', message='Invalid credentials')

    return render_template('admin_login.html')


# Load doctors from the SQL database
def load_doctors_from_database():
    with sqlite3.connect('your_database.db') as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM doctors")
        doctors = [dict(zip([column[0] for column in cursor.description], row)) for row in cursor.fetchall()]
    return doctors


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/recommend', methods=['POST'])
def recommend():
    if request.method == 'POST':
        user_input = request.form['symptoms']
        cleaned_user_input = clean_and_tokenize(user_input)
        predicted_disease = loaded_model.predict([cleaned_user_input])[0]

        # Retrieve doctors from the SQL database based on the "Disease Specialist" field
        with sqlite3.connect('your_database.db') as connection:
            cursor = connection.cursor()

            # Use the "Disease Specialist" field for matching
            cursor.execute("SELECT * FROM doctors WHERE disease_specialist = ?", (predicted_disease,))

            matched_doctors = [dict(zip([column[0] for column in cursor.description], row)) for row in
                               cursor.fetchall()]

        return render_template('result.html', predicted_disease=predicted_disease, matched_doctors=matched_doctors)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Handle doctor registration form data
        full_name = request.form.get('full_name')
        degree = request.form.get('degree')
        specialization = request.form.get('specialization')
        disease_specialist = request.form.get('disease_specialist')
        email = request.form.get('email')
        contact = request.form.get('contact')
        address = request.form.get('address')
        country = request.form.get('country')
        gender = request.form.get('gender')

        # Handle image upload
        file = request.files['file-input']
        if file:
            # Convert image to base64
            image_data = base64.b64encode(file.read()).decode('utf-8')

            # Save the doctor details to the SQL database
            database_file = 'your_database.db'

            # Create the database file if it doesn't exist
            if not os.path.exists(database_file):
                with sqlite3.connect(database_file) as connection:
                    cursor = connection.cursor()
                    cursor.execute(
                        """
                        CREATE TABLE doctors (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            full_name TEXT,
                            degree TEXT,
                            specialization TEXT,
                            disease_specialist TEXT,
                            email TEXT,
                            contact TEXT,
                            address TEXT,
                            country TEXT,
                            gender TEXT,
                            image_data TEXT
                        );
                        """
                    )
                    connection.commit()

            with sqlite3.connect(database_file) as connection:
                cursor = connection.cursor()
                cursor.execute(
                    """
                    INSERT INTO doctors (full_name, degree, specialization, disease_specialist, email, contact, address, country, gender, image_data)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (full_name, degree, specialization, disease_specialist, email, contact, address, country, gender,
                     image_data)
                )
                connection.commit()

        return render_template('index.html', message='Registration successful!')

    return render_template('register.html')


# Update doctor data
@app.route('/admin/update/<int:doctor_id>', methods=['GET', 'POST'])
def update_doctor(doctor_id):
    # Ensure that only the admin can access this route
    username = request.form.get('username')
    password = request.form.get('password')

    if not authenticate_admin(username, password):
        return render_template('admin_login.html', message='Authentication required to update doctor data.')

    if request.method == 'POST':
        # Implement doctor data update logic here
        # Make sure to update the 'doctors' list and the SQL database

        return render_template('update_doctor.html', doctor=doctors[doctor_id])


# Delete doctor data
@app.route('/admin/delete/<int:doctor_id>')
def delete_doctor(doctor_id):
    # Ensure that only the admin can access this route
    username = request.form.get('username')
    password = request.form.get('password')

    if not authenticate_admin(username, password):
        return render_template('admin_login.html', message='Authentication required to delete doctor data.')

    # Implement doctor data deletion logic here
    # Make sure to update the 'doctors' list and the SQL database

    return redirect(url_for('admin_panel'))


if __name__ == '__main__':
    app.run(debug=True)
