import argparse

def main():
    parser = argparse.ArgumentParser(description='sample')
    parser.add_argument('--folder', '-i')
    parser.add_argument('--size', '-s', type=int, default=28)
    args = parser.parse_args()
    X_train, X_test, y_train, y_test = my_load_data(args.folder, args.size)

    # 確認
    print('X_train',X_train)
    print('y_train',y_train)
