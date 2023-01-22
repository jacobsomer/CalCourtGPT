from PyPDF2 import PdfReader
import os
import json
import requests
import openai

folder_path = "/Users/jacobsomer/Documents/Scale-AI-Hackathon/cal-law-pdf/"

# the following is a function that takes a list strings and saves each
# substring sum less than 2000 words to a new list


def splitList(list):
    new_list = []
    temp_string = ""
    for i in range(len(list)):
        if len(temp_string.split(" ")) + len(list[i].split(" ")) < 1900:
            temp_string = temp_string + list[i]
        else:
            new_list.append(temp_string)
            temp_string = ""
    return new_list


def getMetaDatafromText(text):
    api_key = os.environ["OPENAI_API_KEY"]
    openai.api_key = api_key
    text = text + "\n The following is a one sentence medata summary of the above legal text: "
    response = openai.Completion.create(
        engine="davinci",
        prompt=text,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
    )
    return response["choices"][0]["text"]


if __name__ == "__main__":
    # cal_law_text.txt to string
    cal_law_text = ""
    with open("cal-law-text.txt", "r") as f:
        cal_law_text = f.read()

    # split cal_law_text into list of strings split by newline
    cal_law_text = cal_law_text.splitlines()

    # split cal_law_text into list of strings less than 2000 words
    cal_law_text = splitList(cal_law_text)

    # get metadata list for each string in cal_law_text
    max_length = 1000
    for i in range(len(cal_law_text)):
        extract = cal_law_text[i]
        meta = getMetaDatafromText(
            "".join(extract.split(" ")[:max_length]))
        d = {"text": cal_law_text[i], "metadata": meta}
        with open("cal-law-text-" + str(i) + ".json", "w") as f:
            json.dump(d, f)
        # print progress on the same line
        print("Progress: " + str(i) +
              "/" + str(len(cal_law_text)), end="\r")
