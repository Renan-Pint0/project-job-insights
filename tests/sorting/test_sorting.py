from src.pre_built.sorting import sort_by
import pytest


@pytest.fixture
def jobs():
    return [
        {
            "title": "Web developer",
            "min_salary": 100,
            "max_salary": 200,
            "date_posted": "2023-01-01",
        },
        {
            "title": "Front end developer",
            "min_salary": 150,
            "max_salary": 205,
            "date_posted": "2023-01-02",
        },
        {
            "title": "Back End Developer",
            "min_salary": 200,
            "max_salary": 250,
            "date_posted": "2023-01-03",
        },
        {
            "title": "Full stack end developer",
            "min_salary": 120,
            "max_salary": 300,
            "date_posted": "2023-01-04",
        },
    ]


def test_sort_by_criteria(jobs):
    jobs_list = jobs
    sort_by(jobs_list, "min_salary")
    assert jobs_list[0]["min_salary"] == 100
    assert jobs_list[3]["min_salary"] == 200
