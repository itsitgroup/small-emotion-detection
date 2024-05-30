from preprocess import audio_recorder
from evaluate import evaluate
from utils import lb

def main():
    audio_recorder()
    predictions = evaluate()
    emotions = lb.inverse_transform(predictions)
    print("Predicted emotions:", emotions)

if __name__ == "__main__":
    main()
