from emple import Empleado
from ase import asesor
from perso import Persona

persona1 = Persona("3007", "Jn", "Gez", "000", "jjemplo.com", " 123")

print(f"Datos: {persona1.nombre} \n\
      {persona1.apellido},\n\
          Cel: {persona1.celular},\n\
              Tel: {persona1.telefono},\n\
                  Correo: {persona1.correo},\n\
                      Dir: {persona1.direccion}")