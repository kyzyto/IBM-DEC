wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/nosql/catalog.json


wget https://fastdl.mongodb.org/tools/db/mongodb-database-tools-ubuntu1804-x86_64-100.3.1.tgz
tar -xf mongodb-database-tools-ubuntu1804-x86_64-100.3.1.tgz
export PATH=$PATH:/home/project/mongodb-database-tools-ubuntu1804-x86_64-100.3.1/bin
echo "done"

mongoimport --version

start_mongo

mongoimport -u root -p MTQyNDQta2l6aXRv --authenticationDatabase admin --db catalog --collection electronics --file catalog.json

mongo -u root -p MTQyNDQta2l6aXRv --authenticationDatabase admin local


#
show dbs

#
use catalog
show collections

#
db.electronics.createIndex({"type":1})
db.electronics.getIndexes()

#
db.electronics.count({"type":"laptop"})

#
db.electronics.count({"screen size": 6},{"type":"smart phone"})
db.electronics.find({"screen size": 6},{"type":"smart phone"})

db.electronics.aggregate([
{
    "$group":{
        "_id":"$type",
        "average":{"$avg":"$screen size"}
        }
}
])



mongoexport -u root -p MTQyNDQta2l6aXRv --authenticationDatabase admin --db catalog --collection electronics --out catalog.json
mongoexport -u root -p MTQyNDQta2l6aXRv --authenticationDatabase admin --db catalog --collection electronics --out electronics.csv --type=csv --fields _id,type,model