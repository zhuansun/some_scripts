
- 参考老师的代码，手动实现一遍  transformer

老师给的代码中包括了
- data.txt 这是训练用的数据集
- dataloader.py 这是数据集的加载器
- tokenizer.py 数据集加载之后，要进行分词Embedding
- model.py 这是transformer的模型
- utils.py 这是一些工具函数
- main.py 这是对transformer又进行了一层封装，方便训练和推理

目前我认为，应该先从加载数据开始。所以我先实现 dataloader.py


我在实现dataloader的时候，发现使用到了 tokenizer.py 所以需要先去实现tokenizer.py
tokenizer.py中实现了
    - 定义了一个tokenizer类
    - 类中定义了 input 和 output 相关的参数： word2idx, idx2word, len
    - 定义了一些方法：保存字典文件，加载字典文件。
然后我们在回到dataloader.py中，继续我们数据集的加载
    - 数据集的加载依赖 tokenizer
    - 对数据集分批之后
    - 处理每一批的数据：
        - 这里有一个重点，也是核心。
        - 就是关于output的mask，是怎么掩盖掉未来词的
        - 主要是这个方法：subsequent_mask
最后dataloader处理完之后，就看model是怎么处理的了。


关于注意力是怎么算的？
- 参数有：q，k，v，mask，dropout
- 
