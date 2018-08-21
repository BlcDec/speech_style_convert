from concurrent.futures import ProcessPoolExecutor
from functools import partial
import numpy as np
import os
from util import audio


def build_from_path(in_dir, out_dir, num_workers=1):
    data = np.load(os.path.join(out_dir ,'Imuspeech-in_spec-00001.npy'))
    np.set_printoptions(threshold=np.inf)
    print(data)
    print(data.shape)

if __name__ == '__main__':
    in_dir='C:\\Users\\blcdec\\project\\speech_style_convert\\tacotron_imu\\ImuSpeech-1.0'
    out_dir = 'C:\\Users\\blcdec\\project\\speech_style_convert\\tacotron_imu\\ImuSpeech-1.0\\training'
    build_from_path(in_dir,out_dir)


# 请对系统做以下修改：
# 1. 使用新数据
# 2. 输入特征改为mel谱
# 3. 对应修改模型，增加一个输入

      #prenet_outputs = prenet(inputs, is_training, hp.prenet_depths)    # [N, T_in, prenet_depths[-1]=128]
      encoder_outputs = encoder_cbhg(inputs, input_lengths, is_training, # [N, T_in, encoder_depth=256]
                                     hp.encoder_depth)

      # Attention
      attention_cell = AttentionWrapper(
        DecoderPrenetWrapper(GRUCell(hp.attention_depth), is_training, hp.prenet_depths),
        BahdanauAttention(hp.attention_depth, encoder_outputs),
        alignment_history=True,
        output_attention=False)                                                  # [N, T_in, attention_depth=256]

      # Concatenate attention context vector and RNN cell output into a 2*attention_depth=512D vector.
      concat_cell = ConcatOutputAndAttentionWrapper(attention_cell)              # [N, T_in, 2*attention_depth=512]
# 以上复制一份，对应修改为日语特征输入，记新的	concat_cell为concat_cell_jp，新增一行连接两个输出

encoder_out = tf.concat([concat_cell, concat_cell_jp], axis=-1)

# 对应修改解码器

      decoder_cell = MultiRNNCell([
          OutputProjectionWrapper(encoder_out, hp.decoder_depth),
          ResidualWrapper(GRUCell(hp.decoder_depth)),
          ResidualWrapper(GRUCell(hp.decoder_depth))
        ], state_is_tuple=True)