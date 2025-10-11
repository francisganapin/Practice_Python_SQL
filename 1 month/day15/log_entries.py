from collections import Counter
import re



log_entries = [
    "[ERROR] Disk full on /dev/sda1",
    "[INFO] Backup completed",
    "[ERROR] Disk full on /dev/sda1",
    "[WARNING] CPU usage high",
    "[ERROR] Network timeout",
    "[ERROR] Disk full on /dev/sda1",
    "[ERROR] Network timeout",
    "[INFO] System rebooted"
]


error_message = [re.search(r'\[ERROR\](.+)',entry).group(1) for entry in log_entries if '[ERROR]' in entry]


error_counts = Counter(error_message)

top_errors = error_counts.most_common(2)

print('Top Erorr:')
for error,count in top_errors:
    print(f'{error}(Occured {count} times)')