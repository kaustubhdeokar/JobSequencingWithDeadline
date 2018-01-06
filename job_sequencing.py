jobs = []


class JobHandler:
    job_name = ""
    profit = 0

    def __init__(self, job_name, profit):
        self.job_name = job_name
        self.profit = profit


def job_optimise(jobs_on_day):
    c = 0
    t = 0
    top_jobs = []
    for i in jobs_on_day[::-1]:
        t += i
        k = max(jobs[len(jobs) - t + c:], key=lambda p: p.profit)
        c += 1
        jobs.remove(k)
        top_jobs = [k] + top_jobs
    for i in top_jobs:
        print (i.job_name, i.profit)


if __name__ == "__main__":
    days = int(input("enter no. of days : "))
    jobs_on_day = []
    for i in range(days):
        print ("enter no. of jobs on day " + str(i + 1))
        jobs_on_day.append(int(input()))
        for j in range(jobs_on_day[i]):
            job_name = input("job name : ")
            profit = int(input('profit :'))
            jobs.append(JobHandler(job_name, profit))
    job_optimise(jobs_on_day)
