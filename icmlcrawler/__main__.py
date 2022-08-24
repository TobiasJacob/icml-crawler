import json
import logging
from multiprocessing import Pool
import os
import pandas as pd
import argparse

from .icml_parse import get_all_papers, get_paper_author_ids, get_university
from tqdm import tqdm

def get_records(paper: dict) -> list:
    """ Get the records of a paper, used for multiprocessing.
    
    Args:
        paper (dict): paper.
    """
    authors = get_paper_author_ids(paper["id"])
    records = []
    for author in authors:
        record = {}
        record["paperid"] = paper["id"]
        record["title"] = paper["title"]
        record["author"] = author["name"]
        record["authorid"] = author["id"]
        record["university"] = get_university(author["id"])
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
    papers = get_all_papers()
    logging.info(f"Found {len(papers)} papers")

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
                    pbar.set_description(f"{new_records[0]['title']}")

                if i % 50 == 0:
                    with open(args.output, "w") as f:
                        json.dump(records, f)
                i += 1
        with open(args.output, "w") as f:
            json.dump(records, f)

    # convert to csv
    df = pd.DataFrame(records)
    df.to_csv(args.csvout, index=False)