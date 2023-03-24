import csv
from functools import lru_cache
from typing import List, Dict


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path) as file:
        header, *file_list = csv.reader(file)
        result = []
        for value in file_list:
            job = {}
            for index, item in enumerate(value):
                job[header[index]] = item
            result.append(job)
        return result


def get_unique_job_types(path: str) -> List[str]:
    jobs = read(path)
    job_type_list = []
    for job in jobs:
        job_type = job["job_type"]
        if job_type not in job_type_list:
            job_type_list.append(job_type)
    return job_type_list


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError
