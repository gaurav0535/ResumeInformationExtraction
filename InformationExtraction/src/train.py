#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 00:19:23 2020
@author: Gaurav Srivastava
"""


from config import TRAIN_DATA, MODEL_OUTPUT
import spacy, pickle, random

nlp = spacy.load('en_core_web_sm')

train_data = pickle.load(open(TRAIN_DATA, 'rb'))

nlp = spacy.blank('en')


def train_model(train_data, iterations):
    if 'ner' not in nlp.pipe_names:
        ner = nlp.create_pipe('ner')
        nlp.add_pipe(ner, last=True)

    for _, annotation in train_data:
        for ent in annotation['entities']:
            ner.add_label(ent[2])

    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']
    with nlp.disable_pipes(*other_pipes):  # only train NER
        optimizer = nlp.begin_training()
        for itn in range(iterations):
            print("Starting iteration " + str(itn))
            random.shuffle(train_data)
            losses = {}
            index = 0
            for text, annotations in train_data:
                try:
                    nlp.update(
                        [text],  # batch of texts
                        [annotations],  # batch of annotations
                        drop=0.2,  # dropout - make it harder to memorise data
                        sgd=optimizer,  # callable to update weights
                        losses=losses)
                except Exception as e:
                    pass

            print(losses)


if __name__ == '__main__':
    train_model(train_data, 16)
    nlp.to_disk(MODEL_OUTPUT + '/nlp_model')
    nlp_model = spacy.load(MODEL_OUTPUT + '/nlp_model')
    doc = nlp_model(train_data[1][0])
    for ent in doc.ents:
        print(f'{ent.label_.upper():{30}}- {ent.text}')
