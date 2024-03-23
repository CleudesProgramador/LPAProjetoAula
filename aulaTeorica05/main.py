import sqlite3
import json
# #
# # # Conectando ao banco de dados (Cria um novo se não existir)
# #
# # conn = sqlite3.connect('animal.db')
# #
# # # Criando um cursor para executar comandos SQL
# #
# # cursor = conn.cursor()
# # #
# # # # Criando a tabela
# # #
# # # cursor.execute('''Create table if not exists dog(
# # #                id INTEGER PRIMARY KEY AUTOINCREMENT,
# # #                name TEXT,
# # #                age INTEGER,
# # #                weight REAL,
# # #                height REAL,
# # #                breed TEXT )''')
# # #
# # # # Exemplos de dados para inserir na tabela
# # #
# # pets_data = [
# #             ('Luke', 9, 45, 0.80, 'Pastor Alemão'),
# #             ('Buddy', 2, 7.2, 0.30, 'Golden Retriever'),
# #             ('Whiskers', 1, 1.2, 0.15, 'Siamese'),
# #             ('Max', 4, 5.0, 0.40, 'Labrador')
# #             ]
# #
# # # # # Inserindo os dados na tabela
# # # # for pet in pets_data:
# # # #     cursor.execute("Insert into dog"
# # # #                    "(name, age, weight, height, breed)"
# # # #                    "values (?, ?, ?, ?, ?) ", pet)
# # # #
# # # # # Commit das alterações
# # # #
# # conn.commit()
# # #
# # # # Selecionando todos os registros da tabela
# #
# # cursor.execute("SELECT * FROM dog")
# # rows = cursor.fetchall()
# #
# # # Mostrando os registros
# #
# # for row in rows:
# #     print(f"ID: {row[0]}, "
# #           f"Name: {row[1]}, "
# #           f"Age: {row[2]}, "
# #           f"Weight: {row[3]}, "
# #           f"Height: {row[4]}, "
# #           f"Breed: {row[5]} ")
# #
# # # Fechando a conexão com o banco de dados
# #
# # conn.close()
# #
# # #print('Registros inseridos com sucesso.')
#
#
# # Dados a serem salvos em um arquivo JSON
# #
# # data = {
# #     "name": "Luke",
# #     "age": 9,
# #     "weight": 45,
# #     "height": 0.8,
# #     "breed": "pastor alemão"
# # }
#
# # # Caminho para o arquivo JSON
# # file_path = "data.json"
# #
# # # Salvar dados em formato JSON no arquivo
# #
# # with open(file_path, "w") as json_file:
# #     json.dump(data, json_file, indent=4)
# #
# # print("Dados salvos em JSON. ")
# #
# # # Carregar dados de um arquivo JSON
# #
# # with open(file_path, "r") as json_file:
# #     loaded_data = json.load(json_file)
# #
# # print("Dados carregados do JSON: ")
# # print(loaded_data)
#
# import json
#
# class Dog:
#     def __init__(self,name,age,weight,height,breed):
#         self.name = name
#         self.age = age
#         self.weight = weight
#         self.height = height
#         self.breed = breed
#
# # Criando um objeto da classe Dog
# dog = Dog("Luke", 9, 45, 0.8, "Pastor Alemão")
#
# # Caminho para o arquivo JSON
# file_path = "dog.json"
#
# # Conectando o objeto para um dicionário
# dog_dict = {
#     "name": dog.name,
#     "age": dog.age,
#     "weight": dog.weight,
#     "height": dog.height,
#     "breed": dog.breed
# }
#
# #Salvando o dicionário em formato JSON no arquivo
# with open(file_path, "w") as json_file:
#     json.dump(dog_dict, json_file, indent=4)

# CLASSE DOG

class Dog:
    def __init__(self, name, age, weight, height, breed):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.breed = breed

# PROXY PARA INTERAGIR COM O BANCO DE DADOS SQLITE3
class DbProxy:
    def __init__(self, database_path='dogs.db'):
          self.database_path = database_path


    def insert_dog(self, new_dog):
        conn = sqlite3.connect(self.database_path)
        cursor = conn.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS dogs(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        age INTEGER,
                        weight REAL,
                        height REAL,
                        breed TEXT
                     )''')

        cursor.execute("INSERT INTO dogs "
                       "(name, age, weight, height, breed)"
                       "VALUES (?, ?, ?, ?, ?)",
                       (new_dog.name,
                        new_dog.age,
                        new_dog.weight,
                        new_dog.height,
                        new_dog.breed))

        conn.commit()
        conn.close()
        print("Dog inserted sucessfully.")

    def get_all_dogs(self):
        conn = sqlite3.connect(self.database_path)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM dogs")
        rows = cursor.fetchall()

        dogs = []
        for row in rows:
            dogs.append(Dog(row[1], row[2], row[3], row[4], row[5]))

        conn.close()
        return dogs


# Main #
# Criando um objeto Dog
dog = Dog("Luke", 10, 45, 0.80, "Pastor Alemão")

# Usando o Proxy para inserir o objeto no banco de dados
proxy = DbProxy()
proxy.insert_dog(dog)

# Usando o proxy para buscar todos os cachorros no banco de dados
all_dogs = proxy.get_all_dogs()
for d in all_dogs:
    print(f"Name: {d.name}, "
          f"Age: {d.age}, "
          f"Weight: {d.weight}, "
          f"Height: {d.height}, "
          f"Breed: {d.breed} ")

