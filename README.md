# Masked-LM

## BERT

Preferred running environment [Google Colab](https://colab.research.google.com/).

Open a new notebook and change Edit->Notebook settings->Hardware accelerator->GPU.
Read [Getting started with Google Colab](https://towardsdatascience.com/getting-started-with-google-colab-f2fff97f594c) if required.


### Installation

Trained in Python 3.7.10

```
!pip install transformers
!pip install nltk
```

### Accessing the pre-trained model

1. Open the [Google Drive](https://drive.google.com/file/d/1HUP5MWisDXyJ7pJNu7mqTga4Eg3lk4vh/view?usp=sharing) link.
2. Download it or add a shortcut in your drive.

### Loading the pre-trained model

Copy the code in load_model_bert.py by providing the appropriate path of [saved.bin](https://drive.google.com/file/d/1HUP5MWisDXyJ7pJNu7mqTga4Eg3lk4vh/view?usp=sharing) file and run it.

### Predicting prepositions

Copy the code in prediction_bert.py file and run it.

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


## T5

### Installation

```
!pip install simpletransformers
!pip install nltk
```

### Accessing the pre-trained model

1. Open the [Google Drive](https://drive.google.com/file/d/1WTtGg5TdJR5NMGmV1ryLRdDnfiVbWw2b/view?usp=sharing) link.
2. Download it or add a shortcut in your drive.

### Loading the pre-trained model

Unzip the [new_word_output_500.zip](https://drive.google.com/file/d/1WTtGg5TdJR5NMGmV1ryLRdDnfiVbWw2b/view?usp=sharing) file by
```
!unzip /path/for/your/new_word_output_500.zip
```

Copy the code in load_model_t5.py file by providing the appropriate path of new_word_output_500 file into the notebook and run it.

### Predicting prepositions

Copy the code in prediction_t5.py and run it.

To view the predictions:

```
preds = predict_masked_sent(sent)
print(preds)
```

where,

sent: the sentence for which you want to predict the prepositions.

Example:
```
preds = predict_masked_sent('The animals came to the meeting.')
print(preds)
```

Output:
['The animals came from the meeting.', 'The animals came to the meeting.', 'The animals came from the meeting.', 'The animals came to the meeting.', 'The animals came to the meeting.']

Note:

1. The model doesn't neccessarily predict a preposition and multiple outputs can be similar.
2. In case of multiple prepositions, only the first one is masked and predicted.
3. In order to vary the number of output sentences, change "num_return_sequences": preferred number of outputs in the load_model_t5.py file.





