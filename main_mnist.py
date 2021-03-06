from model import Layers, load_data, network

# hyper-parameters
learning_rate = 0.1
num_iter = 10000
batch_size = 128
lr_decay = [0.2, 6000]

# network
net = network.Network(learning_rate=learning_rate, num_iter=num_iter, batch_size=batch_size, lr_decay=lr_decay)

# layers
net.add_layer(Layers.Linear(n_in=28 * 28 * 1, n_out=1024))
net.add_layer(Layers.BatchNorm1d(n_in=1024))
net.add_layer(Layers.ReLU())
net.add_layer(Layers.Dropout(keep_prob=0.5))
net.add_layer(Layers.Linear(n_in=1024, n_out=10))
net.add_layer(Layers.CrossEntropyLoss())

# data
train, val, test = load_data.load_mnist()
net.load_data(train, val, test)

# training
net.train()
