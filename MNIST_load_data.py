def my_load_data(folder_str, size):
    print('load_dataset...')
    folders = folder_str.split('__')
    X = []
    Y = []
    for index, fol_name in enumerate(folders):
        files = glob.glob(fol_name + '/*.jpg')
        for file in files:
            image = Image.open(file)
            image = image.resize((size, size))
            image = image.convert('L')
            data = np.asarray(image)
            X.append(data)
            Y.append(index)
    X = np.array(X)
    Y = np.array(Y)
    oh_encoder = OneHotEncoder(categories='auto', sparse=False)
    onehot = oh_encoder.fit_transform(pd.DataFrame(Y))
    X_train, X_test, y_train, y_test = train_test_split(X, onehot, test_size=0.2)
    return X_train, X_test, y_train, y_test