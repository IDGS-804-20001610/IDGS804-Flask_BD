from dbi import get_connection


try: 
    connection = get_connection()
    with connection.cursor() as cursor:
        cursor.execute('CALL get_alumnos()')
        resultset = cursor.fetchall()
        for row in resultset:
            print(row)
            print(resultset)
    connection.close()
except Exception as ex:
    print(ex)



'''try: 
    connection = get_connection()
    with connection.cursor() as cursor:
        cursor.execute('CALL get_alumno(%s)', (1,))
        resultset = cursor.fetchall()
        for row in resultset:
            print(resultset)
    connection.close()
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