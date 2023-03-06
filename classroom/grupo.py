from classroom.asignatura import Asignatura

class Grupo:
    grado = "Grado 12"

    def __init__(self, grupo="grupo predeterminado", asignaturas=[], estudiantes=[]):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes
        

    def listadoAsignaturas(self, **kwargs):
        for x in kwargs.values():
            if self._asignaturas != None:
                self._asignaturas.append(Asignatura(x))
            else:
                self._asignaturas = [Asignatura(x)]
    def agregarAlumno(self, alumno, lista=None):
        if lista!= None:
            lista.append(alumno)
        else:
            lista = [alumno]
        if self.listadoAlumnos != None:
            self.listadoAlumnos = self.listadoAlumnos
        else:
            self.listadoAlumnos = lista

    def __str__(self):
        return "Grupo de estudiantes: "+ self._grupo

    @ classmethod
    def asignarNombre(cls, nombre="Grado 10"):
        cls.grado = nombre

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre
