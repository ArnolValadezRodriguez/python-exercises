truck = "toyota tacoma"
sedan = "hyundai sonata"
sports_car = "lamborghini diablo"

# 1. 
truck = "toyota tacoma"
make_and_model = truck.split
make = truck.split()[0]
model = truck.split()[1]
truck = {
    "make" : make,
    "model" : model
}
print (truck)

#Other Solution to make dictionary
# truck["make"] = make
# truck["model"] = model
# print (truck)

#Or
# truck = dict("make" = make, "model" = model)
# print (truck)

#This is wrong
#truck = dict(make='toyota', model='tacoma')

# 2.
truck ["make"] = truck ["make"].capitalize()
truck ["model"] = truck ["model"].capitalize()
print(truck)

# 3. 
