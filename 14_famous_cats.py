"""
Encontrar al gatito más famoso con base en su número de seguidores.
"""
cats_1 = [
    {
        "name": "Luna",
        "followers": [500, 200, 300]
    },
    {
        "name": "Michi",
        "followers": [100, 300]
    },
]

cats_2 = [
    {
        "name": "Mimi",
        "followers": [320, 120, 70]
    },
    {
        "name": "Milo",
        "followers": [400, 300, 100, 200]
    },
    {
        "name": "Gizmo",
        "followers": [250, 750]
    }
]
def most_famous_cats(cat_list):
    max_follows = 0
    famous_cats = []

    for cat in cat_list:
        max_followers_cats = max(cat["followers"])

        if max_followers_cats > max_follows:
            max_follows = max_followers_cats
            famous_cats = [cat["name"]]
        elif max_followers_cats == max_follows:
            famous_cats.append(cat["name"])
    return famous_cats

print(most_famous_cats(cats_1))
print(most_famous_cats(cats_2))
