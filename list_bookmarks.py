import os
import tempfile
import shutil
import sqlite3

from config import *

firefox_database = os.path.join(os.path.expanduser(FIREFOX_PROFILE_DIR), "places.sqlite")

# Firefox keeps the database locked, it needs to be copied to a temporary file
temp_database = tempfile.NamedTemporaryFile()
shutil.copyfile(firefox_database, temp_database.name)

con = sqlite3.connect(temp_database.name)
cur = con.cursor()

cur.execute("SELECT moz_bookmarks.title, moz_places.title, url FROM moz_bookmarks INNER JOIN moz_places ON moz_bookmarks.fk == moz_places.id;")

for line in cur:
    print(f'{line[0] + " " if line[0] else ""}{line[1]+ " " if line[1] else ""}{line[2]}')

con.close()
temp_database.close()
