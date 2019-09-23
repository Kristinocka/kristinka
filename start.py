import mysql.connector

my_database = mysql.connector.connect(user='root', password='kristi',
                                      host='127.0.0.1', database='kristinka',
                                      auth_plugin='caching_sha2_password')
# print(my_database)
cursor = my_database.cursor()


def create_table(tb_name):
    cursor.execute('CREATE TABLE IF NOT EXISTS ' + tb_name + '(id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY )')
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()  ## zwraca wszystkie tabele, nie działa bez cursor.execute("SHOW TABLES")

    ## showing all the tables one by one
    print("Tabela stan: po dodaniu")
    for table in tables:
        print(table)


def remove_table(tb_name):
    query_drop_table = 'DROP TABLE IF EXISTS ' + tb_name
    cursor.execute(query_drop_table)

    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()  ## zwraca wszystkie tabele, nie działa bez cursor.execute("SHOW TABLES")

    print('________')
    print("Tabela stan: po usunięciu")
    for table in tables:
        print(table)


def show_all_tables():
    cursor.execute("SHOW TABLES")
    print(cursor.fetchall())


def show_all_columns(tb_name):
    cursor.execute("SHOW columns FROM " + tb_name)
    # cursor.execute("desc " + tb_name)
    print(cursor.fetchall())


# def test(db_name, *args):
#     list_of_args = []
#     if not args:
#         args = ''
#     else:
#         for arg in args:
#             list_of_args.append(arg)
#
#     print('nazwa tabeli: ' + str(db_name))
#     print('lista argumentów wygląda tak: ' + str(list_of_args))
#
#
#     list_of_args = str(list_of_args)
#
#
# # test('nowa_tabela','pierwszy', 'drugi', 'trzeci')
# test('nowatabela', 'name VARCHAR(255)')

def check_if_column_exists(tb_name, cl_name):
    query = "SHOW COLUMNS FROM `" + tb_name + "` LIKE '" + cl_name + "'"
    cursor.execute(query)
    msg = cursor.fetchone()  ## zwraca wszystkie tabele, nie działa bez cursor.execute("SHOW TABLES")
    return msg


def add_column(tb_name, cl_name, cl_type, *args):
    check = check_if_column_exists(tb_name, cl_name)
    print(check)
    if check != None:
        print("Column " + cl_name + " already exists")
    else:
        list_of_args = []

        if not args:
            args = ''
        else:
            for arg in args:
                list_of_args.append(arg)

        query = cl_name + ' ' + cl_type + ' ' + ''.join(list_of_args)
        cursor.execute('ALTER TABLE ' + tb_name + ' ADD COLUMN ' + query + '')
        print('Column ' + cl_name + ' was succesfullly created')


def remove_column(tb_name, cl_name):
    check = check_if_column_exists(tb_name, cl_name)
    print('----')
    print(check)
    if check == None:
        print('There is no such column in your ' + tb_name + ' table')
    else:
        cursor.execute('ALTER TABLE ' + tb_name + ' DROP COLUMN ' + cl_name + '')
        print('Column ' + cl_name + ' was succesfullly removed')

# create_table('testowa')
# check_if_column_exists('testowa', 'date4')
# add_column('testowa', 'date4', 'VARCHAR(255)')
# check_if_column_exists('testowa', 'date4')
# remove_column('testowa', 'date4')
# remove_column('testowa', 'date3')
# show_all_columns('testowa')
# remove_table('ulubione_rzeczy')
# show_all_tables()
#