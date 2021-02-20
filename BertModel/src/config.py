import transformers

MAX_LEN = 512
TRAIN_BATCH_SIZE = 2
VALID_BATCH_SIZE = 1
EPOCHS = 1
BERT_PATH= '../input/bert_base_uncased/'
MODEL_PATH = 'model.bin'
TRAINING_FILE = '../input/stock_data.csv'
TOKENIZER = transformers.BertTokenizer.from_pretrained(BERT_PATH, do_lower_case=True)
RANDOM_SEED=42