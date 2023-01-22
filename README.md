# Legal Text Fine-Tuning with OpenAI

This project demonstrates how to fine-tune a GPT-3 model with legal text using the OpenAI API. The code provided in `train.py` can be used to fine-tune a model to answer questions about legal text stored in a JSONL file. The model will be fine-tuned using the metadata from the JSON file.

## Requirements
- Python 3
- OpenAI API key

## Usage

1. Install the required packages by running `pip install -r requirements.txt`
2. Add your OpenAI API key as an environment variable named `OPENAI_API_KEY`
3. Update the `current_dir` variable in `train.py` to the directory where your JSONL file is stored
4. Run `python train.py` to fine-tune the model and prompt the model to answer a question.
