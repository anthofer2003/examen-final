from flask import Flask, render_template, request, redirect, url_for,flash
from dao.CargosDao import CargosDao


app = Flask(__name__)

# flash requiere esta sentencia
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/cargos-index')
def cargos_index():
    # Creacion de la instancia de cargodao
    cargoDao = CargosDao()
    lista_cargos = cargoDao.getCargos()
    return render_template('cargos-index.html', lista_cargos=lista_cargos)

@app.route('/cargos')
def cargos():
    return render_template('cargos.html')

@app.route('/guardar-cargo', methods=['POST'])
def guardarCargo():
    cargo = request.form.get('txtDescripcion').strip()
    if cargo == None or len(cargo) < 1:
        # mostrar un mensaje al usuario
        flash('Debe escribir algo en la descripcion', 'warning')

        # redireccionar a la vista cargos
        return redirect(url_for('cargos'))

    cargodao = CargosDao()
    cargodao.guardarCargo(cargo.upper())

    # mostrar un mensaje al usuario
    flash('Guardado exitoso', 'success')

    # redireccionar a la vista cargos
    return redirect(url_for('cargos_index'))

@app.route('/cargos-editar/<id>')
def cargosEditar(id):
    cargodao = CargosDao()
    return render_template('cargos-editar.html', cargo=cargodao.getCargoById(id))

@app.route('/actualizar-cargo', methods=['POST'])
def actualizarCargo():
    id = request.form.get('txtIdCargo')
    descripcion = request.form.get('txtDescripcion').strip()

    if descripcion == None or len(descripcion) == 0:
        flash('No debe estar vacia la descripcion')
        return redirect(url_for('cargosEditar', id=id))

    # actualizar
    cargodao = CargosDao()
    cargodao.updateCargo(id, descripcion.upper())

    return redirect(url_for('cargos_index'))

@app.route('/cargos-eliminar/<id>')
def cargosEliminar(id):
    cargodao = CargosDao()
    cargodao.deleteCargo(id)
    return redirect(url_for('cargos_index'))

# se pregunta por el proceso principal
if __name__=='__main__':
    app.run(debug=True)