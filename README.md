# Tecnologias Emergentes
Atividade 2

Acesse um repositório publico de Datasets (sugestão: kaggle.com), escolha um dataset e  implemente classes (1:N) que representem este dataset. Implemente um método para leitura desses dados e produza pelo menos 2 relatórios (criar 2 métodos)

Para essa tarefa, escolhi o dataset "Titanic - Machine Learning from Disaster"
do Kaggle (https://www.kaggle.com/c/titanic).

Nessa implementação, a classe Passageiro representa um passageiro do Titanic e tem atributos 
correspondentes aos campos do dataset. A classe TitanicDataset é responsável por ler os dados 
do arquivo .csv e criar uma lista de objetos Passenger.
Além disso, TitanicDataset possui alguns métodos que fornecem informações básicas sobre o conjunto
de dados, como o número total de passageiros, o número de sobreviventes, o número de passageiros 
em cada classe.
