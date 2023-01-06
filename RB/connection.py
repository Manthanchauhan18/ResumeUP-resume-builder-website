import pymongo


class Mongopy:

    @staticmethod
    def connect(collec):
        print("Welcome......")
        client = pymongo.MongoClient("mongodb://127.0.0.1/27017")
        # Define DB Name
        db = client['ResumeBuilder']
        # Define Collection
        col = db[collec]
        print("Connected...")
        return col

    @staticmethod
    def save_to_db(fm, col):
        data = {
            "name": fm['name'],
            "email": fm['email'],
            "objective": fm['objective'],
            "prof": fm['prof'],
            "college": fm['college'],
            # "college_location": fm['college_location'],
            "college_join": fm['college_join'],
            "college_leave": fm['college_leave'],
            "college_field": fm['college_field'],
            "college_per": fm['college_per'],
            "school_12": fm['school_12'],
            # "school_12_location": fm['school_12_location'],
            "school_12_join": fm['school_12_join'],
            "school_12_leave": fm['school_12_leave'],
            "school_12_field": fm['school_12_field'],
            "school_12_per": fm['school_12_per'],
            "school_10": fm['school_10'],
            # "school_10_location": fm['school_10_location'],
            "school_10_join": fm['school_10_join'],
            "school_10_leave": fm['school_10_leave'],
            "school_10_per": fm['school_10_per'],
            "skill_name_1": fm['skill_name_1'],
            "skill_1": fm['skill_1'],
            "skill_name_2": fm['skill_name_2'],
            "skill_2": fm['skill_2'],
            "skill_name_3": fm['skill_name_3'],
            "skill_3": fm['skill_3'],
            "project": fm['project'],
            "project_obj": fm['project_obj'],
            "project_tech": fm['project_tech']
        }
        col.insert_one(data)

    @staticmethod
    def drop_dbs(dbs):
        print("Welcome......")
        client = pymongo.MongoClient("mongodb://127.0.0.1/27017")
        client.drop_database(dbs)

        print("Connected...")

    @staticmethod
    def getall(collection):
        alldoc = collection.find()
        for item in alldoc:
            print(f"Name :: {item['name']}  Age :: {item['age']}  Minor :: {item['minor']}")


# m = Mongopy()
# col = m.connect('name')
# data1 = {
#     "cv_id": id,
#     "name": fm['name'].value(),
#     "email": fm['email'].value(),
#     "objective": fm['objective'].value(),
#     "prof": fm['prof'].value(),
#     "college": fm['college'].value(),
#     # "college_location": fm['college_location'],
#     "college_join": fm['college_join'].value(),
#     "college_leave": fm['college_leave'].value(),
#     "college_field": fm['college_field'].value(),
#     "college_per": fm['college_per'].value(),
#     "school_12": fm['school_12'].value(),
#     # "school_12_location":fm['school_12_location'],
#     "school_12_join": fm['school_12_join'].value(),
#     "school_12_leave": fm['school_12_leave'].value(),
#     "school_12_field": fm['school_12_field'].value(),
#     "school_12_per": fm['school_12_per'].value(),
#     "school_10": fm['school_10'].value(),
#     # "school_10_location":fm['school_10_location'],
#     "school_10_join": fm['school_10_join'].value(),
#     "school_10_leave": fm['school_10_leave'].value(),
#     "school_10_per": fm['school_10_per'].value(),
#     "skill_name_1": fm['skill_name_1'].value(),
#     "skill_1": fm['skill_1'].value(),
#     "skill_name_2": fm['skill_name_2'].value(),
#     "skill_2": fm['skill_2'].value(),
#     "skill_name_3": fm['skill_name_3'].value(),
#     "skill_3": fm['skill_3'].value(),
#     "project": fm['project'].value(),
#     "project_obj": fm['project_obj'].value(),
#     "project_tech": fm['project_tech'].value()
# }
# col.insert_one(data1)
# Mongopy.save_to_db(data1, col)
