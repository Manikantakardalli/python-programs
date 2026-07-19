print("===== Movie Recommendation =====")

user1 = set(input("Enter movies watched by User 1: ").split())
user2 = set(input("Enter movies watched by User 2: ").split())

print("\nCommon Movies:")
print(user1.intersection(user2))

print("\nRecommend to User 1:")
print(user2.difference(user1))

print("\nRecommend to User 2:")
print(user1.difference(user2))

print("\nmovies watched by both users:")
print(user1.union(user2))