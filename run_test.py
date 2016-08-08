import pickle
import sys
from sklearn import svm
from filepaths import *

def get_features(dic_list, feature_list, use_list):
    X = []
    for filename in dic_list:
        dic_x = {}
        list_x = []
        dic = pickle.load(open(filename, 'rb'))
        dic_size = 0
        for word in dic:
            dic_size += dic[word]
        for index, word in enumerate(feature_list):
            if word not in dic:
                if use_list:
                    list_x.append(0)
            else:
                if use_list:
                    list_x.append(dic[word] / dic_size)
                else:
                    dic_x[index + 1] = dic[word] / dic_size
        if use_list:
            X.append(list_x)
        else:
            X.append(dic_x)
    return X

def test(test_X, test_Y, model):
    y_pred = model.predict(test_X)
    acc = (sum([1 if test_Y[i] == y_pred[i] else 0
            for i in range(len(test_X))]) / len(y_pred))
    return acc, y_pred

def train_set(to_train, nu, gamma=None):
    train_X = []
    for filenames in to_train:
        train_X += get_features(filenames, feature_list, True)
    if len(train_X) % 2 > 0:
        import random
        train_X = train_X + [train_X[random.randint(0, len(train_X) - 1)]]
    if gamma is not None:
        classifier = svm.OneClassSVM(gamma=gamma, nu=nu, kernel='rbf')
    else:
        classifier = svm.OneClassSVM(nu=nu, kernel='rbf')
    classifier.fit(train_X)
    return classifier

def test_set(to_test, model):
    res = []
    for filenames in to_test:
        test_X = get_features(filenames, feature_list, True)
        test_Y = [1 for i in range(len(test_X))]
        acc, y_pred = test(test_X, test_Y, model)
        res.append((acc, y_pred))
    return res

def count(iterable, element):
    ret = 0
    for i in iterable:
        if i == element:
            ret += 1
    return ret

if __name__ == '__main__':
    feature_list = []
    with open('feature_list', 'r') as f:
        for line in f:
            feature_list.append(line[:-1])
    # Use black_list to drop the amgiguous data
    black_list = [bm, lchen]
    black_list_name = ['bm', 'lchen']
    train_data = list(filter(lambda x: x not in black_list, jinyung_all))
    train_data_name = list(
            filter(lambda x: x not in black_list_name, jinyung_all_name))
    # Cross validation
    acc_all = []
    acc_book = []
    for i in range(len(train_data)):
        to_train = train_data[: i] + train_data[i + 1 :]
        model = train_set(to_train, 0.5, gamma=0.03)
        to_test = [train_data[i]]
        acc, y_pred = test_set(to_test, model)[0]
        acc_book.append(acc)
        acc_all.append(y_pred)
    print ('Cross validation result:')
    for index in range(len(train_data)):
        print (train_data_name[index], ':', acc_book[index],
                '(%d/%d)' % (count(acc_all[index], 1), len(acc_all[index])))
        print (acc_all[index])
    print ('Cross validation accuracy: %r' %
            (sum([count(x, 1) for x in acc_all]) /
            sum([len(x) for x in acc_all])))
    print ('Book-wise accuracy: %r' % (sum(acc_book) / len(acc_book)))
    # Real training
    to_train = train_data
    model = train_set(to_train, 0.5, gamma=0.03)
    to_test = jinyung_all + other_martials + other_types
    to_test_name = jinyung_all_name + other_martials_name + other_types_name
    for i, (acc, y_pred) in enumerate(test_set(to_test, model)):
        print (to_test_name[i], ':', acc * 100,
                '(%d/%d)' % (count(y_pred, 1), len(y_pred)))
        print (y_pred)
