import os
import json
import traceback
import PyPDF2

def read_file(file):
    if file is None:
        raise Exception("Please upload a file.")
    
    try:
        if file.name.endswith(".pdf"):
            with open(file.name, "rb") as pdf_file:
                pdf_reader = PyPDF2.PdfReader(pdf_file)
                text = ""
                for page in pdf_reader.pages:
                    text += page.extract_text()
            return text
        elif file.name.endswith(".txt"):
            return file.read().decode("utf-8")
        else:
            raise Exception("Unsupported file format. Only PDF and text files are supported.")
    except FileNotFoundError as e:
        raise Exception(f"Error reading the PDF file: {str(e)}")


def get_table_data(quiz_str):
    try:
        quiz_dict = json.loads(quiz_str)
        quiz_table_data = []

        for key, value in quiz_dict.items():
            mcq = value["mcq"]
            options = " || ".join(
                [f"{option}->{option_value}" for option, option_value in value["options"].items()]
            )
            correct = value["correct"]
            quiz_table_data.append({"MCQ": mcq, "Choices": options, "Correct": correct})

        return quiz_table_data

    except Exception as e:
        traceback.print_exception(type(e), e, e.__traceback__)
        return False
