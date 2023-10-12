# https://zhuanlan.zhihu.com/p/33742983

# 首先调用obj=fitcdiscr(X,y)训练模型,其中obj为获得的大量参数的包裹，X 为数据集合，其中行表示样本，列表示指标特征，y为对应的样本的类别。再调用r=predict(obj,Z)来进行预测，r为获得的预测判别结果，Z为需要判别的矩阵（类似于X）。
# 建议用matlab实现

# lda = fitcdiscr(A,B);  进行分类训练
# ldaClass = resubPredict(lda);      用原始数据A代入分类模型进行预测
# ldaResubErr = resubLoss(lda)     对原始数据代入预测的错误率
# figure
# ldaResubCM = confusionchart(B,ldaClass);  对结果输出混淆矩阵（图片）


# 以上代码均为matlab代码，是LDA，即线性判别分类
# 如果原始数据中某些类呈现出协方差矩阵不同的状态，则可以使用QDA二次判别分析

# https://ww2.mathworks.cn/help/stats/classification-example.html
# matlab分类文档