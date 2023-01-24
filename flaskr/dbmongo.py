from mongoengine import connect

MONGO_URI='mongodb://localhost:27017/mydb'

def dbConnection():
    try:
        client = connect(host=MONGO_URI)
    except ConnectionError:
        print('Error de conexion con la base de datos')
    return None