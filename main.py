# coding=utf-8
import random
import numpy as np
import time
from tqdm import tqdm
import os

import torch
import torch.nn as nn


from pytorch_pretrained_bert.tokenization import BertTokenizer
from pytorch_pretrained_bert.modeling import BertConfig, WEIGHTS_NAME, CONFIG_NAME
from pytorch_pretrained_bert.optimization import BertAdam

from Utils.utils import get_device
from Utils.load_datatsets import load_data
from load_data import AD_DataLoader
from train_evalute import train, evaluate, evaluate_save
from pdb import set_trace


def main(config, model_times, label_list):

    if not os.path.exists(config.output_dir + model_times):
        os.makedirs(config.output_dir + model_times)

    if not os.path.exists(config.cache_dir + model_times):
        os.makedirs(config.cache_dir + model_times)

    output_model_file = os.path.join(
        config.output_dir, model_times, WEIGHTS_NAME)
    output_config_file = os.path.join(
        config.output_dir, model_times, CONFIG_NAME)

    gpu_ids = [int(device_id) for device_id in config.gpu_ids]
    device, n_gpu = get_device(gpu_ids[0])
    if n_gpu > 1:
        n_gpu = len(gpu_ids)

    config.train_batch_size = config.train_batch_size // config.gradient_accumulation_steps

    random.seed(config.seed)
    np.random.seed(config.seed)
    torch.manual_seed(config.seed)

    if n_gpu > 0:
        torch.cuda.manual_seed_all(config.seed)

    # tokenizer = BertTokenizer.from_pretrained(
    #    config.bert_vocab_file, do_lower_case=config.do_lower_case)  # 分词器选择

    num_labels = len(label_list)
    print(num_labels)
    data_loader, example_lens = AD_DataLoader(config)
    # Train and dev
    if config.do_train:
        # train_dataloader, train_examples_len = load_data(
        #    config.data_dir, tokenizer, config.max_seq_length, config.train_batch_size, "train", label_list)
        # dev_dataloader, _ = load_data(
        #    config.data_dir, tokenizer, config.max_seq_length, config.dev_batch_size, "dev", label_list)
        train_dataloader = data_loader["train"]
        train_examples_len = example_lens["train"]
        dev_dataloader = data_loader["valid"]
        num_train_optimization_steps = int(
            train_examples_len / config.train_batch_size / config.gradient_accumulation_steps) * config.num_train_epochs

        print("model name is {}".format(config.model_name))
        if config.model_name == "BertOrigin":
            from BertOrigin.BertOrigin import BertOrigin
            model = BertOrigin.from_pretrained(
                config.bert_model_dir, cache_dir=config.cache_dir, num_labels=num_labels)
        elif config.model_name == "BertCNN":
            from BertCNN.BertCNN import BertCNN
            filter_sizes = [int(val) for val in config.filter_sizes.split()]
            print('bert_model_dir, cache_dir, num_labels,n_filters, filter_sizes:', config.bert_model_dir,
                  config.cache_dir, num_labels, config.filter_num, filter_sizes)
            model = BertCNN.from_pretrained(
                config.bert_model_dir, cache_dir=config.cache_dir, num_labels=num_labels,
                n_filters=config.filter_num, filter_sizes=filter_sizes)
        elif config.model_name == 'BertLSTM':
            from BertLSTM.BertLSTM import BertLSTM
            print('bert_model_dir, cache_dir, num_labels, rnn_hidden_size, num_layers, bidirectional, dropout', config.bert_model_dir,
                  config.cache_dir, num_labels, config.hidden_size, config.num_layers, config.bidirectional, config.dropout)
            model = BertLSTM.from_pretrained(config.bert_model_dir, cache_dir=config.cache_dir, num_labels=num_labels,
                                             rnn_hidden_size=config.hidden_size, num_layers=config.num_layers, bidirectional=config.bidirectional, dropout=config.dropout)
        elif config.model_name == "BertATT":
            from BertATT.BertATT import BertATT
            model = BertATT.from_pretrained(
                config.bert_model_dir, cache_dir=config.cache_dir, num_labels=num_labels)

        elif config.model_name == "BertRCNN":
            from BertRCNN.BertRCNN import BertRCNN
            print('rnn_hidden_size,num_layers, bidirectional,dropout',
                  config.hidden_size, config.num_layers, config.bidirectional, config.dropout)
            model = BertRCNN.from_pretrained(
                config.bert_model_dir, cache_dir=config.cache_dir, num_labels=num_labels, rnn_hidden_size=config.hidden_size, num_layers=config.num_layers, bidirectional=config.bidirectional, dropout=config.dropout)

        elif config.model_name == "BertCNNPlus":
            from BertCNNPlus.BertCNNPlus import BertCNNPlus
            filter_sizes = [int(val) for val in config.filter_sizes.split()]
            model = BertCNNPlus.from_pretrained(
                config.bert_model_dir, cache_dir=config.cache_dir, num_labels=num_labels,
                n_filters=config.filter_num, filter_sizes=filter_sizes)
        elif config.model_name == "BertDPCNN":
            from BertDPCNN.BertDPCNN import BertDPCNN
            print('filter_num', config.filter_num)
            model = BertDPCNN.from_pretrained(
                config.bert_model_dir, cache_dir=config.cache_dir, num_labels=num_labels, filter_num=config.filter_num)

        model.to(device)

        if n_gpu > 1:
            model = torch.nn.DataParallel(model, device_ids=gpu_ids)

        param_optimizer = list(model.named_parameters())
        no_decay = ['bias', 'LayerNorm.bias', 'LayerNorm.weight']
        optimizer_grouped_parameters = [
            {'params': [p for n, p in param_optimizer if not any(
                nd in n for nd in no_decay)], 'weight_decay': 0.01},
            {'params': [p for n, p in param_optimizer if any(
                nd in n for nd in no_decay)], 'weight_decay': 0.0}
        ]

        optimizer = BertAdam(optimizer_grouped_parameters,
                             lr=config.learning_rate,
                             warmup=config.warmup_proportion,
                             t_total=num_train_optimization_steps)

        criterion = nn.CrossEntropyLoss()
        criterion = criterion.to(device)

        if hasattr(torch.cuda, 'empty_cache'):
            torch.cuda.empty_cache()
        train(config.num_train_epochs, n_gpu, model, train_dataloader, dev_dataloader, optimizer,
              criterion, config.gradient_accumulation_steps, device, label_list, output_model_file, output_config_file, config.log_dir, config.print_step, config.early_stop)

    """ Test """

    # test 数据
    #test_dataloader, _ = load_data(config.data_dir, tokenizer, config.max_seq_length, config.test_batch_size, "test", label_list)
    test_dataloader = data_loader["test"]
    # 加载模型
    bert_config = BertConfig(output_config_file)

    if config.model_name == "BertOrigin":
        from BertOrigin.BertOrigin import BertOrigin
        model = BertOrigin(bert_config, num_labels=num_labels)
    elif config.model_name == "BertCNN":
        from BertCNN.BertCNN import BertCNN
        filter_sizes = [int(val) for val in config.filter_sizes.split()]
        model = BertCNN(bert_config, num_labels=num_labels,
                        n_filters=config.filter_num, filter_sizes=filter_sizes)
    elif config.model_name == 'BertLSTM':
        from BertLSTM.BertLSTM import BertLSTM
        model = BertLSTM(bert_config, num_labels, config.hidden_size,
                         config.num_layers, config.bidirectional, config.dropout)
    elif config.model_name == "BertATT":
        from BertATT.BertATT import BertATT
        model = BertATT(bert_config, num_labels=num_labels)
    elif config.model_name == "BertRCNN":
        from BertRCNN.BertRCNN import BertRCNN
        model = BertRCNN(bert_config, num_labels, config.hidden_size,
                         config.num_layers, config.bidirectional, config.dropout)
    elif config.model_name == "BertCNNPlus":
        from BertCNNPlus.BertCNNPlus import BertCNNPlus
        filter_sizes = [int(val) for val in config.filter_sizes.split()]
        model = BertCNNPlus(bert_config, num_labels=num_labels,
                            n_filters=config.filter_num, filter_sizes=filter_sizes)
    elif config.model_name == "BertDPCNN":
        from BertDPCNN.BertDPCNN import BertDPCNN
        model = BertDPCNN(bert_config, num_labels=num_labels,
                          filter_num=config.filter_num)

    model.load_state_dict(torch.load(output_model_file))
    model.to(device)

    # 损失函数准备
    criterion = nn.CrossEntropyLoss()
    criterion = criterion.to(device)

    # test the model
    test_loss, test_acc, test_report, test_auc, all_labels, all_preds = evaluate_save(
        model, test_dataloader, criterion, device, label_list)
    recordfile = open("./nyt-result.txt", "a")
    print("-------------- Test -------------")
    recordfile.write("\n{}\n".format(config.model_name))
    print(
        f'\t  Loss: {test_loss: .3f} | Acc: {test_acc*100: .3f} % | AUC:{test_auc}')
    recordfile.write(
        f"\t Loss: {test_loss: .3f} | Acc: {test_acc*100: .3f} % | AUC:{test_auc}")
    for label in label_list:
        print('\t {}: Precision: {} | recall: {} | f1 score: {}'.format(
            label, test_report[label]['precision'], test_report[label]['recall'], test_report[label]['f1-score']))
        recordfile.write('\n\t {}: Precision: {} | recall: {} | f1 score: {}'.format(
            label, test_report[label]['precision'], test_report[label]['recall'], test_report[label]['f1-score']))
    print_list = ['macro avg', 'weighted avg']

    for label in print_list:
        print('\t {}: Precision: {} | recall: {} | f1 score: {}'.format(
            label, test_report[label]['precision'], test_report[label]['recall'], test_report[label]['f1-score']))
        recordfile.write('\n\t {}: Precision: {} | recall: {} | f1 score: {}'.format(
            label, test_report[label]['precision'], test_report[label]['recall'], test_report[label]['f1-score']))
    recordfile.close()
