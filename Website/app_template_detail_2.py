from flask import Flask, render_template
import sqlite3
import pathlib 

#basepath where the database is located
base_path = pathlib.Path(r'C:\Users\USER\Documents\GitHub\Project_Group3\Database')

#initializing flask
app = Flask(__name__, static_url_path='/static')
db_name = "Airlines.db"
db_path = base_path / db_name
print(db_path)

app = Flask(__name__)

#defining route for home page
@app.route("/")
def index():
    return render_template("index_links.html") 

#defining route for about page
@app.route("/about")
def about():
    return render_template("about.html")


#defining route for data page
@app.route("/data")
def data():
    con = sqlite3.connect(db_path)
    cursor = con.cursor()
    passenger = cursor.execute("SELECT * FROM passenger LIMIT 20").fetchall()
    con.close()

    return render_template("data_table.html", passenger=passenger)

#running flask application
if __name__=="__main__":
    app.run(debug=True)
