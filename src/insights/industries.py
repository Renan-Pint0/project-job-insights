from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    jobs = read(path)
    job_industries_list = []
    for job in jobs:
        job_type = job["industry"]
        if job_type not in job_industries_list:
            job_industries_list.append(job_type)
        if len(job_type) == 0:
            job_industries_list.remove(job_type)
    return job_industries_list


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    job_industries_list = []
    for job in jobs:
        job_list = job["industry"]
        if job_list == industry:
            job_industries_list.append(job)
    return job_industries_list
