import time
import load_data
import numpy as np
import generate_html

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
    obj_tags = obj['TAGS']
    obj_exhibition = obj['EXHIBITION']

    # Second loop through all objects (for comparison)
    for j, obj2 in data.iterrows():

        # Fetch information of an second object
        column_index = j
        obj2_id = obj2['ID']
        obj2_type = obj2['TYPE']
        obj2_tags = obj2['TAGS']
        obj2_exhibition = obj2['EXHIBITION']

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

            # Find tags contained in both objects (includes: year, colors, materials, etc.)
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

# Results for Philip Tan selected arts
generate_html.similar_items(data, 86, 'Philip Tan - Dot Product - Colored Image')
time.sleep(2)
generate_html.similar_items(data, 41, 'Philip Tan - Dot Product - Black and White Image')

# Results for Michael Sta. Maria selected arts
time.sleep(2)
generate_html.similar_items(data, 130, 'Michael Sta. M. - Dot Product - Colored Image')
time.sleep(2)
generate_html.similar_items(data, 138, 'Michael Sta. M. - Dot Product - Black and White Image')

# Results for Diogo Ferreira selected arts
time.sleep(2)
generate_html.similar_items(data, 0, 'Diogo Ferreira - Dot Product - Colored Image')
time.sleep(2)
generate_html.similar_items(data, 10, 'Diogo Ferreira - Dot Product - Black and White Image')

# Results for Jim Lee selected arts
time.sleep(2)
generate_html.similar_items(data, 240, 'Jim Lee - Dot Product - Colored Image')
time.sleep(2)
generate_html.similar_items(data, 181, 'Jim Lee - Dot Product - Black and White Image')
