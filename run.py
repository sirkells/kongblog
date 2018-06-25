from blog import app
#app.config['MONGO_DBNAME'] = 'projectfinder'
#app.config['MONGO_URI'] = 'mongodb://localhost:27017/projectfinder'


#mongo = PyMongo(app)

#client = MongoClient('localhost:27017')
#db = client.itproject

#projects = mongo.db.itproject
#project_list = db.find()





if __name__ == '__main__':
    app.run(debug=True)
