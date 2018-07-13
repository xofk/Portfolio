import os, postgres
# Taking place within the most internal ring of the child branches. Current location is the exact as TIGER2010.
db = postgres.pkl_connect("C:\\Users\\user\\Documents\\python\\itg.pkl", "tigerfiles")
PATH = "D:\\Documents\\TigerFiles\\TIGER2010"


def main():
    dir_list = get_dirlist(PATH)
    for dir in dir_list:
        test = db.query("select count(*) from information_schema."
                        "schemata where schema_name = '{}'".format(
            dir.lower()
        ))
        print(len(test))
        if len(test) == 0:
            sql1 = "CREATE SCHEMA {}".format(dir)
            db.execute(sql1)
            sql2 = "INSERT INTO logs.schema_create (schema_name, date) " \
                   "VALUES " \
                   "('{}', now())".format(dir)
            db.execute(sql2)


def get_dirlist(path):
    list = os.listdir(path)
    return list

if __name__ == '__main__':
    main()