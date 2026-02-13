"""
Liam Weeks
Jody Steele
"""
import random

def sample_input_generation():
    names = ["Alice", "Bob", "James", 'bot']
    task = "task" + str(random.randint(0, 100))
    return (random.choice(names), task, random.randint(0, 10))


def is_bot(commit):
    # (x : y : z: _) for indexing a list in haskell
    return commit[0][0:3] == "bot"


def filter(commits):
    if len(commits) == 0:
        return []
    if is_bot(commits[0]) or commits[0][2] <= 0:
        return [] + filter(commits[1:])
    else:
        return [commits[0]] + filter(commits[1:])

def count_filtered_commits(commits):
    if commits == []:
        return 0
    else: 
        return 1 + count_filtered_commits(commits[1:])

def transformation(commit):
    if commit[2] <= 20:
        return commit
    else:
        return (commit[0], commit[1], 20)


def total_lines_changed(commits):
    if len(commits) == 0:
        return 0
    else:
        return commits[0][2] + total_lines_changed(commits[1:])


def tx_list(commits):
    if len(commits) == 0:
        return []

    return transformation(commits[0]) + tx_list(commits[1:])

def total_commits_kept(commits):
    if len(commits) == 0:
        return 0
    else:
        return 1 + total_commits_kept(commits[1:])


if __name__ == "__main__":
    commits = [sample_input_generation() for x in range(0, 3)]
    
    commits.append(('bot', "test", 19))

    print(commits)

    commits = filter(commits)

    lines_changed = total_lines_changed(commits)
    commits_kept = total_commits_kept(commits)

    print(f"Commits: {commits}")
    print(f"Lines Changed: {lines_changed}")
    print(f"Total Commits Kept: {commits_kept}")



