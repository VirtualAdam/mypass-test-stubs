
def palm_check(filename):
    if filename == 'openhand.jpg':
        return 'access granted'
    elif filename == 'closedhand.jpg':
        return 'access denied'
    else:
        return 'not recognized'

if __name__ == "__main__":
    # execute only if run as a script
    count = palm_check('openhand.jpg')
    print(count)