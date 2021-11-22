import numpy as np
from sklearn.datasets import make_blobs

X_1, y_1 = make_blobs(n_samples=800_000, centers=5, n_features=2, cluster_std=1, random_state=0)
X_2 = np.random.uniform(-10,10,[5_000,2])

y_2 = 5 * np.ones(5_000)

# X_2, y_2 = make_blobs(n_samples=200_000, centers=200_000, n_features=2, cluster_std=2, random_state=0)
# y_2 += 5

X = np.concatenate([X_1, X_2])
Y = np.concatenate([y_1, y_2])

z = np.zeros(len(Y))
means= [2, 4, 6, 8, 9]
for i in range(5):
    z[Y == i] = np.random.normal(means[i], 1, sum(Y == i))
z[Y > 4] = np.random.uniform(5000, 75_000, sum(Y > 4))

X_z = np.append(X, z.reshape(-1,1), 1)
np.random.shuffle(X_z)
np.savetxt("data/temp.txt", X_z, delimiter='\t')
