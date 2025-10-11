checklist = {
    'test_passed':True,
    'env_ready':False,
    'version_tagged':True,
}


if all(checklist.values()):
    print('Ready to deploy')
else:
    failed = [k for k,v in checklist.items() if not v]
    print('Deployment blocked due to:',",".join(failed))