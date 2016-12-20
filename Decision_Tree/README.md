<script type="text/javascript"<src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS_HTML"></script>
#简介
决策树是对实例进行分类的树形结构，由节点和有向边组成,其中节点分为内部节点和叶子节点.内部节点对应特征(规则)，叶子节点对应各个类别.**需要保证特征(规则)互斥且完备**
<div align=center>![Decision_Tree](Decision_Tree.PNG)</div>
建立决策树的过程，就是依次选择最优特征的过程.
##ID3
ID3的核心是依据**信息增益**选择特征.

* 熵
$$
H(X)=-\sum_{i=1}^{n}p_{i}\log p_i
$$

* 条件熵
$$
H(Y|X)=\sum_{i=1}^n p_iH(Y|X=x_i)
$$
其中
$$
p_i=p(X=x_i) \\\\
H(Y|X=x_j)=-\sum_{i=1}^np(y_i|X=x_j)\log p(y_i|X=x_j)
$$

* 信息增益
$$
g(D,A)=H(D)-H(D|A)
$$
其中$A$表示特征，$D$表示数据集，上式表示由于特征$A$的加入，使得对数据集$D$分类的不确定性的减少.

##C4.5
C4.5的核心是依据**信息增益比**选择特征.克服信息增益的缺点，倾向于选择取值较多的属性.

* 信息增益比
$$
g_R={{g(D,A)}\over {H_A(D)}}
$$

* 连续属性的分界点
对于连续型的属性，原始的C4.5算法通过将$k$个值划分为$k-1$个区间，对每个区间取分割点$a_i=(A_i+A_{i+1})/2$，对每种分割情况计算其信息增益比，取信息增益比最大的分割情况.
改进的C4.5对于连续属性的分界点，则是直接在类型变化的边界点上选择.

##CART(Classification and Regression Tree)


* 基尼指数
$$
G
$$