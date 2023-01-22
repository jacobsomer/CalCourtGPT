from PyPDF2 import PdfReader
import os
import json

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

# the following is a function that extracts the strings from a folder of pdfs and saves it as a string


def extractTextFromPDFs(folder_path):
    text = ""
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            with open(os.path.join(folder_path, filename), "rb") as pdf_file:
                reader = PdfReader(pdf_file)
                for page in reader.pages:
                    text += page.extract_text()
    with open("cal-law-text.txt", "w") as f:
        f.write(text)
    return text


if __name__ == "__main__":
    # folder_path = "/Users/jacobsomer/Documents/Scale-AI-Hackathon/data_extract/cal-law-pdf/"
    # extractTextFromPDFs(folder_path)

    # cal_law_text.txt to string
    cal_law_text = ""
    with open("cal-law-text.txt", "r") as f:
        cal_law_text = f.read()

    # split cal_law_text into list of strings split by newline
    cal_law_text = cal_law_text.splitlines()

    # split cal_law_text into list of strings less than 2000 words
    cal_law_text = splitList(cal_law_text)

    # write cal_law_text to jsonl
    for i in range(len(cal_law_text)):
        extract = cal_law_text[i]
        with open("cal-law-text.jsonl", "a") as f:
            json.dump(
                {"prompt": extract, "completion": "The above text is from The California Rules of Court Current as of January 1, 2022."}, f)
