from bs4 import BeautifulSoup

import config
import func

grades_categories: dict = config.grades_categories


def main():
    files = func.get_all_html(grades_categories)
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
        print(f"{file} answer: {answer}")


if __name__ == "__main__":
    main()
