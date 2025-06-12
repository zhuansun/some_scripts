import torch
from torch import nn
from torch.nn.functional import log_softmax
import copy
import math

device = "cuda:0" if torch.cuda.is_available() else "cpu"



class PositionalEncoding(nn.Module):
    "Implement the PE function."

    def __init__(self, d_model, dropout, max_len=5000):
        super(PositionalEncoding, self).__init__()
        self.dropout = nn.Dropout(p=dropout)

        # Compute the positional encodings once in log space.
        pe = torch.zeros(max_len, d_model)
        position = torch.arange(0, max_len).unsqueeze(1)
        div_term = torch.exp(
            torch.arange(0, d_model, 2) * -(math.log(10000.0) / d_model)
        )
        pe[:, 0::2] = torch.sin(position * div_term)
        pe[:, 1::2] = torch.cos(position * div_term)
        pe = pe.unsqueeze(0)
        self.register_buffer("pe", pe)

    def forward(self, x):
        print("调用 PositionalEncoding 的 forward")
        x = x + self.pe[:, : x.size(1)].requires_grad_(False)
        return self.dropout(x)


class Embeddings(nn.Module):
    def __init__(self, d_model, vocab):
        super(Embeddings, self).__init__()
        self.lut = nn.Embedding(vocab, d_model)
        self.d_model = d_model

    def forward(self, x):
        print("调用 Embedding 的 forward")
        return self.lut(x) * math.sqrt(self.d_model)


class LayerNorm(nn.Module):
    """ 层规范化 """
    def __init__(self, features, eps = 1e-6):
        super(LayerNorm, self).__init__()
        # 定义了两个可训练参数 a_2 和 b_2。
        # a_2 的初始值为全 1 的张量，形状为 (features,)。
        # b_2 的初始值为全 0 的张量，形状为 (features,)。
        self.a_2 = nn.Parameter(torch.ones(features))
        self.b_2 = nn.Parameter(torch.zeros(features))
        self.eps = eps
    def forward(self, x):
        # 计算张量 x 在最后一个维度上的均值。
        print("调用 LayerNorm 的 forward")
        mean = x.mean(-1, keepdim=True)
        std = x.std(-1, keepdim=True)
        return self.a_2 * (x - mean) / (std + self.eps) + self.b_2


class EncoderLayer(nn.Module):
    def __init__(self, size, self_attn, feed_forward, dropout):
        super(EncoderLayer, self).__init__()
        self.size = size
        self.self_attn = self_attn
        self.feed_forward = feed_forward
        self.sublayer = clones(SublayerConnection(size, dropout), 2)
    def forward(self, x, mask):
        "Follow Figure 1 (left) for connections."
        print("调用 EncoderLayer 的 forward")
        x = self.sublayer[0](x, lambda x: self.self_attn(x, x, x, mask))
        return self.sublayer[1](x, self.feed_forward)


class SublayerConnection(nn.Module):
    """
    残差网络
    A residual connection followed by a layer norm.
    Note for code simplicity the norm is first as opposed to last.
    一个残差连接后跟一个层归一化。注意，为了代码简洁，归一化是首先进行的，而不是最后。
    """
    def __init__(self, size, dropout):
        super(SublayerConnection, self).__init__()
        self.norm = LayerNorm(size)
        self.dropout = nn.Dropout(dropout)

    def forward(self, x, sublayer):
        "Apply residual connection to any sublayer with the same size."
        "将残差连接应用于任何相同大小的子层。"
        print("调用 SublayerConnection 的 forward")
        return x + self.dropout(sublayer(self.norm(x)))


class Encoder(nn.Module):
    "encoder 核心是N层的"
    def __init__(self,layer, N):
        super(Encoder,self).__init__()
        self.layers = clones(layer,N)
        self.norm = LayerNorm(layer.size)
    def forward(self, x, mask):
        print("调用 Encoder 的 forward")
        for layer in self.layers:
            x = layer(x, mask)
        return self.norm(x)


def clones(module, N):
    # 将 model 复制 N 次
    return nn.ModuleList([copy.deepcopy(module) for _ in range(N)])

class MultiHeadedAttention(nn.Module):
    def __init__(self, h, d_model, dropout=0.1):
        """
        h 多头注意力的头数
        d_model 模型维度
        dropout 随机失活概率
        """
        super(MultiHeadedAttention, self).__init__()
        # 条件为真，正常执行
        assert d_model % h == 0
        # // 取整
        self.d_k = d_model // h
        # 
        self.h = h
        self.linears = clones(nn.Linear(d_model, d_model), 4)
        self.attn = None
        self.dropout = nn.Dropout(p=dropout)
    def forward(self, query, key, value, mask=None):
        print("调用 MultiHeadedAttention 的 forward")
        if mask is not None:
            # Same mask applied to all h heads.
            mask = mask.unsqueeze(1)
        nbatches = query.size(0)

        # 1) Do all the linear projections in batch from d_model => h x d_k
        query, key, value = [
            lin(x).view(nbatches, -1, self.h, self.d_k).transpose(1, 2)
            for lin, x in zip(self.linears, (query, key, value))
        ]

        # 2) Apply attention on all the projected vectors in batch.
        x, self.attn = attention(query, key, value, mask=mask, dropout=self.dropout)

        # 3) "Concat" using a view and apply a final linear.
        x = x.transpose(1, 2).contiguous().view(nbatches, -1, self.h * self.d_k)
        del query
        del key
        del value
        return self.linears[-1](x)

