intructions=[
    """CREATE TABLE IF NOT EXISTS tareas(
        id SERIAL NOT NULL,
        tarea varchar(255) NOT NULL,
        fecha TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        completed BOOLEAN NOT NULL
        );"""
]