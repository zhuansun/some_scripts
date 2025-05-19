import numpy as np
from collections import Counter
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=True, test_size=0.2)


class MyKnn(object):
    def __init__(self, n_neighbors = 5):
        '''
            初始化方法
             - 处理超参的（什么是超参）
        '''
        self.n_neighbors = n_neighbors

    def _get_vec_similarity(self, vec1, vec2):
        '''
            内部辅助函数：用来计算余弦相似度的
        '''
        # np.linalg.norm 获取向量长度的
        return vec1 @ vec2 / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

    def fit(self, X, y):

        '''
            训练过程
        '''

        X = np.array(X)
        y = np.array(y)

        # 数据校验
        if X.ndim != 2 or y.ndim != 1 or X.shape[0] != y.shape[0]:
            raise ValueError('X and y must have the same shape 1111')

        # 把数据集挂在到模型上
        self.X = X
        self.y = y

    def predict(self, X):
        '''
            推理过程
        '''
        X = np.array(X)
        if X.ndim != 2 or X.shape[1] != self.X.shape[1]:
            raise ValueError('X and y must have the same shape 2222')

        results = []
        for x in X:
            # 自动广播机制计算当前 x 与所有的训练集的欧式距离
            similarities = np.array([self._get_vec_similarity(x, vec) for vec in self.X])
            # 找到最近的 n_neighbors 个邻居
            idxes = np.argsort(a=similarities)[::-1][:self.n_neighbors]
            # 取出这些邻居的标签
            labels = self.y[idxes]
            # 因为是分类问题，所以这里用的投票机制；如果是回归问题，这里直接求所有labels的平均值就可以了
            final = Counter(labels).most_common(1)[0][0]
            # 追加到结果中
            results.append(final)
        return np.array(results)

# 构建模型
my_knn = MyKnn(n_neighbors = 5)

# 训练模型
my_knn.fit(X = X_train, y = y_train)

# 模型的预测/测试/推理 predict test infer
y_pred = my_knn.predict(X = X_test)

acc = (y_pred == y_test).mean()

print(acc)