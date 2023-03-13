from flask import Flask, render_template, request
import mysql.connector

# Create the Flask app
app = Flask(__name__)

# Define the database connection details
db = mysql.connector.connect(
  host="localhost",
  user="username",
  password="password",
  database="mydatabase"
)

# Define the table name
table_name = "household_inventory"

# Define a route to display the data
@app.route('/')
def home():
  # Create a cursor object
  cursor = db.cursor()

  # Retrieve the data from the table
  cursor.execute(f"SELECT * FROM {table_name}")
  data = cursor.fetchall()

  # Render the template with the data
  return render_template('index.html', data=data)

# Define a route to add data to the table
@app.route('/add', methods=['GET', 'POST'])
def add():
  if request.method == 'POST':
    # Get the data from the form
    item = request.form['item']
    location = request.form['location']
    category = request.form['category']
    quantity = request.form['quantity']
    expiration_date = request.form['expiration_date']
    purchase_date = request.form['purchase_date']
    purchase_price = request.form['purchase_price']
    supplier = request.form['supplier']
    warranty_start_date = request.form['warranty_start_date']
    warranty_end_date = request.form['warranty_end_date']
    usage_instructions = request.form['usage_instructions']

    # Create a cursor object
    cursor = db.cursor()

    # Insert the data into the table
    cursor.execute(f"INSERT INTO {table_name} (item, location, category, quantity, expiration_date, purchase_date, purchase_price, supplier, warranty_start_date, warranty_end_date, usage_instructions) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (item, location, category, quantity, expiration_date, purchase_date, purchase_price, supplier, warranty_start_date, warranty_end_date, usage_instructions))
    db.commit()

    # Redirect to the home page
    return redirect('/')
  
  # Render the template with the form
  return render_template('add.html')

if __name__ == '__main__':
  app.run(debug=True)
