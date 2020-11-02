#Lang Tuang | Nov1st,2020 | Week10 Part II

import sqlite3 as light
import sys

try:
  conn = sqlite3.connect('pets.db')

  with conn:
    curs = conn.cursor()
        curs.execute("INSERT INTO person(id, first_name,last_name,age) VALUES(1,'James','Smith', 41);")
        curs.execute("INSERT INTO person(id, first_name,last_name,age) VALUES(2, 'Diana', 'Greene', 23);")
        curs.execute("INSERT INTO person(id, first_name,last_name,age) VALUES(3, 'Sara', 'White', 27);")
        curs.execute("INSERT INTO person(id, first_name,last_name,age) VALUES(4, 'William','Gibson', 23);")

        curs.execute("INSERT INTO pet(id, name, breed, age, dead) VALUES(1, 'Rusty', 'Dalmation', 4, 1);")
        curs.execute("INSERT INTO pet(id, name, breed, age, dead) VALUES(2, 'Bella', 'Alaskan Malamute', 3, 0);")
        curs.execute("INSERT INTO pet(id, name, breed, age, dead) VALUES(3, 'Max', 'Cocker Spaniel', 1, 0);")
        curs.execute("INSERT INTO pet(id, name, breed, age, dead) VALUES(4, 'Rocky', 'Beagle', 7, 0);")
        curs.execute("INSERT INTO pet(id, name, breed, age, dead) VALUES(5, 'Rufus', 'Cocker Spaniel', 1, 0);")
        curs.execute("INSERT INTO pet(id, name, breed, age, dead) VALUES(6, 'Spot', 'Bloodhound', 2, 1);")

        curs.execute("INSERT INTO person_pet(person_id, pet_id) VALUES(1, 1);")
        curs.execute("INSERT INTO person_pet(person_id, pet_id) VALUES(1, 2);")
        curs.execute("INSERT INTO person_pet(person_id, pet_id) VALUES(2, 3);")
        curs.execute("INSERT INTO person_pet(person_id, pet_id) VALUES(2, 4);")
        curs.execute("INSERT INTO person_pet(person_id, pet_id) VALUES(3, 5);")
        curs.execute("INSERT INTO person_pet(person_id, pet_id) VALUES(4, 6);")

except light.Error, error:
  print "Error occurs:Will Exit! "
  sys.exit(1)

finally:
  if conn:
    conn.close()
