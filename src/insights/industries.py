from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    jobs = read(path)
    job_industries_list = []
    for job in jobs:
        job_type = job["industry"]
        if job_type != " ":
            job_industries_list.append(job_type)
    return job_industries_list


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    raise NotImplementedError
