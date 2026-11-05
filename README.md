# deep-learning-course

Coursework notebooks for the Deep Learning course at CMC (ВМК) faculty, Moscow State University, Fall 2025. Author: Alex Ju. Notebooks run on Google Colab with PyTorch. Original assignments are in Russian.

## Assignments

| Folder | Topic | Methods | Key Results |
|--------|-------|---------|-------------|
| `hw1-dense-networks` | Fully connected networks, PyTorch (Homework 1.1) | Manual ReLU, Linear, Softmax + cross‑entropy with custom forward/backward (`derivatives.py`); MLP on `sklearn.datasets.load_digits` (8×8 digits). Experiments: depth (3/4/5 layers), weight initializations, activations. | Test accuracy ~92–97% (best 96.89%), train 100%. Some initializations diverge (loss explosion, accuracy ~10% or 0%). Box plots compare runs. |
| `hw2-segmentation` | Three‑class semantic segmentation (background / cat / dog) (Homework 2) | Dataset/DataLoader with disk speed measurement; PSPNet‑style decoder on frozen pretrained `ResNeXt50_32x4d` encoder (PyramidPoolingModule, Upsample, SegmentationHead). IoU, recall, Focal loss, cross‑entropy. Written answers on macro vs micro averaging and focal loss. | Run 1: mIoU 0.8985, recall 0.948. Run 2: mIoU 0.898, recall 0.942. 2 epochs. |
| `hw3-ner` | Named Entity Recognition (token tagging) (Homework 3) | Part 2: BiLSTM tagger. Part 3: Transformer tagger (HF tokenizer + offset mapping). Bonus 1: BiLSTM + attention. Bonus 2: ChatGPT (OpenAI API). TensorBoard logging. | BiLSTM: acc 0.921, macro‑F1 0.808 (target ≥0.76). Transformer (saved run): macro‑F1 0.021, acc 0.029 (did not work). BiLSTM+Attention: acc 0.904, macro‑F1 0.788. ChatGPT: acc 0.843, macro‑F1 0.10. |
| `hw4-audio` | Audio classification on ESC‑50 (50 classes) (Homework 4) | `torchaudio`/`librosa` mel‑spectrograms, SpecAugment (time warp/masking). Models: ClassifierCNN, ClassifierCNNExtended, ClassifierEncoder (Transformer over frames), Bonus AST from scratch, Bonus AST pretrained (code from YuanGongND/ast). | Train / Val / Test accuracy:<br>ClassifierCNN 0.997 / 0.387 / 0.428<br>ClassifierCNNExtended 1.000 / 0.433 / 0.436<br>ClassifierEncoder 1.000 / 0.607 / 0.654<br>AST (scratch) 0.941 / 0.580 / 0.546<br>AST pretrained 1.000 / 0.980 / 0.972 |

## How to run

- Open any `.ipynb` in **Google Colab** or **Jupyter**.
- **GPU runtime recommended** (Colab: Runtime → Change runtime type → GPU).
- Notebooks download datasets automatically; nothing is stored in the repo.
- For `hw3-ner` Bonus 2 (ChatGPT), set the environment variable `OPENAI_API_KEY` before running the relevant cells.

## Notes

- Notebooks keep their executed outputs.
- Original course texts are in Russian.
- OpenAI API key was removed from `hw3-ner`; provide it via `OPENAI_API_KEY`.
- Datasets are downloaded inside the notebooks and are not committed.

---

## 中文说明

CMC（ВМК）学院，莫斯科国立大学，2025 秋季深度学习课程作业笔记本。作者：Alex Ju。在 Google Colab 上使用 PyTorch 运行。原始作业为俄语。

### 作业一览

| 文件夹 | 主题 | 方法 | 关键结果 |
|--------|------|------|----------|
| `hw1-dense-networks` | 全连接网络，PyTorch (作业 1.1) | 手写 ReLU、Linear、Softmax+交叉熵及其前向/反向传播 (`derivatives.py`)；在 `sklearn.datasets.load_digits` (8×8 手写数字) 上训练 MLP。实验：层数 (3/4/5)、权重初始化、激活函数。 | 测试准确率约 92–97%（最佳 96.89%），训练集达 100%。部分初始化发散（Loss 爆炸，准确率降至 ~10% 或 0%）。箱线图对比多次运行。 |
| `hw2-segmentation` | 三类语义分割（背景/猫/狗） (作业 2) | Dataset/DataLoader 含磁盘读取速度测量；冻结预训练 `ResNeXt50_32x4d` 编码器的 PSPNet 式解码器（PyramidPoolingModule、Upsample、SegmentationHead）。IoU、Recall、Focal Loss、交叉熵。书面回答宏/微平均与 Focal Loss。 | 运行 1：mIoU 0.8985，Recall 0.948。运行 2：mIoU 0.898，Recall 0.942。共 2 个 epoch。 |
| `hw3-ner` | 命名实体识别（Token 级标注） (作业 3) | 第 2 部分：BiLSTM 标注器。第 3 部分：Transformer 标注器（HF tokenizer + offset mapping）。Bonus 1：BiLSTM+Attention。Bonus 2：ChatGPT (OpenAI API)。使用 TensorBoard 记录。 | BiLSTM：准确率 0.921，宏 F1 0.808（目标 ≥0.76）。Transformer（保存的运行）：宏 F1 0.021，准确率 0.029（未正常工作）。BiLSTM+Attention：准确率 0.904，宏 F1 0.788。ChatGPT：准确率 0.843，宏 F1 0.10。 |
| `hw4-audio` | ESC-50 环境声音分类 (50 类) (作业 4) | `torchaudio`/`librosa` 梅尔频谱图，SpecAugment 风格增强（时间扭曲/遮蔽）。模型：ClassifierCNN、ClassifierCNNExtended、ClassifierEncoder (Transformer over frames)、Bonus AST 从头训练、Bonus AST 预训练 (代码来自 YuanGongND/ast)。 | 训练/验证/测试准确率：<br>ClassifierCNN 0.997 / 0.387 / 0.428<br>ClassifierCNNExtended 1.000 / 0.433 / 0.436<br>ClassifierEncoder 1.000 / 0.607 / 0.654<br>AST (从头) 0.941 / 0.580 / 0.546<br>AST 预训练 1.000 / 0.980 / 0.972 |

### 运行方式

- 在 **Google Colab** 或 **Jupyter** 中打开任意 `.ipynb`。
- 建议启用 **GPU**（Colab：Runtime → Change runtime type → GPU）。
- 笔记本会自动下载数据集；仓库不存储数据。
- `hw3-ner` 的 Bonus 2 (ChatGPT) 需在运行相关单元格前设置环境变量 `OPENAI_API_KEY`。

### 备注

- 笔记本保留了执行输出。
- 原始课程文本为俄语。
- `hw3-ner` 中已移除 OpenAI API Key，需通过 `OPENAI_API_KEY` 环境变量提供。
- 数据集在笔记本内下载，不提交到仓库。
