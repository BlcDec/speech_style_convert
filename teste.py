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