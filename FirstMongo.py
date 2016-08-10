# first you have to setup MongoDB, mine in in "C:\mongodb".
# Create data file in "C:\data\db" using command "mkdir C:\data\db" in command promt.
# Start server using command "mongod" in command prompt.

"""..........Making a Connection with MongoClient.........."""
from pymongo import MongoClient
client = MongoClient()
# The above code will connect on the default host and port. We can also specify the host and port explicitly,
# as follows:
# client = MongoClient('localhost', 27017)
# client = MongoClient('mongodb://localhost:27017/')

"""..........Getting a Database.........."""
# A single instance of MongoDB can support multiple independent databases. When working with PyMongo you access
# databases using attribute style access on MongoClient instances:
db = client.test_database
# If your database name is such that using attribute style access won’t work (like test-database),
#  you can use dictionary style access instead:
# db = client['test-database']

"""..........Getting a Collection.........."""
# A collection is a group of documents stored in MongoDB, and can be thought of as roughly the equivalent of a table in
# a relational database. Getting a collection in PyMongo works the same as getting a database:
collection = db.test_collection
# or (using dictionary style access):
# collection = db['test-collection']
# An important note about collections (and databases) in MongoDB is that they are created lazily - none of the above
# commands have actually performed any operations on the MongoDB server. Collections and databases are created when the
# first document is inserted into them.

"""..........Documents.........."""
# Data in MongoDB is represented (and stored) using JSON-style documents. In PyMongo we use dictionaries to represent
# documents. As an example, the following dictionary might be used to represent a blog post:
import datetime
post = {
    "author": "Sajid",
    "text": "My first practice with MongoDB and Python",
    "tags": ["mongodb", "python", "pymongo"],
    "date": datetime.datetime.utcnow()
}
# Note that documents can contain native Python types (like datetime.datetime instances) which will be automatically
# converted to and from the appropriate BSON types.

"""..........Inserting a Document.........."""
# To insert a document into a collection we can use the insert_one() method:
posts = db.posts
post_id = posts.insert_one(post).inserted_id
print(post_id)
# When a document is inserted a special key, "_id", is automatically added if the document doesn’t already contain an
# "_id" key. The value of "_id" must be unique across the collection. insert_one() returns an instance of
# InsertOneResult. For more information on "_id", see the documentation on _id.
# After inserting the first document, the posts collection has actually been created on the server. We can verify this
# by listing all of the collections in our database:
print(db.collection_names(include_system_collections=False))

"""..........Getting a Single Document With find_one().........."""
# The most basic type of query that can be performed in MongoDB is find_one(). This method returns a single document
# matching a query (or None if there are no matches). It is useful when you know there is only one matching document,
# or are only interested in the first match. Here we use find_one() to get the first document from the posts collection:
print(posts.find_one())
# The result is a dictionary matching the one that we inserted previously.
# Note: The returned document contains an "_id", which was automatically added on insert.
# find_one() also supports querying on specific elements that the resulting document must match. To limit our results
# to a document with author “Sajid” we do:
print(posts.find_one({"author": "Sajid"}))
# If we try with a different author, like “Eliot”, we’ll get no result:
print(posts.find_one({"author": "Eliot"}))
