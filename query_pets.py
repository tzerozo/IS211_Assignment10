#Lang Tuang ||NOV1st 2020 || Week10_Part2

import sqlite3 as light
import sys

conn = None

try:
  conn = sqlite3.connect('pets.db')
  curs = conn.curs()

except light.Error, error:
  print "Error occurs:Will Exit! "
  sys.exit(1)

########Ask for PersonID (-1 to exit)
########If person exist: print Person's data & Pet's data until (-1)

personID = None

while personID != -1:
  personID = int(input("Please enter the personID. Type (-1) to stop: "))

  if personID == -1:
    sys.exit(1)

  Query = "SELECT person.first_name,person.last_name,person.age FROM person WHERE id = ?"

  with conn:
    curs.execute(Query,(personID,))
    person_info = curs.fetchone()

  if person_info not None:
    print (" %s %s is %s years old" %(person_info[0],person_info[1],person_info[2]))

    curs.execute("DROP TABLE IF EXISTS PET_PERSON_ID;")
    curs.execute("CREATE TABLE PET_PERSON_ID as SELECT pet_id FROM person_pet WHERE person_id = ?", (personID,))
    curs.execute("SELECT pet.name, pet.breed, pet.age, pet.dead FROM pet JOIN PET_PERSON_ID ON PET_PERSON_ID.pet_id = pet.id;")

    pet_info = curs.fetchall()

    for data in pet_info:
      print(" %s  owned %s, a %s , that was %d years old. " % (person_info[0], pet_info[0], pet_info[1],pet_info[2]))

  else:
    print("Sorry Wrong PersonID. You may try again.")
