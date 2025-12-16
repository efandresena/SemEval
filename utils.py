from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, DataCollatorWithPadding
import torch
import pandas as pd

# Fixed config values for subtask 1
CONFIG = {
    'max_length': 300,
}

def load_model(HF_model_name, lan):
    tokenizer = AutoTokenizer.from_pretrained(HF_model_name)
    model = AutoModelForSequenceClassification.from_pretrained(HF_model_name)
    return tokenizer, model

def predict(tokenizer, model, dev_pd):
    class PolarizationDataset(torch.utils.data.Dataset):
        def __init__(self, texts, labels, tokenizer, max_length=300):
            self.texts = texts
            self.labels = labels
            self.tokenizer = tokenizer
            self.max_length = max_length
        def __len__(self):
            return len(self.texts)
        def __getitem__(self, idx):
            enc = self.tokenizer(
                str(self.texts[idx]),
                truncation=True,
                max_length=self.max_length,
                padding=False,
                return_tensors='pt'
            )
            item = {k: v.squeeze(0) for k, v in enc.items()}
            item['labels'] = torch.tensor(0, dtype=torch.long)  # dummy label
            return item

    dummy_labels = [0] * len(dev_pd)
    dev_dataset = PolarizationDataset(
        dev_pd['text'].tolist(),
        dummy_labels,
        tokenizer,
        CONFIG['max_length']
    )
    trainer = Trainer(
        model=model,
        tokenizer=tokenizer,
        data_collator=DataCollatorWithPadding(tokenizer)
    )
    predictions = trainer.predict(dev_dataset)
    pred_labels = torch.argmax(torch.tensor(predictions.predictions), axis=1).numpy()
    dev_pd = dev_pd.copy()
    dev_pd['polarization'] = pred_labels
    output_csv = 'predicted.csv'
    dev_pd[['id', 'polarization']].to_csv(output_csv, index=False)
    return output_csv
