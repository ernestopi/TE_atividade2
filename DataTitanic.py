import csv
'''
Para essa tarefa, escolhi o dataset "Titanic - Machine Learning from Disaster"
do Kaggle (https://www.kaggle.com/c/titanic).
'''

class TitanicPassageiros:
    def __init__(self, row):
        self.id = int(row['PassengerId'])
        self.survived = int(row['Survived'])
        self.pclass = int(row['Pclass'])
        self.name = row['Name']
        self.sex = row['Sex']
        self.age = float(row['Age']) if row['Age'] != '' else None
        self.sibsp = int(row['SibSp'])
        self.parch = int(row['Parch'])
        self.ticket = row['Ticket']
        self.fare = float(row['Fare'])
        self.cabin = row['Cabin']
        self.embarked = row['Embarked']

class TitanicDataset:
    def __init__(self, csv_file):
        self.passengers = []
        with open(csv_file, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                passenger = TitanicPassageiros(row)
                self.passengers.append(passenger)

    def total_passageiros_por_clase(self):
        class_counts = {}
        for passenger in self.passengers:
            if passenger.pclass in class_counts:
                class_counts[passenger.pclass] += 1
            else:
                class_counts[passenger.pclass] = 1
        return class_counts

    def total_passageiro_por_sexo(self):
        sex_counts = {}
        for passenger in self.passengers:
            if passenger.sex in sex_counts:
                sex_counts[passenger.sex] += 1
            else:
                sex_counts[passenger.sex] = 1
        return sex_counts

    def total_mortos_sobreviventes(self):
        count = {'Sobreviveu': 0,'Mortos': 0}
        for passengers in self.passengers:
            if passengers.survived == '1':
                count['Sobreviveu'] += 1
            else:
                count['Mortos'] += 1
        return count



'''
Nessa implementação, a classe Passageiro representa um passageiro do Titanic e tem atributos 
correspondentes aos campos do dataset. A classe TitanicDataset é responsável por ler os dados 
do arquivo .csv e criar uma lista de objetos Passenger.
Além disso, TitanicDataset possui alguns métodos que fornecem informações básicas sobre o conjunto
de dados, como o número total de passageiros, o número de sobreviventes, o número de passageiros 
em cada classe.
'''

titanic = TitanicDataset('train.csv')
print(f"Total de passageiros por classes: {titanic.total_passageiros_por_clase()}")
print(f"Total de passageiros por sexo: {titanic.total_passageiro_por_sexo()}")
print(f"Passageiros que sobreviveram e morreram: {titanic.total_mortos_sobreviventes()}")




