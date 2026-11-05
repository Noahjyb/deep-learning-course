# HW2 · Three-Class Semantic Segmentation

Background / cat / dog segmentation with a PSPNet-like model on a frozen pretrained ResNeXt50_32x4d encoder (PyramidPoolingModule, Upsample, SegmentationHead), custom IoU / recall metrics and Focal / cross-entropy losses.

Results (from notebook outputs, 2 epochs): mean IoU 0.8985 / mean recall 0.948 (run 1); mean IoU 0.898 / recall 0.942 (run 2).

作业 2：背景/猫/狗三类语义分割，PSPNet 式网络 + 冻结的 ResNeXt50 编码器。mIoU 约 0.898。
