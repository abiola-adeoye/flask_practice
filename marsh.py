

class BookSchema(Schema):

    title = fields.Str()
    author = fields.Str()

incoming_book = {
    "title": "wubaluba dubdub",
    "author": "Pickle Rick",
    "description": "Eat my balls"
}

book_schema = BookSchema(unknown=EXCLUDE)
book = book_schema.load(incoming_book)
print(book)
