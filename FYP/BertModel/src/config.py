import transformers
#This file contains global variables for the bert model
MAX_LEN = 512
TRAIN_BATCH_SIZE = 2
VALID_BATCH_SIZE = 1
EPOCHS = 10
BERT_PATH= 'C:/Users/Andrew/Desktop/FinalYearProject/FYP/BertModel/input/bert_based_uncased/'
MODEL_PATH = 'model.bin'
TRAINING_FILE = '../FYP/BertModel/input/stock_data.csv'
TOKENIZER = transformers.BertTokenizer.from_pretrained(BERT_PATH, do_lower_case=True)
RANDOM_SEED=42
