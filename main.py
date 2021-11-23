from Stare import Stare
from Neuron import Neuron

n = int(input('Nr. epoci:'))
m = float(input('Rata de invatare:'))

s = Stare("date", n, m)
network = s.initialize_network(2, 1, 2)

s.train_network(m, n, 2)
for layer in network:
    print(layer)

for row in s.matrix:
    prediction = s.predict(row)
    print('Expected=%d, Got=%d' % (int(row[-1]), prediction))
