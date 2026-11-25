let usarName = " breyner"
let passwordName = "b123456d"
let intentos = 1
do{
    let setUser = prompt("usuario de acceso").toLocaleLowerCase()
    let setPassword = prompt("password de acceso")
    if(setUser == usarName && setPassword == passwordName){
        let option = 0
        do {
        let option = parseInt(prompt(`¿que ejerccio desea ejecutar?:
            1 ejercicio 1
            2 ejercicio 2
            3 ejercicio 3
            4 ejercicio 4
            
            5 serrar sesion`))
        switch(option){
            case 1:
                alert("caso 1")
                break;
            case 2:
                alert("caso 2")
                break;
            case 3:
                alert("caso 3")
                break;
            case 4:
                alert("caso 4")
                break;
            case 5:
                alert("caso 5")
                break;
            
            default
        }}
        while(option !=5){}
    }else{
        alert("credenciales incorrectas")
        intentos++
    }
    if(intentos == 3){
        alert("cantidad de intentos superados \n tu usuaro a sido bloqueado ")
    
    }
    
    

}while(intentos <= 3){s   
}