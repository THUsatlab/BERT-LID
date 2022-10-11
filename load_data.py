
import numpy as np
import torch
import pdb
import os
from torch.utils.data import Dataset, DataLoader
from random import shuffle
import re

DIRS = {"train": "./train",
        "test": "./test",
        "dev": "./dev"}
LABELDICT = {"ct-cn": 0, "id-id": 1, "ja-jp": 2,
             "ko-kr": 3, "ru-ru": 4, "vi-vn": 5}

__all__ = ['AD_DataLoader']


class AD_Dataset(Dataset):
    def __init__(self, args, mode='train'):

        def containenglish(str0):
            return bool(re.search('[A-Z]', str0))

        self.mode = mode
        self.audio = [np.load(os.path.join(DIRS[mode], filename))
                      for filename in os.listdir(DIRS[mode])]
        # self.label = [LABELDICT[filename.split("_")[0]] for filename in os.listdir(DIRS[mode])]
        # self.label = [LABELDICT[filename[-9:-4]]
        #               for filename in os.listdir(DIRS[mode])]

        self.label = []
        for filename in os.listdir(DIRS[mode]):
            if containenglish(filename[:1]):
                self.label.append(0)
            else:
                self.label.append(1)
        self.label = np.array(self.label)

        zippacket = list(zip(self.audio, self.label))
        shuffle(zippacket)
        self.audio, self.label = zip(*zippacket)

    def get_len(self):
        return len(self.audio)

    def __len__(self):
        assert len(self.audio) == len(self.label)
        return len(self.audio)

    def __getitem__(self, index):

        return torch.from_numpy(self.audio[index]).float(), self.label[index]


def AD_DataLoader(args):

    datasets = {
        'train': AD_Dataset(args, mode='train'),
        'valid': AD_Dataset(args, mode='dev'),
        'test': AD_Dataset(args,  mode='test')
    }
    bs = {"train": args.train_batch_size,
          "valid": args.dev_batch_size, "test": args.test_batch_size}
    # dataloader is an iterator for train, valid, test data
    dataLoader = {
        ds: DataLoader(datasets[ds],
                       batch_size=bs[ds],
                       num_workers=args.num_workers,
                       shuffle=True,
                       collate_fn=collate_fn)
        for ds in datasets.keys()
    }
    example_lens = {
        "train": AD_Dataset(args, mode="train").get_len(),
        "valid": AD_Dataset(args, mode="dev").get_len(),
        "test": AD_Dataset(args, mode="test").get_len()
    }
    recordfile = open("./nyt-result.txt", "a")
    recordfile.write(str(DIRS))
    recordfile.close()
    return dataLoader, example_lens


def collate_fn(samples):
    wavs, labels = [], []
    for wav, label in samples:
        wavs.append(wav)
        labels.append(label)
    return wavs, labels
