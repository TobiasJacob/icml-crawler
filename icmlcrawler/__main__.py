import json
import logging
from multiprocessing import Pool
import os
import pandas as pd
import argparse

from .icml_parse import get_all_papers, get_paper_details, get_institution
from tqdm import tqdm

def get_records(paper: dict) -> list:
    """ Get the records of a paper, used for multiprocessing.
    
    Args:
        paper (dict): paper.
    """
    paper_details = get_paper_details(paper["year"], paper["id"])
    authors = paper_details["authors"]
    records = []
    for author in authors:
        record = {}
        record["paperid"] = paper["id"]
        record["title"] = paper["title"]
        record["author"] = author["name"]
        record["authorid"] = author["id"]
        record["abstract"] = paper_details["abstract"]
        record["year"] = paper["year"]
        record["institution"] = get_institution(paper["year"], author["id"])
        records.append(record)
    return records

if __name__ == "__main__":
    # parse args
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", "-o", type=str, default="records.json", help="output file")
    parser.add_argument("--csvout", type=str, default="records.csv", help="output file")
    parser.add_argument("--processes", "-n", type=int, default=os.cpu_count() * 2, help="number of processes")
    args = parser.parse_args()

    # get all papers
    logging.info("Starting ICML Crawler")
    records = []
    for year in reversed(range(2010, 2023)):
        papers = get_all_papers(year)

        # don't download papers that are already in database
        file_name = args.output
        if os.path.exists(file_name):
            with open(file_name, "r") as f:
                records = json.load(f)
        existing_paper_ids = set([record["paperid"] for record in records])
        papers = [paper for paper in papers if paper["id"] not in existing_paper_ids]

        # download paper authors
        if len(papers) > 0:
            with Pool(processes=args.processes) as pool:
                pbar = tqdm(pool.imap(get_records, papers), total=len(papers))
                i = 0
                for new_records in pbar:
                    records.extend(new_records)
                    if len(new_records) > 0:
                        pbar.set_description(f"{year} - {new_records[0]['title'][:20]}")

                    if i % 50 == 0:
                        with open(args.output, "w") as f:
                            json.dump(records, f)
                    i += 1
            with open(args.output, "w") as f:
                json.dump(records, f)

    # convert to csv
    df = pd.DataFrame(records)
    df.to_csv(args.csvout, index=False)
