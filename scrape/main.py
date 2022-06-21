from bs4 import BeautifulSoup
import glob
import re
import json

import config
import func
from models import Question


grades_categories: dict = config.grades_categories


def main():
    questions = list()
    for grade, categories in grades_categories.items():
        for category in categories:
            ans_dirs = glob.glob(f"./html/{grade}/{category}/*/ans")
            ans_dirs.sort(key=lambda path: int(re.search(r"\d{2}", path).group(0)))
            for dir in ans_dirs:
                files = glob.glob(f"{dir}/*.html")
                # e.g. file path: ./html/silver/management/01/ans/ans_0.html
                files.sort(key=lambda path: int(re.search(r"ans_(\d+)", path).group(1)))
                for file in files:
                    with open(file, encoding="utf-8") as f:
                        html = f.read()
                    soup = BeautifulSoup(html, "lxml")

                    sub_category = func.get_sub_category_from_soup(soup)
                    # print(f"{file} sub_category: {sub_category}")

                    number, title = func.get_number_and_title_from_soup(soup)
                    # print(f"{file} number: {number}, title: {title}")

                    choice = func.get_choice_from_soup(soup)
                    # print(f"{file} choice: {choice}")

                    commentary, answer = func.get_commentary_and_answer_from_soup(soup)
                    # print(f"{file} answer: {answer}")

                    question = {
                        "grade": grade,
                        "category": category,
                        "sub_category": sub_category,
                        "number": number,
                        "title": title,
                        "choice": choice,
                        "commentary": commentary,
                        "answer": answer,
                    }

                    questions.append(question)
    with open("questions.json", "w") as f:
        json.dump(questions, f, indent=4)


if __name__ == "__main__":
    main()
