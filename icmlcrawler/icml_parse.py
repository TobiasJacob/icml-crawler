from .cached_request import cached_request


def get_all_papers(year: int):
    """Get all papers from the ICML conference website.

    Returns:
        list: list of all papers.
    """
    url = f"https://icml.cc/Conferences/{year}/Schedule?type=Poster"
    soup = cached_request(url)
    papers = soup.find_all("div", class_="poster")

    return [{
        "year": year,
        "title": paper.find(class_="maincardBody").text,
        "author": paper.find(class_="maincardFooter").text,
        "id": int(paper["id"].split("_")[1]),
        } for paper in papers]


def get_paper_details(year: int, paper_id: int) -> list:
    """Get the author ids of a paper.

    Args:
        paper_id (int): id of the paper.

    Returns:
        list: list of author ids.
    """
    url = f"https://icml.cc/Conferences/{year}/Schedule?showEvent={paper_id}"
    soup = cached_request(url)
    authors = soup.find(id="base-main-content")
    if authors is None:
        authors = []
    else:
        authors = authors.find_all("button")

    abstract = soup.find(class_="abstractContainer")
    if abstract is not None:
        abstract = abstract.find("p")
    if abstract is not None:
        abstract = abstract.text

    return {
        "year": year,
        "authors": [{
            "id": aut["onclick"].split("'")[1],
            "name": aut.text[:-1].strip(),
        } for aut in authors],
        "id": paper_id,
        "abstract": abstract,
    }

def get_institution(year: int, author_id: int) -> str:
    """Get the institution of a author.

    Args:
        author_id (int): id of the author.

    Returns:
        str: institution of the author.
    """
    url = f"https://icml.cc/Conferences/{year}/Schedule?showSpeaker={author_id}"
    soup = cached_request(url)
    institution = soup.find(class_="Remark").find("h4").text
    return institution

# print(get_all_papers(2022)[:5])
# print(get_paper_details(2022, 17783))
# print(get_institution(2022, "68092-17783"))