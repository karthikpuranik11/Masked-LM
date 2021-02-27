# Masked-LM

## BERT

Preferred running environment [Google Colab](https://colab.research.google.com/)

### Installation

Trained in Python 3.7.10

```
!pip install transformers
! pip install nltk
```

### Accessing the pre-trained model

1. Open the [Google Drive](https://drive.google.com/file/d/1HUP5MWisDXyJ7pJNu7mqTga4Eg3lk4vh/view?usp=sharing)
2. Download it or add a shortcut in your drive.

### Loading the pre-trained model

Run the load_model_bert.py file by providing the appropriate path of [saved.bin](https://drive.google.com/file/d/1HUP5MWisDXyJ7pJNu7mqTga4Eg3lk4vh/view?usp=sharing) file.

### Predicting prepositions

Run the prediction_bert.py file.

To view the predictions:

```
preds = predict_masked_sent(sent, top_k=n)
print(preds)
```

where,
sent: the sentence for which you want to predict the prepositions.
n: number of predictions

Example:
```
preds = predict_masked_sent('The animals came to the meeting.', 5)
print(preds)
```

Output:
['The animals came to the meeting.', 'The animals came for the meeting.', 'The animals came into the meeting.', 'The animals came at the meeting.', 'The animals came from the meeting.']

Note:
1. The model doesn't neccessarily predict a preposition. To get a single prediction with a preposition, run pre_pred_bert.py.
2. In case of multiple prepositions, only the first one is masked and predicted.


