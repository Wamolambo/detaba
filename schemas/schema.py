## serializer and Entity managment

def userEntity(item) -> dict:
    return{
        "id":str(item["_id"]),
        "paragraph": item["paragraph"],
        "title": item["title"],
        "author": item["author"],
        "url": item["url"]
    }
    
def usersEntity(entity) -> list:
    return [userEntity(item) for item in entity]

def test(a) -> dict:
    return {**{i:str(a[i]) for i in a if i=='_id'},**{i:a[i] for i in a if i!='_id'}}

def serializeDict(a) -> dict:
    return {**{i:str(a[i]) for i in a if i=='_id'},**{i:a[i] for i in a if i!='_id'}}

def serializeList(entity) -> list:
    return [serializeDict(a) for a in entity]