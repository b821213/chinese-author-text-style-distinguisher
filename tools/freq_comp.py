import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
print ('current_dir: %s' % current_dir)
parent_dir = current_dir + '/..'
if parent_dir not in sys.path:
    sys.path.append(parent_dir)
from filepaths import *
import pickle

def open_dic(filepath):
    with open(filepath, 'rb') as f:
        dic = pickle.load(f)
    return dic

def merge_dic(dic_set):
    dic_all = {}
    for dic in dic_set:
        for word in dic:
            if word in dic_all:
                dic_all[word] += dic[word]
            else:
                dic_all[word] = dic[word]
    return dic_all

def in_list_rate(dic, feature_list):
    sum_all = 0
    sum_in_list = 0
    for word in dic:
        if word in feature_list:
            sum_in_list += dic[word]
        sum_all += dic[word]
    return sum_in_list / sum_all

def merge_word_list(dic1, dic2):
    word_list_all = [word for word in dic1]
    for word in dic2:
        if word not in dic1:
            word_list_all.append(word)
    return word_list_all

def get_freq(word, dic, word_sum):
    if word in dic:
        return dic[word] / word_sum
    else:
        return 0

feature_list = []
with open('../feature_list', 'r') as f:
    for line in f:
        feature_list.append(line[: -1])

set1 = [book for book in jinyong_all
        if book != lcj and book != bmxx and book != bmyb]
set2 = [bmxx]

set1_all = []
for book in set1:
    set1_all += [open_dic(chapter) for chapter in book]
set2_all = []
for book in set2:
    set2_all += [open_dic(chapter) for chapter in book]

set1_dic = merge_dic(set1_all)
set2_dic = merge_dic(set2_all)
word_black_list = ' \u3000\x00\n。：；！？，「」”“'
for word in word_black_list:
    set1_dic.pop(word, None)
    set2_dic.pop(word, None)
set1_sum = sum([set1_dic[word] for word in set1_dic])
set2_sum = sum([set2_dic[word] for word in set2_dic])
set1_other_rate = 1 - in_list_rate(set1_dic, feature_list)
set2_other_rate = 1 - in_list_rate(set2_dic, feature_list)
word_list_all = merge_word_list(set1_dic, set2_dic)

set1_sorted = sorted(
        [(word, set1_dic[word] / set1_sum) for word in set1_dic],
        key=lambda x: x[1], reverse=True)
set2_sorted = sorted(
        [(word, set2_dic[word] / set2_sum) for word in set2_dic],
        key=lambda x: x[1], reverse=True)
diff_list = [
        (word,
        (get_freq(word, set2_dic, set2_sum) -
        get_freq(word, set1_dic, set1_sum)) /
        get_freq(word, set1_dic, set1_sum))
        for word in feature_list]
diff_list = sorted(diff_list, key=lambda x: abs(x[1]), reverse=True)

for pair  in diff_list:
    print (pair)

