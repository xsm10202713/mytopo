[DCell_TRF_creater.cpp]() 用来生成指定 n 和 k 的 DCell 拓扑的 TRF 文件

关于 n 和 k 的定义，参见父目录里面的 《数据中心拓扑总结》

需要注意这个是 C++ 的代码，最初是 haibo 写的，我大概修改了一下，直接扔到一个 C++ 的 IDE 跑起来就可以了。我也放了一个编译好的exe，也不知道换台电脑能不能用。

> ofstream fout("dcell_2_6.txt"); //这句话控制输出文件的位置。

但是 [TRF]() 文件夹里面有之前我已经生成好的 DCell 的 TRF 文件，直接用就好了，并不真的需要使用[DCell_TRF_creater.cpp]()