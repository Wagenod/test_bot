import os
import sqlite3
from dotenv import load_dotenv
from gdrive import GoogleDriveController

load_dotenv()


class Database:
    def __init__(self):
        self.drive_controller = GoogleDriveController()
        self.db_cursor = None
        self.db_conn = None

    def __enter__(self):
        self.drive_controller.download_db()
        self.db_conn = sqlite3.connect(os.getenv("DB_NAME"))
        self.db_cursor = self.db_conn.cursor()
        return self.db_cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.db_cursor.close()
        self.db_conn.commit()
        self.db_conn.close()
        self.drive_controller.upload_db()
        os.remove(os.getenv("DB_NAME"))

