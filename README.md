## Hate Speech Classifier

#### Overview

The **Hate Speech Classifier** utilizes **LSTM** networks to identify and categorize hate speech in text. It incorporates Jupyter Notebooks for data ingestion, validation, transformation, and model training.

#### Workflows

1. Modify `config.yaml`
2. Modify `params.yaml`
3. Modify entity
4. Update the configuration manager in `src/config`
5. Update the components
6. Update the pipeline
7. Update `main.py`
8. Update `app.py`

#### Steps

1. Data Ingestion
2. Data Validation
3. Data Transformation
4. Model Training
5. Build Flask App for Inference

#### LSTM Model

The model consists of:
- **Embedding Layer**: Converts text into dense vectors.
- **LSTM Layer**: Captures temporal dependencies.
- **Dense Layer**: Classifies the text.
- **Softmax Layer**: Provides classification probabilities.
