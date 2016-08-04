import sys
import jieba
import pickle

jieba.enable_parallel()

dic = {}
if len(sys.argv) <= 2:
    print ('[this] [filepath] [savepath]')
    sys.exit(0)
filepath = sys.argv[1]
savepath = sys.argv[2]
with open(filepath, 'r') as f:
    for line in f:
        res = jieba.cut(line)
        for word in res:
            if word in dic:
                dic[word] += 1
            else:
                dic[word] = 1

pickle.dump(dic, open(savepath,'wb'))
