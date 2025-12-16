from utils import load_model, predict
import pandas as pd

# Example usage for subtask 1
HF_MODEL_NAME = "mirindraf/aims-sentiment-analysis"  # Change as needed
lan = "eng"  # Change as needed

tokenizer, model = load_model(HF_MODEL_NAME, lan)

dev_path = "dev.csv"  # Path to your dev set CSV
dev_pd = pd.read_csv(dev_path)
if __name__ == "__main__":
    output_csv = predict(tokenizer, model, dev_pd)
    print(f"Predictions saved to {output_csv}")
