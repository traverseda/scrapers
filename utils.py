import copy

def consolodateComments(comments, depth=0):
    print(depth)
    if not type(comments) == list:
        comments = [comments,]

    for comment in comments:
        c=copy.copy(comment.__dict__)
        del(c['_pq'])
        c['comments']=c
        if comment.comments:
            c['comments'] = [ i for i in consolodateComments(comment.comments)]
        yield c
