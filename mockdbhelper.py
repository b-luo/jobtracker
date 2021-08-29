from mockdata import MOCK_JOBS

class MockDBHelper:
    def __init__(self):
        return

    def addJob(self, job_info):
        MOCK_JOBS.append(job_info)
        return True

    def getAllJobs(self):
        return MOCK_JOBS
    
