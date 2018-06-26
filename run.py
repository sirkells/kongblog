from blog import create_app
#app.config['MONGO_DBNAME'] = 'projectfinder'
#app.config['MONGO_URI'] = 'mongodb://localhost:27017/projectfinder'


#mongo = PyMongo(app)

#client = MongoClient('localhost:27017')
#db = client.itproject

#projects = mongo.db.itproject
#project_list = db.find()



app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
