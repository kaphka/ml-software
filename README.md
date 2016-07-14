# ml-software

Diese Arbeit unsersucht die Untschiede in aktuellen Software-Frameworks für machinelles Lernen.

## Frameworks

| Framework |Homepage | Notebook |
| ------------- | ------------- |----|
| Theano  | https://github.com/Theano/Theano  |[Theano](theano.ipynb)|
| (Keras*)  | http://keras.io/  | |
| TensorFlow  | https://www.tensorflow.org/ |[TensorFlow](tensorflow.ipynb)|
| mxnet  | https://github.com/dmlc/mxnet |[mxnet](mxnet.ipynb)|

* Keras ist als Aufsatz für Theano zu betrachten,
da Theano im Vergleich zu den anderen Framework keine Methoden
zur einfachen Erstellung von neuronallen Netzen liefert

## Datensets

[Datensets-Beispiele](create_data.ipynb)

| Name | Ziel |
| ------------- | ------------- |
| Housing Data Set  | Multivariante Lineare Regression |
| Pima Indians Diabetes Data Set | Binäre Klassifikation |
| MNIST dataset | Multiklassen Klassifikation |
| CIFAR-10 dataset | Multiklassen Klassifikation |


## Strukturierung

Pro Framework liegt ein iPython Notebook vor.
Die Probleme sollen auf unterschiedliche Weise gelößt werden um
unterschiedliche Abstraktionsgrade der Framework zu untersuchen (von Low- zu High-Level).


1. Housing Data Set

 Erzeugung des Graphs

2. Pima Indians Diabetes Data Set

 Variablen im Graph

3. MNIST dataset

 Methoden zur Erstellung von Netzwerkstrukturen

4. CIFAR-10 dataset

 Aktuelle Methoden, Laden und anpassen

Jede Lösung besteht aus 3 Schritten: Modellierung, Training, Persistierung, Evaluierung und Visualisierung.
