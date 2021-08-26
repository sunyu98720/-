import jieba
from flask import Flask

class test1:
    def testa(self):
        s = '上海自来水来自海上,黄山落叶松叶落山黄'
        print('全模式：')
        result = jieba.cut(s, cut_all=True)
        print(result)
        print(' '.join(result))

    def testb(self):
        from collections import Counter
        words_total = open('test', encoding='utf-8').read()
        c = Counter(words_total).most_common(20)
        print(c)
        vector = []
        for frequency in c:
            vector.append(frequency[1])
        print(vector)


if __name__ == '__main__':
    testaa = test1()
    # testaa.testa()
    testaa.testb()
