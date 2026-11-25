const guardar = () => {
    let data = JSON.parse(localStorage.getItem("DatosUsuario")) || []
    data.push({
        nombre : document.getElementById("nombre").value,
        apellido : document.getElementById("apellido").value,
    })
    localStorage.setItem("DatosUsuario",JSON.stringify(data))
    listarDatos()
}

function ObtenerDatos(){
    listarDatos()
}
function listarDatos(){
    let data = JSON.parse(localStorage.getItem("DatosUsuario")) || []
    let tabla = document.getElementById("tabla")
    tabla.innerHTML = ""
    data.forEach((usuario) => {
        let fila = document.createElement("tr")
        let nombre = document.createElement("td")
        let apellido = document.createElement("td")
        nombre.textContent = usuario.nombre
        apellido.textContent = usuario.apellido
        fila.append(nombre, apellido)
        tabla.appendChild(fila)
    })
}

listarDatos()
// para guardar un json uso un metodo
// JSON.stringify() para convertir el objeto en un string y poder guardarlo en el localStorage
//para obtener ese objeto
