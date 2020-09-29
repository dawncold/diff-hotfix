import sys

def read_log_file(filepath):
    with open(filepath, encoding='utf16') as f:
        logs = []
        for line in f.readlines():
            if line.strip():
                logs.append(tuple(line.split(' ', 1)))
    return logs


def diff(current_logs, upstream_logs):
    upstream_titles = set([l[1] for l in upstream_logs])
    should_cherry_pick_logs = []
    for log in current_logs:
        if log[1] not in upstream_titles:
            print(log)
            should_cherry_pick_logs.append(log)
    print(' '.join(reversed([log[0] for log in should_cherry_pick_logs])))

if __name__ == '__main__':
    head_filepath, upstream_filepath = sys.argv[1:]
    diff(read_log_file(head_filepath), read_log_file(upstream_filepath))