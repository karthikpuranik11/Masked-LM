# Masked-LM

## BERT

Preferred running environment [Google Colab](https://colab.research.google.com/)

### Installation

Trained in Python 3.7.10

'''
!pip install transformers
'''

### Accessing the pre-trained model

1. Open the [Google Drive](https://drive.google.com/file/d/1HUP5MWisDXyJ7pJNu7mqTga4Eg3lk4vh/view?usp=sharing)
2. Download it or add a shortcut in your drive.

### Loading the pre-trained model

'''
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
'''

