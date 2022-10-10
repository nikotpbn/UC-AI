import pandas as pd
import numpy as np


# Datasets:
# 1: Long Descriptions
# 2: Structured Descriptions
def load():
    arts = None
    tags = None
    exhibitions = None
    art_tags = None
    exhibition_arts = None

    # id, title, subtitle, description, image, type, created_at, user_id
    arts = pd.read_json('dataset/portifolio_gallery_art.json')
    tags = pd.read_json('dataset/portifolio_gallery_tag.json')
    exhibitions = pd.read_json('dataset/portifolio_gallery_exhibition.json')
    art_tags = pd.read_json('dataset/portifolio_gallery_art_tag.json')
    exhibition_arts = pd.read_json('dataset/portifolio_gallery_exhibition_art.json')

    year_tags = tags.loc[tags['area'] == 6]
    year_tags = year_tags.drop(['created_at', 'user_id', 'area'], axis=1)

    # Create data variable
    data = {}
    year = 0

    # id, title, subtitle, description, image,, type, created_at, user_id
    for i, row in arts.iterrows():

        # Fetch related tags
        related_tags = art_tags.loc[art_tags['art_id'] == row['id']]
        tag_list = related_tags['tag_id'].tolist()
        tag_list = np.array(tag_list)

        for tag in tag_list:
            if tag in year_tags['id'].tolist():
                year = year_tags.loc[year_tags['id'] == tag]


        # Fetch related exhibition
        related_exhibition = exhibition_arts.loc[exhibition_arts['art_id'] == row['id']]
        exhibition = related_exhibition.iloc[0]['exhibition_id']

        # Fetch related year

        # print("ID: {} | TYPE: {} | EXHIBITION: {} | RELATED TAGS: {}".format(row['id'], row['type'], exhibition, tag_list))
        # Insert data row into the dictionary
        data_row = [row['id'], row['title'], row['subtitle'], row['description'], row['type'], year['name'].item(), exhibition, tag_list, row['image']]
        data[i] = data_row

    # Transform data dictionary into a pandas dataframe
    data_df = pd.DataFrame.from_dict(data, orient='index', columns=['ID', 'TITLE', 'SUBTITLE', 'DESC', 'TYPE', 'YEAR', 'EXHIBITION', 'TAGS', 'IMG_URI'])

    return data_df


def get_color_tags():
    tags = pd.read_json('json/new description/portifolio_gallery_tag.json')
    color_tags = tags.loc[tags['area'] == 5]
    color_tags = color_tags.drop(['area', 'created_at', 'user_id'], axis=1)

    return color_tags


def get_inspiration_tags():
    tags = pd.read_json('json/new description/portifolio_gallery_tag.json')
    inspiration_tags = tags.loc[tags['area'] == 2]
    inspiration_tags = inspiration_tags.drop(['area', 'created_at', 'user_id'], axis=1)

    return inspiration_tags


