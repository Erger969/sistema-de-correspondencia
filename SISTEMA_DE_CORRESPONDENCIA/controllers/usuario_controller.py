from flask import request,redirecturl_form,blueprints

from models.usuario_model import Usuario 
from views import Usuario_view
usuario_bp = blueprint('usuario',__name__,url_prefix="/usuario")

@usuario_bp.route("/")
def index():
    return usuario_view.list(usuarios)

@usuario_bp.route("/create", methods=['GET','POST'])
def create ():
    if request.method=='POST':
        nombre = request.form  ['nombre']
        username = request.form['username']
        password = request.form['password']

        usuario = Usuario(nombre,username,password)
        usuario.save()
        return redirect(url_for('usuario.index'))
    return Usuario_view.create()

@usuario_bp.route("/edit/<int:id>",methods=['GET','POST'])
def edit(id):
    usuario = Usuario.get_by_id(id)
    if request.method == 'POST':
        nombre   = request.form  ['nombre']
        username = request.form['username']
        password = request.form['password']
        #ACTUALIZAR-----------------
        usuario.update(nombre=nombre,username=username,password=password)
        return redirect(url_for('usuario.index'))
    return Usuario_view.edit(usuario)

@usuario_bp.route("/delete/<int:id>")
def delete(id):
    usuario = Usuario.get_by_id(id)
    usuario.delete()
    return redirect(url_for('usuario.index'))