

def delete(files, dict):

    for i, v in enumerate(files):
        if v['title'] == dict['title']:
            files.pop(i)
    return files
