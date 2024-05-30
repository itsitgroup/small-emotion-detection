
# Speech Emotion Detection

This project detects emotions from speech using a neural network model. It includes scripts for recording audio, preprocessing the data, and evaluating the model.

## Model Architecture

The model is a sequential neural network composed of several 1D convolutional layers, activation functions, dropout layers, a max-pooling layer, and a dense layer. Here is a detailed description of each layer and its configuration:

1. **Conv1D Layer 1**:
    - **Name**: `conv1d_7`
    - **Input Shape**: `[None, 216, 1]`
    - **Filters**: 128
    - **Kernel Size**: 5
    - **Activation**: `linear`
    - **Padding**: `same`
    - **Initializer**: `VarianceScaling`

2. **Activation Layer 1**:
    - **Name**: `activation_8`
    - **Activation**: `relu`

3. **Conv1D Layer 2**:
    - **Name**: `conv1d_8`
    - **Filters**: 128
    - **Kernel Size**: 5
    - **Activation**: `linear`
    - **Padding**: `same`
    - **Initializer**: `VarianceScaling`

4. **Activation Layer 2**:
    - **Name**: `activation_9`
    - **Activation**: `relu`

5. **Dropout Layer 1**:
    - **Name**: `dropout_3`
    - **Rate**: 0.1

6. **MaxPooling1D Layer**:
    - **Name**: `max_pooling1d_2`
    - **Pool Size**: 8
    - **Strides**: 8

7. **Conv1D Layer 3**:
    - **Name**: `conv1d_9`
    - **Filters**: 128
    - **Kernel Size**: 5
    - **Activation**: `linear`
    - **Padding**: `same`
    - **Initializer**: `VarianceScaling`

8. **Activation Layer 3**:
    - **Name**: `activation_10`
    - **Activation**: `relu`

9. **Conv1D Layer 4**:
    - **Name**: `conv1d_10`
    - **Filters**: 128
    - **Kernel Size**: 5
    - **Activation**: `linear`
    - **Padding**: `same`
    - **Initializer**: `VarianceScaling`

10. **Activation Layer 4**:
    - **Name**: `activation_11`
    - **Activation**: `relu`

11. **Conv1D Layer 5**:
    - **Name**: `conv1d_11`
    - **Filters**: 128
    - **Kernel Size**: 5
    - **Activation**: `linear`
    - **Padding**: `same`
    - **Initializer**: `VarianceScaling`

12. **Activation Layer 5**:
    - **Name**: `activation_12`
    - **Activation**: `relu`

13. **Dropout Layer 2**:
    - **Name**: `dropout_4`
    - **Rate**: 0.2

14. **Conv1D Layer 6**:
    - **Name**: `conv1d_12`
    - **Filters**: 128
    - **Kernel Size**: 5
    - **Activation**: `linear`
    - **Padding**: `same`
    - **Initializer**: `VarianceScaling`

15. **Activation Layer 6**:
    - **Name**: `activation_13`
    - **Activation**: `relu`

16. **Flatten Layer**:
    - **Name**: `flatten_2`

17. **Dense Layer**:
    - **Name**: `dense_2`
    - **Units**: 10
    - **Activation**: `linear`
    - **Initializer**: `VarianceScaling`

18. **Activation Layer 7**:
    - **Name**: `activation_14`
    - **Activation**: `softmax`

## Setup

1. Clone the repository.
2. Install the dependencies using `pip install -r requirements.txt`.
3. Run the project using `python main.py`.

## Usage

- `preprocess.py`: Contains functions for recording and preprocessing audio.
- `evaluate.py`: Contains the evaluation logic for the model.
- `model.py`: Loads the model architecture from a JSON file.
- `utils.py`: Contains utility functions and label encodings.
- `main.py`: Main entry point for the project.
