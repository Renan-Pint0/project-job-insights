from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    jobs = read(path)
    max_salary = 0
    job_list = []
    for job in jobs:
        job_type = job["max_salary"]
        if job_type != "invalid" and len(job_type) != 0:
            job_list.append(job_type)
    for salary in job_list:
        int_salary = int(salary)
        if int_salary > max_salary:
            max_salary = int_salary
    return max_salary


def get_min_salary(path: str) -> int:
    jobs = read(path)
    job_list = []
    for job in jobs:
        job_type = job["min_salary"]
        if job_type != "invalid" and len(job_type) != 0:
            job_list.append(job_type)
    min_salary = int(job_list[0])
    for salary in job_list:
        int_salary = int(salary)
        if int_salary < min_salary:
            min_salary = int_salary
    return min_salary


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        min_salary = int(job["min_salary"])
        max_salary = int(job["max_salary"])
        if int(min_salary) > int(max_salary):
            raise (ValueError)
        elif int(min_salary) <= int(salary) <= int(max_salary):
            return True
        else:
            return False
    except (TypeError, KeyError):
        raise ValueError


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    job_list = []
    for job in jobs:
        try:
            job_salary = matches_salary_range(job, salary)
            if job_salary is True:
                job_list.append(job)
        except ValueError:
            print("Invalid Salary")
    return job_list
