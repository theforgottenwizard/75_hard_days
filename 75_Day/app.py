from flask import Flask, render_template,redirect, request 
import sqlite3 

app = Flask(__name__) 

# Connect to the database (creates if it doesn't exist)
conn = sqlite3.connect("your_database.db")  # Replace with your desired database name

# Create a cursor object
cursor = conn.cursor()

# # Create the table with the specified fields
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS days (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     diet BOOLEAN NOT NULL,
#     morning_workout BOOLEAN NOT NULL,
#     water BOOLEAN NOT NULL,
#     cheat_meal BOOLEAN NOT NULL,
#     picture BOOLEAN NOT NULL,
#     read BOOLEAN NOT NULL,
#     study BOOLEAN NOT NULL
# )
# """)
cursor.execute("""
    ALTER TABLE MyTable
    ALTER COLUMN bool_column1 SET DEFAULT 0,
    ALTER COLUMN bool_column2 SET DEFAULT 0,
    ALTER COLUMN bool_column3 SET DEFAULT 0,
    ALTER COLUMN bool_column4 SET DEFAULT 0,
    ALTER COLUMN bool_column5 SET DEFAULT 0;
               """)


# Commit the changes to the database
conn.commit()

# Close the connection
conn.close()

print("Table 'days' created successfully!")

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/day", methods=["POST","GET"])
def display_day():
    print(request.method)
    div_id = request.form.get("divId")
    return render_template("day.html")


@app.route("/submit_day", methods=["POST"])
def submit_days_work():
    diet = request.form.get("diet")
    water = request.form.get("water")
    study = request.form.get("study")
    morning_workout = request.form.get("morning_workout") 
    afternoon_workout = request.form.get("afternoon_workout") 
    cheat_meal = request.form.get("cheat_meal") 
    print(f"diet is {diet}, water is {water}, study is {study}, morning workout is {morning_workout}, afternoon workout is {afternoon_workout}, cheat_meal is {cheat_meal}")
    print(request.form)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)