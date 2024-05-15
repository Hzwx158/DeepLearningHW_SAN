import os
import glob
from tqdm import tqdm


#一个简单的脚本，用于处理一组文本文件中的单词，并将这些单词写入到一个单独的文件中，同时统计不同单词的数量

#找到 label_path 文件夹中所有扩展名为 .txt 的文件，并将它们的路径存储在列表 labels 中

#TODO: 修改这个路径
label_path = 'test-bak'

labels = glob.glob(os.path.join(label_path, '*.txt'))

#
words_dict = set(['<eos>', '<sos>', 'struct'])

with open('word.txt', 'w') as writer:
    #我们先写三个单词进去
    writer.write('<eos>\n<sos>\nstruct\n')
    i = 3
    for item in tqdm(labels):
        #把文件列表里的文件写进去
        with open(item) as f:
            lines = f.readlines()
        for line in lines:
            #文件读出来的那一行应该有这个格式， 
            #我们只关心前四项，且我们只记录c
            cid, c, pid, p, *r = line.strip().split()
            if c not in words_dict:
                #如果没有出现过，则更新字符集
                words_dict.add(c)
                writer.write(f'{c}\n')
                i+=1
    #最后再补一点东西
    #TODO：这些东西为啥不在word_dict 里面？
    writer.write('above\nbelow\nsub\nsup\nl_sup\ninside\nright')
print(i)


