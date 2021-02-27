from transformers import BertForMaskedLM
import torch
import torch.nn as nn

class BertPred(nn.Module):
    def __init__(self):
        super().__init__()
        self.bert = BertForMaskedLM.from_pretrained('bert-base-uncased')

    def forward(self, input_ids, attention_mask=None, token_type_ids=None,
            position_ids=None, head_mask=None, labels=None):
        return self.bert(input_ids=input_ids,labels=labels)

model = BertPred()
model.load_state_dict(torch.load('/path/for/your/saved.bin'))
model.eval()