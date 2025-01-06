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


## Notebooks

1. **`01_data_ingestion.ipynb`**: Ingest and preprocess raw data.
2. **`02_data_validation.ipynb`**: Validate data quality.
3. **`03_data_transformation.ipynb`**: Tokenize, pad sequences, and split data.
4. **`04_model_trainer.ipynb`**: Train and save the LSTM model.

## LSTM Model

The model includes:
- **Embedding Layer**: Converts text to dense vectors.
- **LSTM Layer**: Learns temporal dependencies.
- **Dense Layer**: Classifies the text.
- **Softmax Layer**: Outputs classification probabilities.
