import pandas as pd
import numpy as np


def load():
    # id, title, subtitle, description, image, type, created_at, user_id
    arts = pd.read_json('json/portifolio_gallery_art.json')
    tags = pd.read_json('json/portifolio_gallery_tag.json')
    exhibitions = pd.read_json('json/portifolio_gallery_exhibition.json')
    art_tags = pd.read_json('json/portifolio_gallery_art_tag.json')
    exhibition_arts = pd.read_json('json/portifolio_gallery_exhibition_art.json')

    # Create data variable
    data = {}

    # id, title, subtitle, description, image,, type, created_at, user_id
    for i, row in arts.iterrows():

        # Fetch related tags
        related_tags = art_tags.loc[art_tags['art_id'] == row['id']]
        tag_list = related_tags['tag_id'].tolist()
        tag_list = np.array(tag_list)

        # Fetch related exhibition
        related_exhibition = exhibition_arts.loc[exhibition_arts['art_id'] == row['id']]
        exhibition = related_exhibition.iloc[0]['exhibition_id']

        # print("ID: {} | TYPE: {} | EXHIBITION: {} | RELATED TAGS: {}".format(row['id'], row['type'], exhibition, tag_list))
        # Insert data row into the dictionary
        data_row = [row['id'], row['type'], exhibition, tag_list]
        data[i] = data_row

    # Transform data dictionary into a pandas dataframe
    data_df = pd.DataFrame.from_dict(data, orient='index', columns=['ID', 'TYPE', 'EXHIBITION', 'TAGS'])
    return data_df
    # print(data_df)
