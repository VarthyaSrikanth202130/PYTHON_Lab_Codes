"""Program to represent data required for "Job Sequencing with Deadlines" using dataclass"""

from dataclasses import dataclass
@dataclass
class Job:
    job_name: str
    profit: int
    deadline: int


if __name__ == '__main__':
    # taking input from users
    job_names = input("Enter Job names: ").split(" ")
    profits = list(map(int, input("Enter Profits: ").split(" ")))
    deadlines = list(map(int, input("Enter Deadlines: ").split(" ")))

    # Storing all jobs in an list
    jobs = [Job(name, profit, deadline)
            for (name, profit, deadline) in zip(job_names, profits, deadlines)]

    print("\nAll Jobs are:")
    for job in jobs:
        print(job)