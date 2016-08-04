import pickle

def top_words(dic_list, N):
    dic_all = {}
    for filename in dic_list:
        dic = pickle.load(open(filename, 'rb'))
        for word in dic:
            if word not in dic_all:
                dic_all[word] = dic[word]
            else:
                dic_all[word] += dic[word]
    forsort = []
    for word in dic_all:
        forsort.append((word, dic_all[word]))
    forsort = sorted(forsort, key=lambda x: x[1], reverse=True)
    ret_list = [forsort[i][0] for i in range(N)]
    return ret_list

dic_list = [
       './金庸/天龍八部/dic_tlon%02d' % i
       for i in range(1, 51)
]
res = top_words(dic_list, 300)
for word in res:
    print (word)
