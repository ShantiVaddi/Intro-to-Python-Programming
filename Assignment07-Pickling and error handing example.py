# This script describes
# ------------------------------------------------- #
# Title: Lab7-1
# Description: A simple example of Pickling data
# ChangeLog: (Who, When, What)
# <SVaddi>,<8.31.2021>,Created Script
# ------------------------------------------------- #
# Pickling
# Demonstrates pickling and shelving data
import pickle,shelve

# First we create three lists that I plan to pickle and write to a file.
print("Pickling lists.")
category = ["Herbivorous", "Carnivorous", "Omnivorous"]
size = ["big", "medium", "small"]
climate = ["Tropical", "dry", "Polar"]

# Second I open the new file to store the pickled lists
f = open("pickles1.dat","wb")

# Third , I pickle and store the three lists category,size, and climate in the file pickles1.dat using the
# pickle.dump()function
pickle.dump(category, f)
pickle.dump(size, f)
pickle.dump(climate,f)
f.close()

# Reading Data from a file and unpickling it.

print("\nunpickling lists.")
f = open("pickles1.dat", "rb")
category = pickle.load(f)
size = pickle.load(f)
climate = pickle.load(f)

# Finally I print the unpickled lists to prove that the process worked.

print(category)
print(size)
print(climate)
f.close()
# First , I create a shelf, s:

print("\nShelving lists.")
s = shelve.open("pickles2.dat")

# Using a shelf to store Pickled data.

s["category"] = ["Herbivorous", "Carnivorous", "Omnivorous"]
s["size"]= ["big", "medium", "small"]
s["climate"] = ["Tropical", "dry", "Polar"]

# Finally I invoke the sync()method:
s.sync() # make sure data is written
# As we mentioned that the shelf acts like a dictionary, we can randomly access pickled objects from it by supplying a key.
print("\nRetrieving lists from a shelved file:")
print("category -",s["category"])
print("size -",s["size"])
print("climate -",s["climate"])

# Finally , we close the file:
s.close()

input("\n\nPress the enter key to exit.")



