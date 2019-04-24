import unicodedata

def findUnicode(unisearch):
    array_result=dict()
    a_bool = 'U+' in unisearch
    #exception pour les chiffres de 0 a 9
    if(unisearch.isdigit()==True and int(unisearch)<10):
        searchNumber = 48+int(unisearch)
        letter = chr(int(searchNumber))
        name_unicode = unicodedata.name(letter,' ')
        category = unicodedata.category(chr(int(searchNumber)))
        array_result[0] = {} 
        array_result[0]['unicode']=u""+letter+""
        array_result[0]['name']=name_unicode
        array_result[0]['number']=int(searchNumber)
        array_result[0]['cat']=category
        return array_result
    #test si chiffres
    elif(unisearch.isdigit()==True):
        letter = chr(int(unisearch))
        name_unicode = unicodedata.name(letter,' ')
        category = unicodedata.category(chr(int(unisearch)))
        array_result[0] = {} 
        array_result[0]['unicode']=u""+letter+""
        array_result[0]['name']=name_unicode
        array_result[0]['number']=int(unisearch)
        array_result[0]['cat']=category
        return array_result
    #test hexa    
    elif(a_bool==True):
        char = chr(int(unisearch[2:], 16))
        number = ord(char)
        name_unicode = unicodedata.name(chr(number),' ')
        category = unicodedata.category(chr(number))
        array_result[0] = {} 
        array_result[0]['unicode']=u""+letter+""
        array_result[0]['name']=name_unicode
        array_result[0]['number']=number
        array_result[0]['cat']=category
        return array_result
    #si un seul char
    elif(len(unisearch)==1):
        number = ord(unisearch)
        name_unicode = unicodedata.name(chr(number),' ')
        category = unicodedata.category(chr(number))
        array_result[0] = {} 
        array_result[0]['unicode']=u""+letter+""
        array_result[0]['name']=name_unicode
        array_result[0]['number']=number
        array_result[0]['cat']=category
        return array_result
    #si name
    else:
        m=0
        for k in range(22999):
            letter = chr(k)
            name_unicode = unicodedata.name(letter,' ')
            a_bool = unisearch in name_unicode
            if(a_bool == True):
                actual=unicodedata.lookup(name_unicode)
                number = ord(actual)
                name_unicode = unicodedata.name(chr(number),' ')
                category = unicodedata.category(chr(number))  
                array_result[m] = {}   
                array_result[m]['unicode']=u""+letter+""
                array_result[m]['name']=name_unicode
                array_result[m]['number']=number
                array_result[m]['cat']=category
                m=m+1
        print(array_result)
        return array_result
def getAllInformations():
    array_result=dict()
    for j in range(22999):
        letter = chr(j)
        name_unicode = unicodedata.name(letter,' ')
        category = unicodedata.category(chr(j))
        array_result[j] = {}
        array_result[j]['unicode']=u""+letter+""
        array_result[j]['name']=name_unicode
        array_result[j]['number']=j
        array_result[j]['cat']=category
    return array_result
def UniqueUni(codepoint):
    array_result=dict()
    letter = chr(int(codepoint))
    print(letter)
    name_unicode = unicodedata.name(letter,' ')
    category = unicodedata.category(chr(int(codepoint)))
    array_result['unicode']=u""+letter+""
    array_result['name']=name_unicode
    array_result['number']=int(codepoint)
    array_result['cat']=category
    return array_result