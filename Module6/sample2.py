#!/usr/bin/env python3
file = open("student2.dat", "wb")

#file = open("/Applications/XAMPP/xamppfiles/htdocs/3TSY2526_CS0048/Module6/student1.txt", "w")

file.write(b"Hadji Javier")
file.close()

print("File created and data saved.")