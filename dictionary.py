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

# UPDATE 
# get_book = library.get("1")
   #OPTION 1 # get_book["author"] = "ELON MUSK"
   #OPTION 2 # get_book.update({"author": "hhhh"})
# print(get_book)



# DELETE
# get_book = library.get("1")
# del get_book["author"]
#print(get_book)



# Retrieve Author 

# get_book = library.get("1")
# OPTION 1
# author= get_book["author"]
#print( author)

#OPTION 2 
#print( get_book['author'])


#OPTION 3  print(library.get("1")["author"])


# Find a books based on its ISBN number

# print(library.get("2")["ISBN"])