a=predict_masked_sent('The animals came to the meeting.', top_k=5)
for j in range(len(a)):
  x=0
  a[j]=a[j].split()
  #print(a[j])
  tok = pos_tag(a[j])
  for k in range(len(tok)):
    if tok[k][1]=='IN' or tok[k][0]=='to':
      pred=' '.join(a[j])
      print(pred)
      break
  break
    
    