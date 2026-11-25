const guardar = () => {
    let data = JSON.parse(localStorage.getItem("DatosUsuario")) || []
    data.push({
        nombre : document.getElementById("nombre").value,
        apellido : document.getElementById("apellido").value,
        numero : document.getElementById("numero").value,
        tipoDocumento : document.getElementById("tipoDocumento").value,
        numeroDocumento : document.getElementById("numeroDocumento").value,
        gmail : document.getElementById("gmail").value,
    })
    localStorage.setItem("DatosUsuario",JSON.stringify(data))
    listarDatos()

    if (typeof exito === "function" && typeof Swal !== "undefined") {
        exito()
    }
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
        let numero = document.createElement("td")
        let tipoDocumento = document.createElement("td")
        let numeroDocumento = document.createElement("td")
        let gmail = document.createElement("td")
        nombre.textContent = usuario.nombre
        apellido.textContent = usuario.apellido
        numero.textContent = usuario.numero
        tipoDocumento.textContent = usuario.tipoDocumento
        numeroDocumento.textContent = usuario.numeroDocumento
        gmail.textContent = usuario.gmail
        fila.append(nombre, apellido, numero, tipoDocumento, numeroDocumento, gmail)
        tabla.appendChild(fila)
    })
}

listarDatos()
// para guardar un json uso un metodo
// JSON.stringify() para convertir el objeto en un string y poder guardarlo en el localStorage
//para obtener ese objeto
