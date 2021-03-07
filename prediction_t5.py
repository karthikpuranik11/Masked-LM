import nltk
nltk.download('averaged_perceptron_tagger')
from nltk import pos_tag

def predict_masked_sent(text):
    text=text.split()
    tokens_tag = pos_tag(text)
    l=[]
    x=0
    for i in range(len(tokens_tag)):
      if x==0 and tokens_tag[i][1]=='IN' or tokens_tag[i][1]=='TO':
        l.append('X')
        x=1
      else:
        l.append(tokens_tag[i][0])
    text=' '.join(l)
    list1 = ["fill in the blank 1: " + text]
    preds=new_model.predict(list1)
    li=[]
    for j in range(len(preds[0])):
      text1=text
      text1=text1.split()
      for i in range(len(text1)):
        if text1[i]=='X':
          text1[i]=preds[0][j]
          break
      text1=' '.join(text1)
      li.append(text1)
    return li

