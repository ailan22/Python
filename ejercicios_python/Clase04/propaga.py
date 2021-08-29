def propagar (vector):
    post = []
    for j, n in enumerate(vector):
        if n == -1:
            post.append(-1)
        elif n== 0:
            try:
                if vector[j-1] == 1:
                    post.append(1)
                elif vector[j+1] == 1:
                    post.append(1)
                else:
                    post.append(0)
            except IndexError:
                post.append(0)
        else:
            post.append(1)
    return post

propagar([ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0])

