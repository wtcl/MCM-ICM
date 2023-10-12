# https://blog.csdn.net/qq_23590921/article/details/84310115
# 朴素贝叶斯分类基本概念

# matlab代码
# nbGau = fitcnb(A,B) A为特征值矩阵，B为类别
# nbGauResubErr = resubLoss(nbGau)  输出错误率
# 下面这个属于QDA
# cp = cvpartition(A(:),'KFold',10)  使用 cvpartition 生成 10 个不相交的分层子集
# nbGauCV = crossval(nbGau, 'CVPartition',cp);
# nbGauCVErr = kfoldLoss(nbGauCV)

# 使用核密度估计对每个类中的每个变量进行建模，这是一种更灵活的非参数化方法。此处我们将核设置为 box。
# nbKD = fitcnb(A,B, 'DistributionNames','kernel', 'Kernel','box')
# nbKDResubErr = resubLoss(nbKD)
# 下面属于QDA
# cp = cvpartition(A(:),'KFold',10)  使用 cvpartition 生成 10 个不相交的分层子集
# nbKDCV = crossval(nbKD, 'CVPartition',cp);
# nbKDCVErr = kfoldLoss(nbKDCV)

