import os,sys
from github import Github
from datetime import datetime, timedelta
from pprint import pprint

#token = '4d7b188397667dcd05d6d945b5f2e25ba0fe9ae7'
token = '25ef6409334a6272036f147b9b4d1012bbca6db6'

g = Github(token)

odoorpc= g.get_repo("OCA/odoorpc")
print(odoorpc)
result = []
since = datetime.now() - timedelta(days=100)
for fork in odoorpc.get_forks():
    print(fork)
    commits = fork.get_commits()#since=since)
    if commits.totalCount:
        c0=commits[0]
        print(c0.last_modified)
        result.append((c0.last_modified, fork.full_name))
result.sort()
pprint(result)
sys.exit()
# for repo in g.get_user().get_repos():
#     print(repo)

repos = ['OCA/odoorpc']
# You can change get_organization to get_user()
org = g.get_organization('OCA')

git_repos ={repo: org.get_repo(repo) for repo in repos}
print(git_repos)

# # Issue is a equivalent to pr
# # Issue API should be called first to fetch tags
# def get_pr_from_issues(issues):
#     for issue in issues:
#         if issue.pull_request is not None:
#             pr_id = int(issue.pull_request.html_url.split("/")[-1])
#             yield issue.repository.get_pull(pr_id), issue.labels

# repo_prs = {}
# for repo_name, repo in git_repos.items():
#     repo_prs[repo_name] = get_pr_from_issues(repo.get_issues(state='open'))