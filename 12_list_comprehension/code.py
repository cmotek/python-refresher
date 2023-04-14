#numbers = [1, 3, 5]
#doubled = [x * 2 for x in numbers]
#print(doubled)

friends = ["Sam", "Samantha", "Saurabh"]
starts_s = [friend for friend in friends if friend.startswith("S")]

print(friends)
print(starts_s)
print(friends is starts_s)
print(friends[0] is starts_s[0])
print(id(friends[0]), id(starts_s[0]))
print("friends: ", id(friends), "starts_s:", id(starts_s))

