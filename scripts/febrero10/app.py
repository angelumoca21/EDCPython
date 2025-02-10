from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Conectar con MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="2196",
    database="tareas_db"
)
cursor = db.cursor()

@app.route("/")
def index():
    cursor.execute("SELECT * FROM tareas")
    tareas = cursor.fetchall()
    return render_template("index.html", tareas=tareas)

@app.route("/add", methods=["POST"])
def add():
    titulo = request.form["titulo"]
    descripcion = request.form["descripcion"]
    cursor.execute("INSERT INTO tareas (titulo, descripcion) VALUES (%s, %s)", (titulo, descripcion))
    db.commit()
    return redirect("/")

@app.route("/delete/<int:id>")
def delete(id):
    cursor.execute("DELETE FROM tareas WHERE id = %s", (id,))
    db.commit()
    return redirect("/")

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    if request.method == "POST":
        titulo = request.form["titulo"]
        descripcion = request.form["descripcion"]
        cursor.execute("UPDATE tareas SET titulo=%s, descripcion=%s WHERE id=%s", (titulo, descripcion, id))
        db.commit()
        return redirect("/")
    
    # Obtener datos de la tarea seleccionada
    cursor.execute("SELECT * FROM tareas WHERE id = %s", (id,))
    tarea = cursor.fetchone()
    
    return render_template("edit.html", tarea=tarea)

if __name__ == "__main__":
    app.run(debug=True)
