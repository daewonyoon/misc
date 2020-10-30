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
embedding_dim = 256
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
model_name = "rnn_bidi_classifier_en"
BATCH_SIZE=128
NUM_EPOCHS=10
VALID_SPLIT=0.1


# %%
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(vocab_size, embedding_dim, input_length=max_length),
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(64)),
    #tf.keras.layers.Dropout(rate=.2),
    tf.keras.layers.Dense(256, activation="relu"),
    tf.keras.layers.Dropout(rate=.5),
    tf.keras.layers.Dense(5, activation="softmax")
])


# %%
model.compile(loss="sparse_categorical_crossentropy",
              optimizer="adam",
              metrics=["accuracy"])
print(model.summary())            


# %%
#num_epochs = 20
#history = model.fit(train_padded, y_train, epochs=num_epochs, verbose=2, validation_split=.2)

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
sample_submission.to_csv("submission_rnn_bidi.csv", index=False, encoding="utf-8")


# %%



