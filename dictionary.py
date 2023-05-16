library = {
        '1':{
        'author': 'FaithK',
        'title': 'How to win',
        'year':2020,
        'ISBN': 100
        }, 
        '2':{
        'author': 'Kym',
        'title': 'How to Sleep',
        'year':2023,
        'ISBN': 10032
        },

}

get_book = library.get("1")
get_book["author"] = "calvin"

print(get_book)






# library = {
#         '1':{
#         'author': 'FaithK',
#         'title': 'How to win',
#         'year':2020,
#         'ISBN': 100
#         }, 
#         '2':{
#         'author': 'Kym',
#         'title': 'How to Sleep',
#         'year':2023,
#         'ISBN': 10032
#         },

# }

# get_book = library.get("1")
# get_book.update({"author": "hhhh"})

# print(get_book)

