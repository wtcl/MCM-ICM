# 决策树
# matlab代码
# t = fitctree(A, B);  进行树的创建
# view(t,'Mode','graph');   进行树图的展示
# dtResubErr = resubLoss(t)  重新带入输出错误率


# 尝试对树进行剪枝。首先计算原始树的各种子集的再代入误差。然后计算这些子树的交叉验证误差。
# resubcost = resubLoss(t,'Subtrees','all');
# [cost,secost,ntermnodes,bestlevel] = cvloss(t,'Subtrees','all');
# plot(ntermnodes,cost,'b-', ntermnodes,resubcost,'r--')
# figure(gcf);
# xlabel('Number of terminal nodes');
# ylabel('Cost (misclassification error)')
# legend('Cross-validation','Resubstitution')
# 通过计算截止值（等于最小成本加上一个标准误差），您可以在图上显示这一点。由 cvloss 方法计算的“最佳”级别是此截止值下的最小树
# [mincost,minloc] = min(cost);
# cutoff = mincost + secost(minloc);
# hold on
# plot([0 20], [cutoff cutoff], 'k:')
# plot(ntermnodes(bestlevel+1), cost(bestlevel+1), 'mo')
# legend('Cross-validation','Resubstitution','Min + 1 std. err.','Best choice')
# hold off
# 查看修剪后的树
# pt = prune(t,'Level',bestlevel) 查看修建后的树
# view(pt,'Mode','graph')
# cost(bestlevel+1)  计算其误分类误差
# resubLoss(pt)   计算误分类误差