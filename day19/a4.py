scores = {'math':85,'english':-1,'science':92}

invalid = {subject: score for subject,score in scores.items() if score < 0 or score > 100 }


if invalid:
    print('Invalid Score Detected:')
    for subject,score in invalid.items():
        print(f'{subject}:{score}')
else:
    print('All score valid')