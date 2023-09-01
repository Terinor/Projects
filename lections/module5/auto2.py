articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]


# def find_articles(key, letter_case=False):
#     if letter_case:
#         for articles in articles_dict:
#             for item in articles.values():
#                 item = str(item)
                
#     for articles in articles_dict:
#         for item in articles.values():
#             item.find(key)

def find_articles(key, letter_case=False):
    matching_articles = []

    for article in articles_dict:
        title = article["title"]
        author = article["author"]

        if not letter_case:
            if key.lower() in title.lower() or key.lower() in author.lower():
                matching_articles.append(article)
        else:
            if key in title or key in author:
                matching_articles.append(article)

    return matching_articles
    
    

print(find_articles(key = "ocean"))
