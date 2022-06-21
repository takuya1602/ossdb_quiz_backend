from bs4 import BeautifulSoup
import re
import glob


def get_all_html(grades_categories: dict[str, list[str]]) -> list[str]:
    html_files = list()
    for grade, categories in grades_categories.items():
        for category in categories:
            ans_dirs = glob.glob(f"./html/{grade}/{category}/*/ans")
            ans_dirs.sort(key=lambda path: int(re.search(r"\d{2}", path).group(0)))
            for dir in ans_dirs:
                files = glob.glob(f"{dir}/*.html")
                # e.g. file path: ./html/silver/management/01/ans/ans_0.html
                files.sort(key=lambda path: int(re.search(r"ans_(\d+)", path).group(1)))
                html_files.extend(files)
    return html_files


def get_sub_category_from_soup(soup: BeautifulSoup) -> str:
    h2 = soup.select_one(".heading > h2").text
    if match := re.search(
        r"「.+ - (.+)[\(|（].+[\(|（].+[\)|）].+[\(|（].+[\)|）].+[\)|）]」", h2
    ):
        sub_category = match.group(1).strip()
    elif match := re.search(r"「.+ - (.+)[\(|（].+[\(|（].+[\)|）].+[\)|）]」", h2):
        sub_category = match.group(1).strip()
    elif match := re.search(r"「.+ - (.+)[\(|（].+[\)|）] *」", h2):
        sub_category = match.group(1).strip()
    elif match := re.search(r"「.+-(.+)-.+」", h2):
        sub_category = match.group(1).strip()
    elif match := re.search(r"「(.+)[\(|（].+[\)|）] *」", h2):
        sub_category = match.group(1).strip()
    elif match := re.search(r"「.+ - (.+)」", h2):
        sub_category = match.group(1).strip()
    else:
        sub_category = "no_match"
    return sub_category


def get_number_and_title_from_soup(soup: BeautifulSoup) -> tuple[int, str]:
    h4 = soup.select_one(".question > h4").text
    if match := re.search(r"\d\.(\d+) *[NEW|ALTER]* *(.+)", h4):
        number = int(match.group(1))
        title = match.group(2)
    else:
        number = 0
        title = "no_match"
    return number, title


def get_choice_from_soup(soup: BeautifulSoup) -> list[str]:
    if (tmp := soup.select(".question + div > ol > li")) != []:
        li = tmp
    elif (tmp := soup.select(".question + div + div > ol > li")) != []:
        li = tmp
    elif (tmp := soup.select(".question + div + div + div > ol > li")) != []:
        li = tmp
    elif (tmp := soup.select(".question + div > p")) != []:
        li = tmp
    else:
        li = soup.select(".no_match")

    li_text = [i.text.strip() for i in li]
    return li_text


def get_commentary_and_answer_from_soup(soup: BeautifulSoup) -> tuple[str, list[str]]:
    div = soup.select_one(".answer").text
    near_answer = ""
    if match := re.search(r"正解は([A-E]、*)+", div):
        near_answer = match.group(0)
    elif match := re.search(r"[正解|答え]は、*( *[A-E] *と*)+", div):
        near_answer = match.group(0)
    elif match := re.search(r"([A-Z]) *が正解", div):
        near_answer = match.group(0)
    elif match := re.search(r"([A-Z] *と* *)+です", div):
        near_answer = match.group(0)
    else:
        answer = ["no_match"]
    if near_answer != "":
        answer = re.findall(r"[A-E]", near_answer)

    return div, answer
