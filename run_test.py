import pickle
import sys
from sklearn import svm
from filepaths import *

def get_features(dic_list, feature_list, use_list):
    """Gets the frequency vector of words on the feature list from dic files.

    dic_list:
        A list of filenames of the dic files.
    feature_list:
        A list of string containing key words.
    use_list:
        A boolean variable, which decides the type of the return value.
        If this is true, the return type will be a list; otherwise, it
        will be a dictionary.

    return:
        A vector whose dimension is len(feature_list), which may be
        a list or a dictionary, depanding on use_list. Each entry
        of the vector is the frequency of a word on the feature_list.
        Note that if use_list is false, the dictionary is indexed from
        one to easily use LibSVM later.
    """
    X = []
    for filename in dic_list:
        dic_x = {}
        list_x = []
        dic = pickle.load(open(filename, 'rb'))
        dic_size = 0
        word_black_list = ' \u3000\x00\n。：；！？，「」”“'
        for word in dic:
            if word not in word_black_list:
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

def train(train_X, nu, gamma):
    if gamma is not None:
        classifier = svm.OneClassSVM(gamma=gamma, nu=nu, kernel='rbf')
    else:
        classifier = svm.OneClassSVM(nu=nu, kernel='rbf')
    classifier.fit(train_X)
    return classifier

def test(test_X, test_Y, model):
    y_pred = model.predict(test_X)
    acc = (sum([1 if test_Y[i] == y_pred[i] else 0
            for i in range(len(test_X))]) / len(y_pred))
    return acc, y_pred

def train_set(to_train, feature_list, nu, gamma=None):
    """Trains a model using data in to_train.

    to_train:
        A list of works. A work is a list of filenames, where each filename
        is the path of the text of a chapter of the work.
        That is, to_train should be a list of lists of strings.
    feature_list:
        A list of string containing key words.
    nu, gamma:
        These two arguments are parameters of one-class SVM.

    return:
        A LibSVM model which is a binary classifier.
    """
    train_X = []
    for filenames in to_train:
        train_X += get_features(filenames, feature_list, True)
    # The following part is for an unsolved bug in LibSVM.
    # Please see https://github.com/cjlin1/libsvm/issues/69 for details.
    if len(train_X) % 2 > 0:
        import random
        train_X = train_X + [train_X[random.randint(0, len(train_X) - 1)]]
    return train(train_X, nu, gamma)

def test_set(to_test, feature_list, model):
    """Tests data in to_test by the given model.

    to_test:
        The format of to_test is similar to to_train in train_set.
    feature_list:
        A list of string containing key words.
    model:
        A model derived from train_set.

    return:
        A list of pairs, ([accuracy], [prediction of each chapter]),
        which are the results for each work.
        Here [accuracy] is defined as
            [number of chapters to be 1] / [number of chapters].
    """
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
    # Black list for jinyong
    black_list = [bmxx, bmyb, lcj]
    black_list_name = ['白馬嘯西風','白馬原版', '連城訣']
    train_data = jinyong_all
    train_data_name = jinyong_all_name
    train_data = list(filter(lambda x: x not in black_list, train_data))
    train_data_name = list(
            filter(lambda x: x not in black_list_name, train_data_name))
    gamma = 0.01
    # Cross validation
    acc_all = []
    acc_book = []
    for i in range(len(train_data)):
        to_train = train_data[: i] + train_data[i + 1 :]
        model = train_set(to_train, feature_list, 0.5, gamma=gamma)
        to_test = [train_data[i]]
        acc, y_pred = test_set(to_test, feature_list, model)[0]
        acc_book.append(acc)
        acc_all.append(y_pred)
    print ('gamma = %r' % gamma)
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
    model = train_set(to_train, feature_list, 0.5, gamma=gamma)
    # Testing
    to_test = jinyong_all + yusheng_all + other_martials + other_types
    to_test_name = (
            jinyong_all_name + yusheng_all_name +
            other_martials_name + other_types_name)
    for i, (acc, y_pred) in enumerate(test_set(to_test, feature_list, model)):
        print (to_test_name[i], ':', acc * 100,
                '(%d/%d)' % (count(y_pred, 1), len(y_pred)))
        print (y_pred)
