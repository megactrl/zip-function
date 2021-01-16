 #combine two two lists

movies = ["Inception","The Dark Knight","Interstellar","The Prestige","Batman Begins",]
ratings = [8,8,9,7,7]

new_list = []

for tree in zip(movies,ratings):
    new_list.append(tree)

print(new_list)
