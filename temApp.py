from db import get_connection

try: 
    connection = get_connection()
    with connection.cursor() as cursor:
        cursor.execute('call get_alumnos()')
        connection.close()
        resultset = cursor.fetchall()
        for row in resultset:
            print(row)
except Exception as ex:
    print(ex)

'''try: 
    connection = get_connection()
    with connection.cursor() as cursor:
        cursor.execute('call get_alumno(%s)', (1,))
        connection.close()
        resultset = cursor.fetchall()
        for row in resultset:
            print(resultset)
except Exception as ex:
    print(ex)'''

'''try: 
    connection = get_connection()
    with connection.cursor() as cursor:
        cursor.execute('call create_alumno(%s, %s, %s)', 
                       ('Luis', 'Lopez', 'lopez@gmail.com'))
        connection.commit()
        connection.close()
except Exception as ex:
    print(ex)'''