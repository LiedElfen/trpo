#!/usr/bin/env python3
from github import Github
from os.path import isfile, join
from os import environ, listdir


def git_curret_branch():
    with open('.git/HEAD') as f:
         body = f.read()

    PREFIX = 'ref: refs/heads/'
    return body[len(PREFIX):]


def log(job):
    filename = '/tmp/{}.log'.format(job)
    with open(filename) as f:
         return f.read().strip()


def exit_code(job):
    filename = '/tmp/{}.res'.format(job)
    with open(filename) as f:
         return int.from_bytes(f.read().strip(), 'big')


def main():
    token = environ.get('GH_TOKEN')
    job = environ.get('JOB')

    body = log(job)
    if (body == ''):
       return

    res = exit_code(job)

    g = Github(token)
    repo = g.get_repo('liedelfen/trpo')

    branch = git_current_branch()
    ISSUE = 'issue'
    if branch.starswith(ISSURE):
       issure_num = num(branch[len(ISSURE):])
       issure = repo.get_issure(issure_num)
    else:
       if res == 0:
          return;
       issure = repo.create_issure('Nightly build failed', 'Travis nightly build failed')

    START_BODE = '## Travis {} result'.format(job)
    comment = None
    for c in issure.get_comments():
        if c.body.startswith(START_BODY):
           comment = c

    body = '{}\n```\n{}\n```'.format(START_BODY, body)
    if comment:
       comment.edit(body)
    else:
       issure.create_comment(body)

if __name__ == "__main__":
     main()
