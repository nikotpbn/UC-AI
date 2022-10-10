# Third Party
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import DistanceMetric
import time

# Own
import load_data
import generate_html

# Load data
data = load_data.load()
data = data.drop(['ID', 'TITLE', 'SUBTITLE', 'DESC', 'IMG_URI'], axis=1)

# Separate target from data
y = data['EXHIBITION']
# data = data.drop(['EXHIBITION'], axis=1)

# Materials data
INK = []  # id 1
PENCIL = []  # id 2
DIGITAL = []  # id 3
WATERCOLOR = []  # id 21
COLORED_PENCILS = []  # id 22
ACRYLICS = []  # id 28

for i, obj in data.iterrows():
    if 1 in obj['TAGS']:
        INK.append(1)
    else:
        INK.append(0)

    if 2 in obj['TAGS']:
        PENCIL.append(1)
    else:
        PENCIL.append(0)

    if 3 in obj['TAGS']:
        DIGITAL.append(1)
    else:
        DIGITAL.append(0)

    if 21 in obj['TAGS']:
        WATERCOLOR.append(1)
    else:
        WATERCOLOR.append(0)

    if 22 in obj['TAGS']:
        COLORED_PENCILS.append(1)
    else:
        COLORED_PENCILS.append(0)

    if 28 in obj['TAGS']:
        ACRYLICS.append(1)
    else:
        ACRYLICS.append(0)

# Add new data to dataframe
data['PENCIL'] = PENCIL
data['WATERCOLOR'] = WATERCOLOR

# Color data
RED = []  # id 11
ORANGE = []  # id 12
YELLOW = []  # id 13
GREEN = []  # id 14
CYAN = []  # id 15
BLUE = []  # id 16
VIOLET = []  # id 17
BLACK = []  # id 18
WHITE = []  # id 19
BROWN = []  # id 23

# Build new data arrays
for i, obj in data.iterrows():
    # Check red color tag
    if 11 in obj['TAGS']:
        RED.append(1)
    else:
        RED.append(0)

    # Check orange color tag
    if 12 in obj['TAGS']:
        ORANGE.append(1)
    else:
        ORANGE.append(0)

    # Check yellow color tag
    if 13 in obj['TAGS']:
        YELLOW.append(1)
    else:
        YELLOW.append(0)

    # Check green color tag
    if 14 in obj['TAGS']:
        GREEN.append(1)
    else:
        GREEN.append(0)

    # Check cyan color tag (15)
    if 15 in obj['TAGS']:
        CYAN.append(1)
    else:
        CYAN.append(0)

    # Check blue color tag (16)
    if 16 in obj['TAGS']:
        BLUE.append(1)
    else:
        BLUE.append(0)

    # Check violet color tag (17)
    if 17 in obj['TAGS']:
        VIOLET.append(1)
    else:
        VIOLET.append(0)

    # Check black color tag (18)
    if 18 in obj['TAGS']:
        BLACK.append(1)
    else:
        BLACK.append(0)

    # Check white color tag (19)
    if 19 in obj['TAGS']:
        WHITE.append(1)
    else:
        WHITE.append(0)

    # Check brown color tag (23)
    if 23 in obj['TAGS']:
        BROWN.append(1)
    else:
        BROWN.append(0)

# Add new data to dataframe
data['RED'] = RED
data['ORANGE'] = ORANGE
data['YELLOW'] = YELLOW
data['GREEN'] = GREEN
data['CYAN'] = CYAN
data['BLUE'] = BLUE
data['VIOLET'] = VIOLET
data['BLACK'] = BLACK
data['WHITE'] = WHITE
data['BROWN'] = BROWN

# TODO: ADD inspiration and materials?
#     4      Marvel Comics
#     5          DC Comics
#     6    H. P. Lovecraft
#   20       Image Comics
#   29  Dark House Comics
#   30    Dynamite Comics

INSPIRATION = []
for i, obj in data.iterrows():
    if 4 in obj['TAGS']:
        INSPIRATION.append(4)

    elif 5 in obj['TAGS']:
        INSPIRATION.append(5)

    elif 6 in obj['TAGS']:
        INSPIRATION.append(6)

    elif 20 in obj['TAGS']:
        INSPIRATION.append(20)

    elif 29 in obj['TAGS']:
        INSPIRATION.append(29)

    elif 30 in obj['TAGS']:
        INSPIRATION.append(30)

# Add new data to data frame
data['INSPIRATION'] = INSPIRATION

# Remove list of TAGS from dataframe
data = data.drop(['TAGS'], axis=1)
data = data.drop(['EXHIBITION'], axis=1)

# Create and train the classifier
# Metrics: euclidean | manhattan | chebyshev | minkowski (default) | cityblock | cosine(best)
neigh = KNeighborsClassifier(n_neighbors=5, metric='cosine')
classifier = neigh.fit(data, y)

# Find the 5 nearest neighbors of all objects
neigh_dist, neigh_inx = classifier.kneighbors(n_neighbors=5)
ids = neigh_inx + 1

# Reload data
data = load_data.load()
# Concatenate new information
data['SIMILAR ARTS'] = ids.tolist()

# Results for Philip Tan selected arts
generate_html.similar_items(data, 86, 'Philip Tan - KNN - Colored Image')
time.sleep(2)
generate_html.similar_items(data, 41, 'Philip Tan - KNN - Black and White Image')

# Results for Michael Sta. Maria selected arts
time.sleep(2)
generate_html.similar_items(data, 130, 'Michael Sta. M. - KNN - Colored Image')
time.sleep(2)
generate_html.similar_items(data, 138, 'Michael Sta. M. - KNN - Black and White Image')

# Results for Diogo Ferreira selected arts
time.sleep(2)
generate_html.similar_items(data, 0, 'Diogo Ferreira - KNN - Colored Image')
time.sleep(2)
generate_html.similar_items(data, 10, 'Diogo Ferreira - KNN - Black and White Image')

# Results for Jim Lee selected arts
time.sleep(2)
generate_html.similar_items(data, 240, 'Jim Lee - KNN - Colored Image')
time.sleep(2)
generate_html.similar_items(data, 181, 'Jim Lee - KNN - Black and White Image')
