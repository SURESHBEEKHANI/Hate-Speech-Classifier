# Hate-Speech-Classifier

## Overview

The **Hate-Speech-Classifier** uses **LSTM** networks to detect and classify hate speech in text data. It includes Jupyter Notebooks for data ingestion, validation, transformation, and model training.



## Workflows

1. Update config.yaml
2. Update params.yaml
3. Update entity
4. Update the configuration manager in src config
5. update the conponents
6. update the pipeline
7. update the main.py
8. update the app.py


## step

1. data_ingestion
2. data_validation
3. data_transformation
4. model_trainer

## LSTM Model

The model includes:
- **Embedding Layer**: Converts text to dense vectors.
- **LSTM Layer**: Learns temporal dependencies.
- **Dense Layer**: Classifies the text.
- **Softmax Layer**: Outputs classification probabilities.
