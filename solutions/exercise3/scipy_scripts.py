import numpy as np
import matplotlib.pyplot as plt

# numpy load I_q_IPA_exp.npy
data = np.load('I_q_IPA_exp.npy')
model = np.load('I_q_IPA_model.npy')

x = data[:, 0]
y = data[:, 1]

fig = plt.figure()
ax  = fig.add_subplot(111)
ax.plot(x, y, 'o', label='data')