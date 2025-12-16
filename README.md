# SemEval 2026 Task 9: Detecting Multilingual, Multicultural, and Multievent Online Polarization

This repository contains the notebooks and code for **SemEval 2026 Task 9**, focusing on detecting polarized text across multiple languages and contexts.

## Repository Structure
 – Contains Jupyter notebooks for each subtask.
- `dev_phase` in the same folder here to run the notebooks.


## Getting Started
To run the notebooks:

1. Ensure the `dev_phase` folder is located in the same directory as the notebooks.
2. Update the `workdir` variables in each notebook to point to your working directory(SemEval).

## Subtasks
- **Subtask 1:** Binary polarization detection (English, Swahili, Hausa)  
- **Subtask 2:** Multilingual polarization classification (English + Swahili)  
- **Subtask 3:** Multilingual manifestation identification (English + Swahili)  

Each notebook is self-contained and provides detailed steps for preprocessing, model training, and evaluation.

For the with weight and without weight approach one must change the vakue of the argument of the function train in notebook 2 and 3.

## Models
- The final models are based on transformer architectures, including **XLM-RoBERTa** and **RoBERTa-based sentiment models**.  
- Class imbalance is handled via **Focal Loss** and weighted training where applicable.  
- A FastText static embedding approach is also provided as a baseline.

## Test Run
Running the notebooks end-to-end will:
1. Preprocess the dataset.
2. Train models for each subtask.
3.One Fastext model if one have hugging face account models can be saved, then can be uploaded to **Hugging Face** for deployment.

# AIMS ML SemEval Polarization Projectv USAGE ON SUBTASK 1

## Installation

Clone the repository and install requirements:

```bash
git clone https://github.com/efandresena/SemEval.git
cd SemEval
pip install -r requirements.txt
```

## Model Names Subtask 1 
- mirindraf/aims-sentiment-analysis  %This is for english only
- mirindraf/aims-sentiment-analysis-hau
- mirindraf/bert-base-uncased-polarization
## Model Names Subtask 2
Under development
## Model Names Subtask 3
Under development

## Usage
It is preferable to clone the repository in colab so that no need to install for requirements.
 This is an example usage of locally.
1. Prepare the path to the dev or test set .
2. Edit `main.py` to set the correct model name and dev set path.
3. Run:

```bash
python main.py
```

This will load the model and tokenizer, run predictions, and save the results to a CSV file.


## References
- Lin et al., 2017. Focal Loss for Dense Object Detection.  
- Conneau et al., 2020. XLM-RoBERTa: Large-Scale Multilingual Representation Learning.  

## Future work
During the test phase final model. An application will be released to upload/download the best model to hugging face and then acces to predict the test set.

## Contact
For questions or collaboration, reach out to:  
**Mirindra Fandresena Randriamanantena** – [mirindraf@aims.ac.za](mailto:mirindraf@aims.ac.za)
