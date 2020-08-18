from chapter02.thinkbayes2 import Pmf

# 概率质量函数
pmf = Pmf()
# 先验分布
pmf.Set('Bowl1', 0.5)
pmf.Set('Bowl2', 0.5)

pmf.Mult('Bowl1', 0.75)
pmf.Mult('Bowl2', 0.5)

# Mult 将给定假设的概率乘以已知的似然度

# 更新后的分布还没有归一化，但由于这些假设互斥且构成了完全集合（意味着完全包
# 含了所有可能假设），我们可以进行重新归一化如下
pmf.Normalize()

# 其结果是一个包含每个假设的后验概率分布，这就是所说的后验分布。
# 最后，我们可以得到假设碗1 的后验概率如下：
print(pmf.Prob('Bowl1'))
