# SemEval 2026 Task 9: Detecting Multilingual, Multicultural, and Multievent Online Polarization

This repository contains the notebooks and code for **SemEval 2026 Task 9**, focusing on detecting polarized text across multiple languages and contexts.

## Repository Structure
- `polarizatio/` – Contains Jupyter notebooks for each subtask.
- – Place the `dev_phase` folder here to run the notebooks.


## Getting Started
To run the notebooks:

1. Ensure the `dev_phase` folder is located in the same directory as the notebooks.
2. Update the `workdir` variables in each notebook to point to your working directory.
3. Install required dependencies (e.g., using `requirements.txt` if provided).

## Subtasks
- **Subtask 1:** Binary polarization detection (English, Swahili, Hausa)  
- **Subtask 2:** Multilingual polarization classification (English + Swahili)  
- **Subtask 3:** Multilingual manifestation identification (English + Swahili)  

Each notebook is self-contained and provides detailed steps for preprocessing, model training, and evaluation.

## Models
- The final models are based on transformer architectures, including **XLM-RoBERTa** and **RoBERTa-based sentiment models**.  
- Class imbalance is handled via **Focal Loss** and weighted training where applicable.  
- A FastText static embedding approach is also provided as a baseline.

## Test Run
Running the notebooks end-to-end will:
1. Preprocess the dataset.
2. Train models for each subtask.
3.One Fastext model if one have hugging face account models can be saved, then can be uploaded to **Hugging Face** for deployment.

## References
- Lin et al., 2017. Focal Loss for Dense Object Detection.  
- Conneau et al., 2020. XLM-RoBERTa: Large-Scale Multilingual Representation Learning.  

## Future work
For the test phase final model will be released to hugging face and the acces and use f it will be implemented here.

## Contact
For questions or collaboration, reach out to:  
**Mirindra Fandresena Randriamanantena** – [mirindraf@aims.ac.za](mailto:mirindraf@aims.ac.za)  
