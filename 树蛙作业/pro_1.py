import numpy as np

class Min():
    def __init__(self):
        """初始化"""
        self.a_ = None
        self.b_ = None

    def train(self , x_train , y_train ):
        """训练"""
        assert x_train.ndim==1,\
            "基本条件"
        assert len(x_train)== len(y_train),\
            "基本条件"
        x_arr = np.nanmean(x_train)
        y_arr = np.nanmean(y_train)
        mom = 0.0
        son = 0.0
        mom += (x_train - x_arr).dot(y_train - y_arr)
        son += (x_train - x_arr).dot(x_train - x_arr)
        self.a_ = mom / son
        self.b_ = y_arr - self.a_ * x_arr
        return self

    def perdiect_solo(self,x_solo):
        """计算单个"""
        return self.a_*x_solo+self.b_

    def prediect(self,x_prediect):
        """预测"""
        assert x_prediect.ndim==1,\
        "是一维的矩阵"
        assert self.a_ is not None and self.b_ is not None,\
        "要先训练"

        for x in x_prediect:
            return self.perdiect_solo(x)

    def score(self,x_test,y_test):
        y_pre=self.prediect(x_test)
        return (1-np.nansum(y_test-y_pre)/np.nansum(y_test-np.nanmean(y_test)**2))


    def __repr__(self):
        return "pro_1()"



