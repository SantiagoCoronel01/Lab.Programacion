alumno1 = {
    'nombre': 'santiago',
    'edad': 15,
    'apellido': 'coronel'
}

alumno2 = {
    'nacimiento':'07/09/2007',
    'pais': 'argentina',
    'telefono': '1140589301'
}


alumno = alumno1.copy()
alumno.update(alumno2)


print(alumno)