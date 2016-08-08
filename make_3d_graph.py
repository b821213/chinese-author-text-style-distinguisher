from sklearn import decomposition
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from filepaths import *
from run_test import get_features, train_set, test_set
import pickle

def splitter(lst_all, len_lst):
    ret = []
    for i in len_lst:
        ret.append(lst_all[: i])
        lst_all = lst_all[i :]
    return ret

feature_list = []
with open('feature_list', 'r') as f:
    for line in f:
        feature_list.append(line[:-1])

if __name__ == '__main__':
    black_list = [bm, lchen]
    train_data = list(filter(lambda x: x not in black_list, jinyung_all))
    train_X = []
    for filepaths in train_data:
        train_X += get_features(filepaths, feature_list, True)
    model = train_set(train_data, feature_list, 0.5, 0.03)
    y_pred_set = test_set(train_data, feature_list, model)
    y_res = []
    for acc, y_pred in y_pred_set:
        y_res += list(y_pred)
    forfilter = [(train_X[i], y_res[i]) for i in range(len(train_X))]
    neg_X = [ff[0] for ff in forfilter if ff[1] <= 0]
    pos_X = [ff[0] for ff in forfilter if ff[1] > 0]

    others = [bm, lchen]
    other_X = []
    for filepaths in others:
        other_X += get_features(filepaths, feature_list, True)

    pca = decomposition.PCA(n_components=3)
    pca.fit(neg_X + pos_X + other_X)
    X = pca.transform(neg_X + pos_X + other_X)

    split_res = splitter(X, [len(neg_X), len(pos_X), len(bm), len(lchen)])
    colors = ['m', 'g', 'y', 'r']
    scales = [20, 20, 50, 50]
    labels = ['neg', 'pos', 'bma', 'lchen']
    ax = plt.subplot(111, projection='3d')
    for i in range(len(split_res)):
        x = [p[0] for p in split_res[i]]
        y = [p[1] for p in split_res[i]]
        z = [p[2] for p in split_res[i]]
        ax.scatter(x, y, z, label=labels[i], c=colors[i], s=scales[i], edgecolor='white')
    ax.legend()
    plt.savefig('3d.png')
    plt.show()

