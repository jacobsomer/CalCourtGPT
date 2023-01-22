# train.py -- given a set of json files stored in a folder, train.py
# will train a model to answer questions about the legal text in the
# json files. The model will be trained using the metadata from the
# json files.
import os
import json
import requests
import openai


def uploadFile(file_path):
    api_key = os.environ["OPENAI_API_KEY"]
    openai.api_key = api_key
    response = openai.File.create(file=open(file_path), purpose='fine-tune')
    return response["id"]


def fineTuneModel(file_id):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    fine_tune = openai.FineTune.create(
        training_file="file-OpzD4btE7k97mll8qsMlEnK6", model="davinci")


if __name__ == "__main__":
    file_id = uploadFile(
        "/Users/jacobsomer/Documents/Scale-AI-Hackathon/data_extract/cal-law-text.jsonl")
    openai.api_key = os.getenv("OPENAI_API_KEY")
    fine_tune = openai.FineTune.create(
        training_file=file_id, model="davinci")

    print(openai.Completion.create(
        model="davinci",
        prompt="Referencing the California Rules of Court Effective as of January 1, 2022, a professional lawyer answers his client's questions.\n\n Client: how much are the court fees for a civil case? \n California Lawyer:",
        max_tokens=150,
        temperature=0
    ))
