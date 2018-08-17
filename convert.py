
import csv
import os


def test():
    in_dir = 'C:\\Users\\blcdec\\project\\speech_style_convert\\tacotron_imu\\ImuSpeech-1.0'
    with open(os.path.join(in_dir, 'metadata.csv'), encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split(',')
            tar_path = os.path.join(in_dir, 'wavs', '%s.wav' % parts[0])

            in_path = os.path.join(in_dir, 'wavs', '%s.wav' % parts[1])
            print(in_path)



def write_csv(path_in,path_target):
    ''' 获取指定目录下的所有指定后缀的文件名 '''

    f_list_in = os.listdir(path_in)
    f_list_target =os.listdir(path_target)
    # print f_list
    list_in=[]
    list_target=[]
    for i in f_list_in:
        # os.path.splitext():分离文件名与扩展名
        if os.path.splitext(i)[1] == '.wav':
            list_in.append(os.path.splitext(i)[0])

    for i in f_list_target:
        # os.path.splitext():分离文件名与扩展名
        if os.path.splitext(i)[1] == '.wav':
            list_target.append(os.path.splitext(i)[0])
    print(list_in)

    print(list_target)
    metadata = open('C:\\Users\\blcdec\\project\\speech_style_convert\\tacotron_imu\\metadata.csv', 'w', newline='')
    w = csv.writer(metadata)
    for i in range(0,len(list_in)):
        w.writerow([list_target[i], list_in[i]])
    metadata.close()



if __name__ == '__main__':
    in_dir = 'C:\\Users\\blcdec\\project\\speech_style_convert\\tacotron_imu\\chinese_dubbing'
    tar_dir = 'C:\\Users\\blcdec\\project\\speech_style_convert\\tacotron_imu\\cinese_generage'
    # write_csv(in_dir, tar_dir)
    test()
