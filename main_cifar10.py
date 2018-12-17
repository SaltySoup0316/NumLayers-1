from model import Layers, load_data
from model.network import Network

# hyper-parameters
learning_rate = 0.01
num_iter = 10000
batch_size = 128

# network
net = Network(learning_rate=learning_rate, num_iter=num_iter, batch_size=batch_size, lr_decay=None)

# layers
net.add_layer(Layers.Linear(n_in=32 * 32 * 3, n_out=1024))
net.add_layer(Layers.BatchNorm1d(n_in=1024))
net.add_layer(Layers.ReLU())
net.add_layer(Layers.Dropout(keep_prob=0.5))
net.add_layer(Layers.Linear(n_in=1024, n_out=1024))
net.add_layer(Layers.BatchNorm1d(n_in=1024))
net.add_layer(Layers.ReLU())
net.add_layer(Layers.Dropout(keep_prob=0.5))
net.add_layer(Layers.Linear(n_in=1024, n_out=10))
net.add_layer(Layers.CrossEntropyLoss())

# data
train, val, test = load_data.load_cifar10()
net.load_data(train, val, test)

# training
net.train()
