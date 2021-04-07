import transformers
import BertModel.src.config as config
import torch.nn as nn
#This file defines the bert model
class BERTBaseUncased(nn.Module):

    def __init__(self):
        super(BERTBaseUncased, self).__init__()
        self.bert = transformers.BertModel.from_pretrained(config.BERT_PATH)
        self.bert_drop = nn.Dropout(0.3)
        self.out = nn.Linear(768,1)

    def forward(self, ids, mask, token_type_ids):
        outputarr =self.bert(ids, 
                        attention_mask=mask,
                        token_type_ids= token_type_ids
                        )

        bo = self.bert_drop(outputarr[1])
        output= self.out(bo)
        return output
