import nltk
from transformers import BertTokenizer
#nltk.download('all') 
#uncomment if required
from nltk import pos_tag 

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
def predict_masked_sent(text, top_k=5):
    # Tokenize input
    text2=text
    text=text.split()
    tokens_tag = pos_tag(text)
    l=[]
    x=0
    for i in range(len(tokens_tag)):
      if x==0 and tokens_tag[i][1]=='IN' or tokens_tag[i][1]=='TO':
        l.append('[MASK]')
        x=1
      else:
        l.append(tokens_tag[i][0])
    text=' '.join(l)
    if x==1:
      text = "[CLS] %s [SEP]"%text
      tokenized_text = tokenizer.tokenize(text)
      labels = tokenizer(text , return_tensors="pt")["input_ids"]
      masked_index = tokenized_text.index("[MASK]")
      indexed_tokens = tokenizer.convert_tokens_to_ids(tokenized_text)
      tokens_tensor = torch.tensor([indexed_tokens])
      # tokens_tensor = tokens_tensor.to('cuda')    # if you have gpu

      # Predict all tokens
      with torch.no_grad():
          outputs = model(tokens_tensor)
          predictions = outputs[0]

      probs = torch.nn.functional.softmax(predictions[0, masked_index], dim=-1)
      top_k_weights, top_k_indices = torch.topk(probs, top_k, sorted=True)

      li=[]
      for i, pred_idx in enumerate(top_k_indices):
          predicted_token = tokenizer.convert_ids_to_tokens([pred_idx])[0]
          token_weight = top_k_weights[i]
          text1=text
          text1=text1.split()
          text1=text1[1:-1]
          for i in range(len(text1)):
            if text1[i]=='[MASK]':
              text1[i]=predicted_token
              break
          text1=' '.join(text1)
          li.append(text1)
      return li
    else:
      return [text2]
