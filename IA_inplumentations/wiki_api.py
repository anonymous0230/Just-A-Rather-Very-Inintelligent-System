from os import X_OK
import wikipedia

def get_wiki_ans(try_wiki):
    if try_wiki == "":
        try_wiki = input('wat wil je zoeken')

    return wikipedia.search(try_wiki)



# [u'Barak (given name)', u'Barack Obama', u'
# Barack (brandy)', u'Presidency of Barack Obama', u'Family of Barack Obama', u'First inauguration of Barack Obama', u'Barack Obama presidential campaign, 2008', u'Barack Obama, Sr.', u'Barack Obama citizenship conspiracy theories', u'Presidential transition of Barack Obama']



