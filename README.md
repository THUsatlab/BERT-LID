# BERT-LID: Leveraging BERT to Improve Spoken Language Identification

We propose a BERT-based language identification system (BERT-LID) to improve language identification performance, especially on short-duration speech segments. We extend the original BERT model by taking the phonetic posteriorgrams (PPG) derived from the front-end phone recognizer as input. Then we deployed the optimal deep classifier followed by it for language identification.

## Datasets
We use OLR20, TIMIT&THCHS-30, [TAL_ASR](https://ai.100tal.com/dataset) datasets for experiments. Among them, in order to test in segment audio, we perform segmentation processing on TIMIT&THCHS-30, where the window length is 1s and the window movement is 1s for segmentation. The specific usage of data is shown in data. The TAL_ASR data is forcibly aligned. 

## Feature extraction
We directly obtains the phoneme features of the audio through [Phoneme recognizer based on long temporal context](https://speech.fit.vutbr.cz/software/phoneme-recognizer-based-long-temporal-context), and then obtains tokens through the BertTokenizer model provided by BERT. We take this feature as input. For the specific processing of data, see the 'get_data.py'.

## Experiments

### Load data
Load the data by adjusting the path parameters in 'load_data.py'. In the experiment, we divided the dataset into three datasets: train, test, and dev.

### Models
Our model is saved in BertCNN, BertRCNN, BertDPCNN, BertLSTM, and pay attention to whether bert in the model-related file is turned on during use. 

### Program
Run the program using the following command:

```
python run_me.py
```
Important parameters are as follows:

* model_name: Select the input model

* label_list：Given label list

* bert_voacb_file：Input the bert model

Or you can use the following command to run multiple times and adjust the super parameters at the same time:

```
bash run_me.sh
```

## References
[1] P. Schwarz, "Phoneme Recognition based on Long Temporal Context, PhD Thesis", Brno University of Technology, 2009

[2] TAL_ASR: https://ai.100tal.com/dataset

[2] Devlin, Jacob, et al. "Bert: Pre-training of deep bidirectional transformers for language understanding." arXiv preprint arXiv:1810.04805 (2018).

[4] https://github.com/codertimo/BERT-pytorch

[5] Schwarz, Petr, et al. "Phoneme recognizer based on long temporal context." Speech Processing Group, Faculty of Information Technology, Brno University of Technology.[Online]. Available: http://speech. fit. vutbr. cz/en/software (2006).

## Citation

Please cite our paper if you find this work useful:

```bibtex
@InProceedings{NieYT2022_ISCSLP,
  author    = {Yuting Nie and Junhong Zhao and Wei-Qiang Zhang and Jinfeng Bai},
  booktitle = {International Symposium on Chinese Spoken Language Processing (ISCSLP)},
  title     = {BERT-LID: Leveraging BERT to improve spoken language identification},
  address   = {Singapore},
  month     = {12},
  year      = {2022},
  url       = {https://arxiv.org/abs/2203.00328},
}
```
