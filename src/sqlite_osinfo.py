#!/usr/bin/env python3
##/var/ossec/framework/python/bin/python3 /home/wazuh-user/syscollector-report/src/sqlite.py

import os
import sqlite3

def check_db_access(db_path):
    return os.path.isfile(db_path) and os.access(db_path, os.R_OK)

def show_osinfo(db_path):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM dbsync_osinfo")
        osinfo = cursor.fetchall()
        if osinfo:
            print("Tables in the osinfo database:")
            for row in osinfo:
                print(row)
        else:
            print("No osinfo data found in the database.")
        conn.close()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

def main():
    #db_path = os.path.expanduser("~/410.db")
    db_path = os.path.expanduser("/var/ossec/queue/syscollector/db/local.db")
    if check_db_access(db_path):
        print("Database file is accessible.")
        show_osinfo(db_path)
    else:
        print("Database file is not accessible.")

if __name__ == "__main__":
    main()