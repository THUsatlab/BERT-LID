# BERT-LID: Leveraging BERT to Improve Spoken Language Identification

We propose a BERT-based language identification system (BERT-LID) to improve language identification performance, especially on short-duration speech segments. We extend the original BERT model by taking the phonetic posteriorgrams (PPG) derived from the front-end phone recognizer as input. Then we deployed the optimal deep classifier followed by it for language identification.

## Datasets
We use OLR20, TIMIT&THCHS-30, [TAL_ASR](https://ai.100tal.com/dataset) datasets for experiments. Among them, in order to test in segment audio, we perform segmentation processing on TIMIT&THCHS-30, where the window length is 1s and the window movement is 1s for segmentation. The specific usage of data is shown in data. The TAL_ASR data is forcibly aligned. 

## Feature extraction
The audio posterior probability feature is extracted as the input feature, and we use PHONEXIA BOTTLENECK FEATURE EXTRACTOR to extract. For more details, we can get more from "Multilingually trained bottleneck features in spoken language recognition".

## Experiments

### Load data
Load the data by adjusting the path parameters in AA. In the experiment, we divided the dataset into three datasets: train, test, and dev.

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
[1] Fer, Radek, et al. "Multilingually trained bottleneck features in spoken language recognition." Computer Speech & Language 46 (2017): 252-267.

[2] P. Schwarz, "Phoneme Recognition based on Long Temporal Context, PhD Thesis", Brno University of Technology, 2009

[3] TAL_ASR: https://ai.100tal.com/dataset

[4] Devlin, Jacob, et al. "Bert: Pre-training of deep bidirectional transformers for language understanding." arXiv preprint arXiv:1810.04805 (2018).

[5] https://github.com/codertimo/BERT-pytorch


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
