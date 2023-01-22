# train.py -- given a set of json files stored in a folder, train.py
# will train a model to answer questions about the legal text in the
# json files. The model will be trained using the metadata from the
# json files.
import os
import json
import requests
import openai

folder_path = "/Users/jacobsomer/Documents/Scale-AI-Hackathon/"

# the following is a function that uploads a file to openAPI for the purpose of answering questions
# about the legal text in the file


def uploadFile(file_path):
    api_key = os.environ["OPENAI_API_KEY"]
    openai.api_key = api_key
    response = openai.File.create(file=open(file_path), purpose='fine-tune')
    return response["id"]

# change a json file with format {"text": "text", "metadata": "metadata"} to {"prompt": "text"+"... \n where is the above file from?", "completion": "The above text is from The California Rules of Court Current as of January 1, 2022."}


# def changeJsonFile(file_path):
#     with open(file_path, "r") as f:
#         d = json.load(f)
#     d["prompt"] = d["prompt"]
#     d["completion"] = "The above text is from The California Rules of Court Current as of January 1, 2022."
#     # delete d["text"] and d["metadata"]
#     del d["text"]
#     del d["metadata"]
#     with open(file_path, "w") as f:
#         json.dump(d, f)

# json to dictionairy
def jsonToDict(file_path):
    with open(file_path, "r") as f:
        d = json.load(f)
    return d

# get convert the json files in a folder to a dictionairy and then save them line by line as text into one jsonl file


def jsonlFile():
    with open("cal-law-text.jsonl", "w") as f:
        for i in range(0, 203):
            d = {}
            file_path = folder_path + "/cal-law/" + \
                "cal-law-text-" + str(i) + ".json"
            if os.path.exists(file_path):
                d = jsonToDict(file_path)
                f.write(json.dumps(d) + "\n")


# def fineTuneModel():
#     file_ids = []
#     with open("file_ids.txt", "r") as f:
#         file_ids = f.read().splitlines()
#     api_key = os.environ["OPENAI_API_KEY"]
#     openai.api_key = api_key
#     for file in file_ids:

#     response = openai.Engine("davinci").create(
#         files=file_ids,
#         model="curie:ft-1",
#         version=1,
#         temperature=0.9,
#         max_tokens=150,
#         top_p=1,
#         frequency_penalty=0,
#         presence_penalty=0.6,
#     )
#     return response


if __name__ == "__main__":
    # for i in range(0, 203):
    #     file_path = folder_path + "/cal-law/" + \
    #         "cal-law-text-" + str(i) + ".json"
    #     if os.path.exists(file_path):
    #         id = uploadFile(file_path)
    #         print(id)
    #         # save file_id to text file line by line
    #         with open("file_ids.txt", "a") as f:
    #             f.write(id + "\n")
    #     else:
    #         print("file does not exist")
    # print(fineTuneModel())
    # print(uploadFile(
    # "/Users/jacobsomer/Documents/Scale-AI-Hackathon/data_extract/cal-law-text.jsonl"))
    # jsonlFile()
    # file_id = "file-k9VOqvdDaGtQbmrozSkfJWtB"
    # openai.api_key = os.getenv("OPENAI_API_KEY")
    # fine_tune = openai.FineTune.create(
    #     training_file="file-OpzD4btE7k97mll8qsMlEnK6", model="davinci")
    # print(openai.FineTune.list())
    print(openai.Completion.create(
        model="davinci",
        prompt="Referencing the California Rules of Court Effective as of January 1, 2022, a professional lawyer answers his client's questions.\n\n Client: how much are the court fees for a civil case? \n California Lawyer:",
        max_tokens=150,
        temperature=0
    ))
