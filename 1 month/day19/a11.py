names = ['Alice','Bob','Charlie']
scores = [85,90,92]
subject = ['Math','Science','Filipino']


for name,score,subject in zip(names,scores,subject):
    print(f'{name} scored {subject} {score}')