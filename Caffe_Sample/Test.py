import sys
import pickle
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
sys.path.append('/home/d/Documents/caffe/python')
import caffe

net = caffe.Net('test.prototxt', 'simple_mlp_iter_2000.caffemodel', caffe.TEST)

with open('data.pkl', 'rb') as f:
    samples, labels = pickle.load(f)
samples = np.array(samples)
labels = np.array(labels)

X = np.arange(0, 1.05, 0.05)
Y = np.arange(0, 1.05, 0.05)
X, Y = np.meshgrid(X, Y)

grids = np.array([[X[i][j], Y[i][j]] for i in range(X.shape[0]) for j in range(X.shape[1])])

grid_probs = []
for grid in grids:
    net.blobs['data'].data[...] = grid.reshape((1, 2))[...]
    output = net.forward()
    grid_probs.append(output['prob'][0][1])
grid_probs = np.array(grid_probs).reshape(X.shape)
fig = plt.figure('Sample Surface')
ax = fig.gca(projection='3d')
ax.plot_surface(X, Y, grid_probs, alpha=0.15, color='k', rstride=2, cstride=2, lw=0.5)

samples0 = samples[labels==0]
samples0_probs = []
for sample in samples0:
    net.blobs['data'].data[...] = sample.reshape((1, 2))[...]
    output = net.forward()
    samples0_probs.append(output['prob'][0][1])
samples1 = samples[labels==1]
samples1_probs = []
for sample in samples1:
    net.blobs['data'].data[...] = sample.reshape((1, 2))[...]
    output = net.forward()
    samples1_probs.append(output['prob'][0][1])

ax.scatter(samples0[:, 0], samples0[:, 1], samples0_probs, c='r', marker='o', s=50)
ax.scatter(samples1[:, 0], samples1[:, 1], samples1_probs, c='b', marker='^', s=50)

plt.show()


