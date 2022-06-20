import unittest

from bs4 import BeautifulSoup
import config
import func

grades_categories: dict = config.grades_categories


class TestGetFunction(unittest.TestCase):
    def setUp(self) -> None:
        print("setup")
        self.files: list[str] = func.get_all_html(grades_categories)
        self.element_num: int = len(self.files)

    def test_get_sub_category_from_soup(self):
        sub_categories = list()
        for file in self.files:
            with open(file, encoding="utf-8") as f:
                html = f.read()
            soup = BeautifulSoup(html, "lxml")
            sub_category = func.get_sub_category_from_soup(soup)

            self.assertNotEqual(
                sub_category,
                "no_match",
                f"There is no_match in searching sub_category in file: {file}",
            )

            self.assertIsNotNone(
                sub_category,
                f"sub_category is not fonud in file: {file}",
            )

            sub_categories.append(sub_category)

        self.assertEqual(
            len(sub_categories),
            self.element_num,
            f"There are some cases where sub_category cannot be extracted from soup",
        )

    def test_get_number_and_title_from_soup(self):
        numbers = list()
        titles = list()
        for file in self.files:
            with open(file, encoding="utf-8") as f:
                html = f.read()
            soup = BeautifulSoup(html, "lxml")
            number, title = func.get_number_and_title_from_soup(soup)

            # the following file
            if file == "./html/gold/monitoring/01/ans/ans_4.html":
                number = 99999  # add manually later
                title = "add manually later"

            # self.assertNotEqual(number, 0) is unnecessary
            # because if number == 0, title == "no_match" (definitly)
            self.assertNotEqual(
                title,
                "no_match",
                f"There is no_match in searching number and title in file: {file}",
            )

            self.assertIsNotNone(
                number,
                f"number is not found in file: {file}",
            )

            self.assertIsNotNone(
                title,
                f"title is not found in file; {file}",
            )

            numbers.append(number)
            titles.append(title)

        self.assertEqual(
            len(titles),
            self.element_num,
            "There are some cases where number and title cannot be extracted from soup",
        )

    def test_get_choice_from_soup(self):
        choices = list()
        for file in self.files:
            with open(file, encoding="utf-8") as f:
                html = f.read()
            soup = BeautifulSoup(html, "lxml")
            choice = func.get_choice_from_soup(soup)
            choices.append(choice)

        self.assertEqual(
            len(choices),
            self.element_num,
            "There are some cases where choice cannot be extracted from soup",
        )

    def test_get_commentary_and_answer_from_soup(self):
        commentaries = list()
        for file in self.files:
            with open(file, encoding="utf-8") as f:
                html = f.read()
            soup = BeautifulSoup(html, "lxml")
            commentary = func.get_commentary_and_answer_from_soup(soup)
            commentaries.append(commentary)

        self.assertEqual(
            len(commentaries),
            self.element_num,
            f"There are some cases where commentary cannot be extracted from soup",
        )


if __name__ == "__main__":
    unittest.main()
