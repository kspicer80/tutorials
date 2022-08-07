import sqlite_practice

#sqlite_practice.add_one('Neville', 'Longbottom', 'nl@hogwarts.com')
#sqlite_practice.delete_one('3')

stuff = [
    ('Draco', 'Malfoy', 'dm@hogwarts.com'),
    ('Luna', 'Lovegood', 'll@hogwarts.com')
]

#sqlite_practice.add_many(stuff)
sqlite_practice.email_lookup('ll@hogwarts.com')
#sqlite_practice.show_all()
