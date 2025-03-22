def insert_url(db, original_url, short_code):
    db.urls.insert_one({
        "original_url": original_url,
        "short_code": short_code
    })

def find_original_url(db, short_code):
    url = db.urls.find_one({"short_code": short_code})
    return url["original_url"] if url else None

def find_existing_short_code(db, original_url):
    url = db.urls.find_one({"original_url": original_url})
    return url["short_code"] if url else None

