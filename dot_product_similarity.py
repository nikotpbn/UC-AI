import numpy as np
import load_data

# Load data
data = load_data.load()

# Allocate memory for the similarity data
similarity_matrix = np.zeros((data.shape[0], data.shape[0]), dtype=int)

# Iterate through all objects
for i, obj in data.iterrows():

    # Fetch information of an object
    row_index = i
    obj_id = obj['ID']
    obj_type = obj['TYPE']
    obj_exhibition = obj['EXHIBITION']
    obj_tags = obj['TAGS']

    # Second loop through all objects (for comparison)
    for j, obj2 in data.iterrows():

        # Fetch information of an second object
        column_index = j
        obj2_id = obj2['ID']
        obj2_type = obj2['TYPE']
        obj2_exhibition = obj2['EXHIBITION']
        obj2_tags = obj2['TAGS']

        # Check if it is the same object
        if i == j:
            similarity_matrix[row_index][column_index] = 0

        # If its not the same object then calculate the similarity between them by comparing the features
        else:
            # Check if objects are the same type
            if obj_type == obj2_type:
                similarity_matrix[row_index][column_index] += 1

            # Check if objects are on the same exhibition
            if obj_exhibition == obj2_exhibition:
                similarity_matrix[row_index][column_index] += 1

            # Find tags contained in both objects
            similar_tags = np.intersect1d(obj_tags, obj2_tags)
            similarity_matrix[row_index][column_index] += len(similar_tags)

# TODO: HOW TO MAKE SURE IDS ARE CORRECT IF THEY ARE NOT INDEX+1?
new_data_column = []
for i in range(0, data.shape[0]):
    # Find the 5 maximum values in the matrix row array
    ind = np.argpartition(similarity_matrix[i], -5)[-5:]

    # Sort values from smallest to biggest
    sorted_indexes = ind[np.argsort(similarity_matrix[i][ind])]

    # Reverse the order
    most_similar_indexes = list(reversed(sorted_indexes))

    # Find correct IDs of the objects
    most_similar_ids = [x+1 for x in most_similar_indexes]

    # Append the data to a list
    new_data_column.append(most_similar_ids)

# Concatenate the new column to the main dataframe
data['SIMILAR ARTS'] = new_data_column
print(data)

# # Object to test (index=0, id=1)
# print(similarity_matrix[0])
#
# # Get indexes of the 5 maximum values
# ind = np.argpartition(similarity_matrix[0], -5)[-5:]
# print(ind)
# print(similarity_matrix[0][ind])
#
# # sort
# print("------------------sorted---------------------")
# sorted_indexes = ind[np.argsort(similarity_matrix[0][ind])]
# sorted_values = similarity_matrix[0][sorted_indexes]
# print(sorted_indexes)
# print(sorted_values)
#
# # reversed sort
# print("------------------most similar---------------------")
# most_similar_indexes = list(reversed(sorted_indexes))
# most_similar_values = similarity_matrix[0][most_similar_indexes]
# print(most_similar_indexes)
# print(most_similar_values)



