
from dataset import data_set, split_and_save_dataset


FNAME = '../datasets/adult/adult.csv'


if __name__ == '__main__':
    data = data_set(FNAME)
    for key, value in data.items():
        print(key)

    fname = FNAME.split('/')
    fname = fname[-1]
    print('fname -->', fname)

    split_and_save_dataset(data)