# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import os
import re

import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer


tf.random.set_seed(9999)


# %%
def get_chk_dir_path()->str:
    return os.path.abspath('../chk')    

def get_dat_dir_path()->str:
    return os.path.abspath('../dat')

def get_train_csv_path()->str:
    dat_dir = get_dat_dir_path()
    # print(dat_dir)
    return os.path.join(dat_dir, "train.csv")

def get_test_csv_path()->str:
    dat_dir = get_dat_dir_path()
    return os.path.join(dat_dir, "test_x.csv")

def get_sample_sub_path()->str:
    dat_dir = get_dat_dir_path()
    return os.path.join(dat_dir, "sample_submission.csv")


# %%
train = pd.read_csv(get_train_csv_path())
test = pd.read_csv(get_test_csv_path())
sample_submission = pd.read_csv(get_sample_sub_path())


# %%
# preprocesscing


# %%
def alpha_num(txt:str)->str:
    return re.sub(r"[^A-Za-z0-9 ]", "", txt)

train["text"] = train["text"].apply(alpha_num)


# %%
train


# %%
stopwords = [ "a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", "as", 
             "at", "be", "because", "been", "before", "being", "below", "between", "both", "but", "by", "could", 
             "did", "do", "does", "doing", "down", "during", "each", "few", "for", "from", "further", "had", "has", 
             "have", "having", "he", "he'd", "he'll", "he's", "her", "here", "here's", "hers", "herself", "him", "himself", 
             "his", "how", "how's", "i", "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is", "it", "it's", "its", "itself", 
             "let's", "me", "more", "most", "my", "myself", "nor", "of", "on", "once", "only", "or", "other", "ought", "our", "ours", 
             "ourselves", "out", "over", "own", "same", "she", "she'd", "she'll", "she's", "should", "so", "some", "such", "than", "that", 
             "that's", "the", "their", "theirs", "them", "themselves", "then", "there", "there's", "these", "they", "they'd", "they'll", 
             "they're", "they've", "this", "those", "through", "to", "too", "under", "until", "up", "very", "was", "we", "we'd", "we'll", 
             "we're", "we've", "were", "what", "what's", "when", "when's", "where", "where's", "which", "while", "who", "who's", "whom", 
             "why", "why's", "with", "would", "you", "you'd", "you'll", "you're", "you've", "your", "yours", "yourself", "yourselves" ]

def remove_stopwords(text:str) -> str:
    final_txt = []
    for i in text.split():
        if i.strip().lower() not in stopwords:
            final_txt.append(i.strip())
    return " ".join(final_txt)


# %%
train["text"] = train["text"].apply(alpha_num).apply(remove_stopwords)
test["text"] = test["text"].apply(alpha_num).apply(remove_stopwords)


# %%
train


# %%
# x_train = train["text"].values


# %%
# x_train


# %%
x_train = np.array([x for x in train["text"]])
x_test = np.array([x for x in test["text"]])
y_train = np.array([x for x in train["author"]])


# %%
# x_train


# %%
# Modeling


# %%
vocab_size = 20000
embedding_dim = 128
max_length = 500
padding_type = "post"


# %%
tokenizer = Tokenizer(num_words=vocab_size)
tokenizer.fit_on_texts(x_train)
word_index = tokenizer.word_index


# %%
list(word_index)[:10]


# %%
train_sequence = tokenizer.texts_to_sequences(x_train)
train_padded = pad_sequences(train_sequence, padding=padding_type, maxlen=max_length)

test_sequence = tokenizer.texts_to_sequences(x_test)
test_padded = pad_sequences(test_sequence, padding=padding_type, maxlen=max_length)


# %%
train_padded


# %%
############################################################################
## this model part is from 텐서플로2와 머신러닝으로 시작하는 자연어처리 04. 텍스트분류
############################################################################

model_name = "cnn_classifier_en"
BATCH_SIZE=512
NUM_EPOCHS=10
VALID_SPLIT=0.1
MAX_LEN=train_padded.shape[1]

kargs = {
    "model_name": model_name,
    "vocab_size": vocab_size,
    "embedding_size": 256,
    "num_filters": 100,
    "dropout_rate": .5,
    "hidden_dimension": 250,
    "output_dimension": 5
}


# %%
class CNNClassifier(tf.keras.Model):
    def __init__(self, **kargs):
        super(CNNClassifier, self).__init__(name=kargs["model_name"])
        self.embedding = tf.keras.layers.Embedding(input_dim=kargs["vocab_size"],
                                                   output_dim=kargs["embedding_size"])
        self.conv_list = [ tf.keras.layers.Conv1D(filters=kargs["num_filters"],
                                                  kernel_size=kernel_size,   
                                                  padding="valid", 
                                                  activation="relu", 
                                                  kernel_constraint=tf.keras.constraints.MaxNorm(max_value=3.))
                            for kernel_size in [3,4,5,6,7] ]
        self.pooling = tf.keras.layers.GlobalMaxPooling1D()
        self.dropout = tf.keras.layers.Dropout(kargs["dropout_rate"])
        self.fc1 = tf.keras.layers.Dense(units=kargs["hidden_dimension"], activation="relu", 
                                         kernel_constraint=tf.keras.constraints.MaxNorm(max_value=3.)
                                         )
        self.fc2 = tf.keras.layers.Dense(units=kargs["output_dimension"], activation="softmax",
                                         kernel_constraint=tf.keras.constraints.MaxNorm(max_value=3.)
                                         )


    def call(self, x):
        x = self.embedding(x)
        x = self.dropout(x)
        x = tf.concat([self.pooling(conv(x)) for conv in self.conv_list], axis=-1)
        x = self.fc1(x)
        x = self.dropout(x)
        x = self.fc2(x)

        return x                                         


# %%
model = CNNClassifier(**kargs)


# %%
model.compile(loss="sparse_categorical_crossentropy",
              optimizer="adam",
              metrics=["accuracy"])
model.build(train_padded.shape)
print(model.summary())            


# %%
#num_epochs = 20
earlystop_callback = tf.keras.callbacks.EarlyStopping(monitor="val_accuracy", 
                                                    min_delta=0.0001, 
                                                    patience=2)

checkpoint_path = os.path.join( get_chk_dir_path(), model_name, "weights.h5" )
checkpoint_dir = os.path.dirname(checkpoint_path)

cp_callback = tf.keras.callbacks.ModelCheckpoint(checkpoint_path, 
                                                monitor="val_accuracy", 
                                                verbose=1, 
                                                save_best_only=True, 
                                                save_weights_only=True)

if not os.path.exists(checkpoint_dir):
    os.makedirs(checkpoint_dir, exist_ok=True)

history = model.fit(train_padded, y_train, 
                    batch_size=BATCH_SIZE, 
                    epochs=NUM_EPOCHS, 
                    verbose=2, 
                    validation_split=VALID_SPLIT, 
                    callbacks=[earlystop_callback, cp_callback])


# %%
model.load_weights(checkpoint_path)

pred = model.predict(test_padded)


# %%
pred


# %%
pred.shape


# %%
test_padded.shape


# %%
sample_submission[[str(i) for i in range(5)]] = pred
sample_submission


# %%
sample_submission.to_csv("submission_cnn.csv", index=False, encoding="utf-8")


# %%



