from .cached_request import cached_request


def get_all_papers():
    """Get all papers from the ICML conference website.

    Returns:
        list: list of all papers.
    """
    url = "https://icml.cc/Conferences/2022/Schedule?type=Poster"
    soup = cached_request(url)
    papers = soup.find_all("div", class_="poster")

    return [{
        "title": paper.find(class_="maincardBody").text,
        "author": paper.find(class_="maincardFooter").text,
        "id": int(paper["id"].split("_")[1]),
        } for paper in papers]


def get_paper_details(paper_id: int) -> list:
    """Get the author ids of a paper.

    Args:
        paper_id (int): id of the paper.

    Returns:
        list: list of author ids.
    """
    url = f"https://icml.cc/Conferences/2022/Schedule?showEvent={paper_id}"
    soup = cached_request(url)
    authors = soup.find(id="base-main-content").find_all("button")

    abstract = soup.find(class_="abstractContainer").find("p")
    if abstract is not None:
        abstract = abstract.text

    return {
        "authors": [{
            "id": aut["onclick"].split("'")[1],
            "name": aut.text[:-1].strip(),
        } for aut in authors],
        "id": paper_id,
        "abstract": abstract,
    }

def get_university(author_id: int) -> str:
    """Get the university of a author.

    Args:
        author_id (int): id of the author.

    Returns:
        str: university of the author.
    """
    url = f"https://icml.cc/Conferences/2022/Schedule?showSpeaker={author_id}"
    soup = cached_request(url)
    university = soup.find(class_="Remark").find("h4").text
    return university

# print(get_all_papers()[:5])
# print(get_paper_details(17783))
# print(get_university("68092-17783"))