'''
Written by Keaten Fox

GOAL:
    The goal of this script is to create a wrapper for psycopg2.

ACTIONS:
    1) Mannually connect to postgreSQL database
    2) Build a pickle connector
    3) Load a pickle connector

    DATABASE OBJECT - The database object creates the psycopg2 cursor and enables single line SQL command functions for
        queries and commands.


'''
import psycopg2
import pickle
import os

def manual_connect():
    db = input("DB Name: ")
    host = input("Host: ")
    user = input("User Name: ")
    pw = input("Password: ")
    os.system("cls")
    db_class = database(db, host, user, pw)
    return db_class


def pkl_connect(file, db):
    dict = pickle.load(open(file, 'rb'))
    db_class = database(db, dict['host'], dict['user'], dict['pw'])
    return db_class


def pkl_create():
    print("Welcome to the DB pickle creator! Please fill out the following:")
    host = input("Host: ")
    user = input("User Name: ")
    pw = input("Password: ")
    export = input("Export Path: ")
    name = input("Pickle Name: ")
    path = "{}\\{}.p".format(export,name)
    dict = {'host': host, 'user': user, 'pw': pw}
    with open(path, 'wb+') as f:
        pickle.dump(dict, f)
    print("Pickle Created Successfully!")

def pkl_read(file):
    dict = pickle.load(open(file, 'rb'))
    print("User: {}".format(dict['user']))
    print("Host: {}".format(dict['host']))
    print("PW: {}".format(dict['pw']))


class database():
    def  __init__(self, db, host, user, pw):
        self.db = db
        self.host = host
        self.user = user
        self.pw = pw

    def connect(self):
        conn = psycopg2.connect(dbname=self.db, host=self.host, user=self.user, password=self.pw)
        cur = conn.cursor()
        return cur, conn

    def query(self, SQL):
        cur,conn=self.connect()
        cur.execute(SQL)
        rows=cur.fetchall()
        cur.close()
        del conn
        return rows

    def execute(self, SQL):
        cur,conn=self.connect()
        cur.execute(SQL)
        conn.commit()
        cur.close()
        del conn


if __name__ == '__main__':
    pkl_create()