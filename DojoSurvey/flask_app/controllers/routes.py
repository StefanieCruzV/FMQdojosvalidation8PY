from flask_app import app
from flask import render_template,redirect,request,session
from flask_app.models.user import User

@app.route("/")
def index():
    users = User.get_all() # regresa los valores del metodo get all y almacena todos los datos de lbd
    print(users)
    return render_template("index.html",users=users) 

@app.route("/result", methods=["POST"])
def result():
    # for key in request.form:
    #     print(key)
    #     print(request.form[key])
    if not User.validate_user(request.form):
        # redirect to the route where the burger form is rendered.
        return redirect('/')
    # else no errors:
    data = {
        "name": request.form["name"],
        "dojo_locsation": request.form["dojo_locsation"],
        "favorite_lenguage": request.form["favorite_lenguage"],
        "coments": request.form["comments"]
        # guarda los valores del formulario
        }
    id_new_user=User.save(data) # manda llamar al metodo para guardar
    new_data = {
        "id": id_new_user
    }
    user = User.get_user_by_id(new_data)
    return render_template("response.html", user=user)






# @app.route("/newuser")
# def newuser():
#     return render_template("newuser.html")
 
 

# @app.route('/create_user', methods=["POST"])
# def create_user():
#     data = {
#         "uname": request.form["uname"],
#         "ulastname": request.form["ulastname"],
#         "uemail": request.form["uemail"]
#         # guarda los valores del formulario
#         }
   
#     id=User.save(data) # manda llamar al metodo para guardar
#     print(id)
   
#     return redirect(f"/show_user/{id}")# lo que me regreso de la base al html
#         # si es otra pagina 

# @app.route('/delete_user/<int:id>')
# def delete_user(id):
#     print(id)
#     data = {
#         "id": id
#         }
#     User.delete(data)
#     users = User.get_all()
#     return render_template("users.html",users=users)
   


# @app.route('/show_user/<int:id>')
# def show_user(id):
#     print(id)
#     data = {
#         "id": id,
    
#         }
#     user_id = User.get_user_by_id(data)
#     print(user_id)
#     return render_template("showuser.html",user= user_id) # lo que me regreso de la base al html
#         # si es otra pagina 

# @app.route('/update_user/<int:id>')
# def update_user(id):
#     print(id)
#     data = {
#         "id": id
#         }
#     user_id = User.get_user_by_id(data)
#     print(user_id)
#     return render_template("updateuser.html",user_id= user_id) # lo que me regreso de la base al html
#         # si es otra pagina 

# @app.route('/update_user/<int:id>', methods=["POST"])
# def update_user_post(id):
#     print(id)
#     data = {
#         "id": id,
#         "uname": request.form["uname"],
#         "ulastname": request.form["ulastname"],
#         "uemail": request.form["uemail"]
#         }
#     User.update(data)
#     print(f"/show_user/{id}")
#     return redirect(f"/show_user/{id}") # lo que me regreso de la base al html
#         # si es otra pagina 