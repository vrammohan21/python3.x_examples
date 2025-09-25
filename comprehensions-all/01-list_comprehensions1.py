list_liked = [1, 2, 3, 4, 5, 4, 5, 1]

likes=sum([like for like in list_liked])/len(list_liked)
avg_likes=sum(likes)/len(likes)
print(f"Average likes of likes from {list_liked} = {avg_likes}")