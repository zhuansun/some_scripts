import jieba
import os
from tqdm import tqdm
import torch
from opencc import OpenCC

opencc = OpenCC("t2s")

class Tokenizer(object):

    def __init__(self, file, save_dict):

        # 校验参数
        if not os.path.exists(file):
            raise FileNotFoundError(f"文件{file}不存在")
        if save_dict is None or save_dict == '':
            save_dict = os.path.join(os.path.dirname(file), "dict.pkl")

        self.file = file
        self.save_dict = save_dict

        self.input_word2idx = {}
        self.input_idx2word = {}
        self.input_dict_len = None
        self.input_embed_dim = 256
        self.input_hidden_size = 256

        self.output_word2idx = {}
        self.output_idx2word = {}
        self.output_dict_len = None
        self.output_embed_dim = 256
        self.output_hidden_size = 256
        # 推理时候输出的最大长度
        self.output_max_length = 100 

        # 英文的标点符号
        self.punctuations = [".",",","?","!"]

    def build_dict(self):
        
        # 判断是否存在本地字典集合
        if os.path.exists(path = self.save_dict):
            self.load()
            return
        
        input_words = {"<UNK>","<PAD>"}
        output_words = {"<UNK>","<PAD>","<SOS>","<EOS>"}

        # 读取文件
        with open(file=self.file,mode="r",encoding="utf-8") as f:
            for line in tqdm(f):
                if line:
                    input_sentence, output_sentence = line.strip().split("\t")
                    input_sentence_words = self.split_input(input_sentence)
                    output_sentence_words = self.split_output(output_sentence)
                    input_words = input_words.union(set(input_sentence_words))
                    output_words = output_words.union(set(output_sentence_words))
        # 输入字典
        self.input_word2idx = {word: idx for idx, word in enumerate(input_words)}
        self.input_idx2word = {idx: word for word, idx in self.input_word2idx.items()}
        self.input_dict_len = len(self.input_word2idx)
        # 输出字典
        self.output_word2idx = {word: idx for idx, word in enumerate(output_words)}
        self.output_idx2word = {idx: word for word, idx in self.output_word2idx.items()}
        self.output_dict_len = len(self.output_word2idx)
        # 保存字典
        self.save()

    def load(self):
        # 本地字典存在，加载本地字典文件
        if os.path.exists(path=self.save_dict):
            state_dict = torch.load(f=self.save_dict)
            self.input_word2idx = state_dict.get("input_word2idx")
            self.input_idx2word = state_dict.get("input_idx2word")
            self.input_dict_len = state_dict.get("input_dict_len")
            self.output_word2idx = state_dict.get("output_word2idx")
            self.output_idx2word = state_dict.get("output_idx2word")
            self.output_dict_len = state_dict.get("output_dict_len")
            print("本地字典加载成功")

    def split_input(self, sentence):
        # 分词 input
        """
        输入 I'm a student
        输出 ['i','m','a','student']
        """
        # 转小写
        sentence = sentence.lower()
        # 把缩写拆分成两个词
        sentence = sentence.replace("'"," ")
        # 把标点符合和单词分开
        sentence = "".join([" " + char + " " if char in self.punctuations else char for char in sentence])
        # 切分单词
        words = [word for word in sentence.split(" ") if word]
        # 返回形式 列表
        return words

    def split_output(self, sentence):
        # 分词 output
        """
        输入 我爱北京天安门
        输出 ['我','爱','北京','天安门']
        """
        # 繁体转简体
        sentence = opencc.convert(sentence)
        # jieba分词
        words = jieba.lcut(sentence)
        # 返回形式 列表
        return words

    def save(self):
        # 保存本地字典文件
        state_dict = {
            "input_word2idx": self.input_word2idx,
            "input_idx2word": self.input_idx2word,
            "input_dict_len": self.input_dict_len,
            "output_word2idx": self.output_word2idx,
            "output_idx2word": self.output_idx2word,
            "output_dict_len": self.output_dict_len
        }
        # 保存到文件
        torch.save(obj=state_dict,f=self.save_dict)
        print("保存本地字典成功")

    def encode_input(self, sentence, sentence_len):
        """
        将输入的句子，转变为指定长度的序列号
        输入：["i", "m", "a", "student"]
        输出：[5851, 4431, 6307, 1254, 2965]
        """
        # 变索引号
        # 遍历sentence中的每个word。
        # 将每个单词转换为其在词汇表中的索引。
        # 如果单词不在词汇表中，则使用 <UNK> 的索引。
        # 将所有索引收集到一个列表 input_idx 中。
        input_idx = [self.input_word2idx.get(word, self.input_word2idx.get("<UNK>")) for word in sentence]
        
        # 填充PAD
        # 将句子的索引列表 input_idx 填充到固定长度 sentence_len
        # 如果句子长度不足 sentence_len，则用 <PAD> 的索引进行填充。
        # 如果句子长度超过 sentence_len，则截断多余的元素。
        input_idx = (input_idx + [self.input_word2idx.get("<PAD>")] * sentence_len)[:sentence_len]

        return input_idx

    def encode_output(self, sentence, sentence_len):
            """
            将输出的句子，转变为指定长度的序列号
            输入：["我", "爱", "北京", "天安门"]
            输出：[11642, 10092, 5558, 3715, 10552, 1917]
            """
            # 添加结束标识符 <EOS>
            sentence = ["<SOS>"] + sentence + ["<EOS>"]
            # 长度也 + 2
            sentence_len = sentence_len + 2
            # 变 索引号
            output_idx = [self.output_word2idx.get(word, self.output_word2idx.get("<UNK>")) for word in sentence]
            # 填充 PAD
            output_idx = (output_idx + [self.output_word2idx.get("<PAD>")] * sentence_len)[:sentence_len]
            return output_idx
    
    # @classmethod 是一个装饰器，用于定义类方法。
    # 类方法的第一个参数是类本身（通常命名为 cls），而不是实例（self）。
    # 类方法可以通过类名直接调用，而不需要创建类的实例。
    @classmethod
    def make_std_mask(cls, tgt, pad):
        # 创建一个掩码，用于隐藏目标序列中的填充符号。
        # 结合未来单词掩码，防止模型在解码时看到未来的信息。
        # 返回最终的掩码张量，用于在模型中进行掩码操作。
        tgt_mask = (tgt != pad).unsqueeze(-2)
        tgt_mask = tgt_mask & Tokenizer.subsequent_mask(tgt.size(-1)).type_as(tgt_mask.data)
        return tgt_mask

    @classmethod
    def subsequent_mask(cls, size):
        # 生成一个形状为 (1, size, size) 的上三角矩阵，对角线及其以下为 0，对角线以上为 1。
        # 将矩阵的类型转换为 torch.uint8。
        attn_shape = (1, size, size)
        subsequent_mask = torch.triu(torch.ones(attn_shape), diagonal=1).type(torch.uint8)
        # 将矩阵中的值反转，使得对角线及其以下为 True，对角线以上为 False。
        return subsequent_mask == 0


    def __repr__(self):
        # 用于返回对象的“官方”字符串表示形式。它通常用于调试和开发阶段，提供关于对象的详细信息。
        return f"[ Tokenizer ]: 输入字典长度: {self.input_dict_len}, 输出字典长度: {self.output_dict_len}"



def get_tokenizer(file,save_dict="/Users/zhuansunpengcheng/workspace/github/some_scripts/python/AI/nlp/my_transformer/dicts.bin"):
    # 获取分词器
    tokenizer = Tokenizer(file=file,save_dict=save_dict)
    tokenizer.build_dict()
    return tokenizer

if __name__ == "__main__":
    # 测试
    tokenizer = get_tokenizer(
        file="/Users/zhuansunpengcheng/workspace/github/some_scripts/python/AI/nlp/my_transformer/data.txt",
        save_dict="/Users/zhuansunpengcheng/workspace/github/some_scripts/python/AI/nlp/my_transformer/dicts.bin"
        )
    print(tokenizer)