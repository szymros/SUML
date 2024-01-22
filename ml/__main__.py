from ml.prepare_data import prepare_data
from ml.train_model import model_pipeline


def main():
    prepare_data()
    model_pipeline()
    
    

if __name__ == "__main__":
    main()