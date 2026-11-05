# HW4 · Audio Classification (ESC-50)

Environmental sound classification (50 classes) from mel-spectrograms with augmentation (time warp / masking). Models: CNN, extended CNN, Transformer encoder, Audio Spectrogram Transformer (AST, code by the paper authors, YuanGongND/ast) from scratch and pretrained.

| Model | Train | Val | Test |
|---|---|---|---|
| ClassifierCNN | 0.997 | 0.387 | 0.428 |
| ClassifierCNNExtended | 1.000 | 0.433 | 0.436 |
| ClassifierEncoder | 1.000 | 0.607 | 0.654 |
| AST (scratch) | 0.941 | 0.580 | 0.546 |
| AST (pretrained) | 1.000 | 0.980 | 0.972 |

作业 4：ESC-50 环境声音分类。预训练 AST 测试准确率 0.972。
