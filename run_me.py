# coding=utf-8
from main import main

if __name__ == "__main__":

    model_name = "BertCNN"
    label_list = ['0', '1']
    #label_list = ['0', '1', '2', '3', '4', '5'] #'6', '7', '8', '9']
    data_dir = "./data"
    output_dir = "./me_output/" 
    cache_dir = "./me_cache/"
    log_dir = "./me_log/" 

    # bert-base
    bert_vocab_file = "bert-base-cased"
    bert_model_dir = "bert-base-cased"

    # # bert-large
    # bert_vocab_file = "/search/hadoop02/suanfa/songyingxin/pytorch_Bert/bert-large-uncased-vocab.txt"
    # bert_model_dir = "/search/hadoop02/suanfa/songyingxin/pytorch_Bert/bert-large-uncased"

    if model_name == "BertOrigin":
        from BertOrigin import args

    elif model_name == "BertCNN":
        from BertCNN import args

    elif model_name == 'BertLSTM':
        from BertLSTM import args

    elif model_name == "BertATT":
        from BertATT import args

    elif model_name == "BertRCNN":
        from BertRCNN import args

    elif model_name == "BertCNNPlus":
        from BertCNNPlus import args
    
    elif model_name == "BertDPCNN":
        from BertDPCNN import args

    config = args.get_args(data_dir, output_dir, cache_dir,
                           bert_vocab_file, bert_model_dir, log_dir)
    config.num_workers=6
    #config.gpu_ids=["6"]
    #config.num_train_epochs=250
    #config.print_step=5
    config.do_train="True"
    main(config, config.save_name, label_list)
        

