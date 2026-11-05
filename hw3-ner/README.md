# HW3 · Named Entity Recognition

Token-level NER taggers: BiLSTM, Transformer-based (HF tokenizer with offset mapping), BiLSTM + attention (bonus) and a ChatGPT-based tagger via the OpenAI API (bonus).

Results (test, from notebook outputs): BiLSTM acc 0.921 / macro-F1 0.808; Transformer tagger macro-F1 0.021 in the saved run (did not work correctly); BiLSTM+Attention acc 0.904 / macro-F1 0.788; ChatGPT acc 0.843 / macro-F1 0.10.

The OpenAI API key was removed — set `OPENAI_API_KEY` to run the ChatGPT part.

作业 3：命名实体识别。BiLSTM 宏 F1 0.808；Transformer 部分保存的结果未跑通；BiLSTM+Attention 宏 F1 0.788；ChatGPT 宏 F1 0.10。运行 ChatGPT 部分需设置环境变量 OPENAI_API_KEY。
