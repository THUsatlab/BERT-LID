from pytorch_pretrained_bert import BertTokenizer
import numpy as np
import os


if __name__ == '__main__':

    tokenizer = BertTokenizer.from_pretrained('/home/nieyuting/bert/bert/bert_nyt/bert-base-cased/vocab.txt')
    mlf_path = './ad_test_all.mlf'
    label_path = 'AD_long_label21.csv'
    data_train_path = './ad_test/'
    data_test_path = './en_ch_1_2w/'

    en_ch_s_train_path = '/home/nieyuting/nieyt/work/lang-recognition/multilingual-bottleneck-features-master/feature/en_ch_s_train.txt'
    en_ch_1_2w_path = '/home/nieyuting/nieyt/work/lang-recognition/multilingual-bottleneck-features-master/feature/en_ch_1_2w.txt'

    with open(en_ch_s_train_path, 'r') as f:
        en_ch_1_train = f.readlines()
    with open(en_ch_1_2w_path, 'r') as f:
        en_ch_1_2w = f.readlines()
    
    #print(en_ch_1_train)



    label_dict={}

    with open(label_path, 'r') as f:
        label_lines = f.readlines()
    
    for label_line in label_lines[1:]:
        print('label_line:', label_line)
        label_line = label_line.split(',')
        label_dict[label_line[1]] = label_line[3].strip()
    
    print(label_dict)

    with open(mlf_path, 'r') as f:
        mlf_lines = f.readlines()
    
    ph_str = ''
    for mlf_line in mlf_lines:
        #print(len(mlf_line))
        if '*' in mlf_line:
            #file_name = label_dict[mlf_line[3:8]]
            
            mlf_line_split = mlf_line.split('/')
            mlf_line_split = mlf_line.split('.')
            aaa = mlf_line_split[0]
            file_name = aaa[3:]
            #print(aaa[3:])
            
            
            #print('file_name',file_name)
        elif len(mlf_line) > 20:
            mlf_line = mlf_line.split()
            ph = mlf_line[2]
            ph_str = ph_str + ph + ' '
            #print(ph_str)
        elif len(mlf_line) == 2:
            #print('file_name, ph_str:', file_name, ph_str)
            token = tokenizer.tokenize(ph_str)
            token_ids = tokenizer.convert_tokens_to_ids(token)
            ph_str = ''

            if len(token_ids) > 512:
                token_ids = token_ids[:512]
                #print(len(token_ids))
                #print('filne_name >512:', file_name)

            #print(token, token_ids)
            
            

            label = label_dict[file_name]
            npy_path = data_train_path + file_name + '_' + label + '.npy'
            #npy_path = data_train_path + file_name + '_0' + '.npy'
            print('npy_path:', npy_path)
            with open(npy_path, 'a') as f:
                f.write('')
            np.save(npy_path, token_ids)

#            flag = file_name + '\n'

#            if flag in en_ch_1_train:
#                npy_path = data_train_path + file_name + '.npy'
#                with open(npy_path, 'a') as f:
#                    f.write('')
                #np.save(npy_path, token_ids)
                #print('train data:', file_name)

#            if flag in en_ch_1_2w:
#                npy_path = data_test_path + file_name + '.npy'
#                with open(npy_path, 'a') as f:
#                    f.write('')
                #np.save(npy_path, token_ids)            
                #print('test data:', file_name)
           
            # data = np.load(npy_path)
            # print(data)
        

            
    