def attention(query, key, value, mask=None, dropout=None):
    "Compute 'Scaled Dot Product Attention'"
    print("计算 attention")
    d_k = query.size(-1)
    scores = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(d_k)
    if mask is not None:
        mask = mask.to(device=device)
        scores = scores.masked_fill(mask == 0, -1e9)
    p_attn = scores.softmax(dim=-1)
    if dropout is not None:
        p_attn = dropout(p_attn)
    return torch.matmul(p_attn, value), p_attn


class EncoderDecoder(nn.Module):
    """
    一个标准的encoder-decoder架构 适用于当前代码和其他模型
    """
    def __init__(self, encoder, decoder, src_embed, tgt_embed, generator):
        super(EncoderDecoder,self).__init__()
        self.encoder = encoder
        self.decoder = decoder
        self.src_embed = src_embed
        self.tgt_embed = tgt_embed
        self.generator = generator

    def forward(self, src, tgt, src_mask, tgt_mask):
        print("模型运行的时候-EncoderDecider中的 forward")
        return self.decode(self.encode(src,src_mask), src_mask, tgt, tgt_mask)
    
    def encode(self, src, src_mask):
        return self.encoder(self.src_embed(src), src_mask)
    
    def decode(self, memory, src_mask, tgt, tgt_mask):
        return self.decoder(self.tgt_embed(tgt), memory, src_mask, tgt_mask)
    
    

class PositionwiseFeedForward(nn.Module):
    "Implements FFN equation."

    def __init__(self, d_model, d_ff, dropout=0.1):
        super(PositionwiseFeedForward, self).__init__()
        self.w_1 = nn.Linear(d_model, d_ff)
        self.w_2 = nn.Linear(d_ff, d_model)
        self.dropout = nn.Dropout(dropout)

    def forward(self, x):
        print("调用 PositionwiseFeedForward 的 forward")
        return self.w_2(self.dropout(self.w_1(x).relu()))



class DecoderLayer(nn.Module):
    "Decoder is made of self-attn, src-attn, and feed forward (defined below)"

    def __init__(self, size, self_attn, src_attn, feed_forward, dropout):
        super(DecoderLayer, self).__init__()
        self.size = size
        self.self_attn = self_attn
        self.src_attn = src_attn
        self.feed_forward = feed_forward
        self.sublayer = clones(SublayerConnection(size, dropout), 3)

    def forward(self, x, memory, src_mask, tgt_mask):
        "Follow Figure 1 (right) for connections."
        print("调用 DecoderLayer 的 forward")
        m = memory
        x = self.sublayer[0](x, lambda x: self.self_attn(x, x, x, tgt_mask))
        x = self.sublayer[1](x, lambda x: self.src_attn(x, m, m, src_mask))
        return self.sublayer[2](x, self.feed_forward)


class Decoder(nn.Module):
    "Generic N layer decoder with masking."

    def __init__(self, layer, N):
        super(Decoder, self).__init__()
        self.layers = clones(layer, N)
        self.norm = LayerNorm(layer.size)

    def forward(self, x, memory, src_mask, tgt_mask):
        print("调用 Decoder 的 forward")
        for layer in self.layers:
            x = layer(x, memory, src_mask, tgt_mask)
        return self.norm(x)


class Generator(nn.Module):
    "Define standard linear + softmax generation step."

    def __init__(self, d_model, vocab):
        super(Generator, self).__init__()
        self.proj = nn.Linear(d_model, vocab)

    def forward(self, x):
        print("调用 Generator 的 forward")
        return log_softmax(self.proj(x), dim=-1)


def get_model(src_vocab,tgt_vocab,N=6,d_model=512,d_ff=2048,h=8,dropout=0.1):
    """
        构建transformer模型
        src_vocab: 源语言词典大小
        tgt_vocab: 目标语言词典大小
        N: 编码解码层数
        d_model: 模型维度
        d_ff: 前向传播层维度
        h: 多头注意力的头数
        dropout: 随机失活概率
    """
    # 多头注意力
    attn = MultiHeadedAttention(h, d_model, dropout)
    pff = PositionwiseFeedForward(d_model, d_ff, dropout)
    position_encoding = PositionalEncoding(d_model, dropout)
    
    model = EncoderDecoder(
        encoder = Encoder(EncoderLayer(d_model, copy.deepcopy(attn), copy.deepcopy(pff), dropout), N),
        decoder = Decoder(DecoderLayer(d_model, copy.deepcopy(attn), copy.deepcopy(attn), copy.deepcopy(pff), dropout), N),
        src_embed = nn.Sequential(Embeddings(d_model, src_vocab), copy.deepcopy(position_encoding)),
        tgt_embed = nn.Sequential(Embeddings(d_model, tgt_vocab), copy.deepcopy(position_encoding)),
        generator = Generator(d_model, tgt_vocab),
    )

    # 这个的意思是只初始化权重w 不初始化偏置b 偏置b的维度是1，所以不会初始化
    for p in model.parameters():
        if p.dim() > 1:
            nn.init.xavier_uniform_(p)
    return model
        

if __name__ == "__main__":
    model = get_model(src_vocab=10,tgt_vocab=5,N=2)
    print(model)