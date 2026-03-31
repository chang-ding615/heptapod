from tools.cms_dqm.training.train import train_baseline_model
from tools.cms_dqm.inference.predict import run_inference

def main():
    train_baseline_model("data/sample_dqm.csv", "outputs/baseline_model")
    results = run_inference("data/sample_dqm.csv", "outputs/baseline_model")
    print(results.head())

if __name__ == "__main__":
    main()