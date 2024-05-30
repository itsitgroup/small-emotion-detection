from sklearn.preprocessing import LabelEncoder

labels = {
    'female_angry': 0,
    'female_calm': 1,
    'female_fearful': 2,
    'female_happy': 3,
    'female_sad': 4,
    'male_angry': 5,
    'male_calm': 6,
    'male_fearful': 7,
    'male_happy': 8,
    'male_sad': 9
}

lb = LabelEncoder()
lb.fit(list(labels.values()))

class_mapping = {
    'Angry': 0,
    'Calm': 1,
    'Fearful': 2,
    'Happy': 3,
    'Sad': 4
}
