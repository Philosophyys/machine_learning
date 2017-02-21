KNN由三个部分组成：k值的选择、距离度量及分类决策规则 没有显式的学习过程，只是根据k个最近邻来多数表决该例属于的类别

使用MINIST数据集
数据来源：[THE MNIST DATABASE of handwritten digits]("http://yann.lecun.com/exdb/mnist/")
对于后缀名为idx3-ubyte的数据集，运行同一文件夹的Matlab文件，得到图像数据和标签数据
以下是KNN分类器在不同预处理情况下的错误率
| CLASSIFIER    | PREPROCESSING  | TEST ERROR RATE (%) |
| ------------- |:-------------:| -----:|
|K-nearest-neighbors, Euclidean (L2)|none|5.0|
| K-nearest-neighbors, Euclidean (L2) | none | 3.9 |
| K-nearest-neighbors, L3 | none | 2.83 |
| K-nearest-neighbors, Euclidean (L2) | deskewing | 2.4 |
| K-nearest-neighbors, Euclidean (L2) | deskewing, noise removal, blurring | 1.80 |
| K-nearest-neighbors, L3 | deskewing, noise removal, blurring | 1.73 |
| K-nearest-neighbors, L3 | deskewing, noise removal, blurring, 1 pixel shift | 1.33 |
| K-nearest-neighbors, L3 |  	deskewing, noise removal, blurring, 2 pixel shift | 1.22 |
| K-NN with non-linear deformation (IDM) | shiftable edges | 0.54 |
| K-NN with non-linear deformation (P2DHMDM) | shiftable edges | 0.52 |
| K-NN, Tangent Distance | subsampling to 16x16 pixels |1.1  |
| K-NN, shape context matching |  	shape context feature extraction | 0.63 |
