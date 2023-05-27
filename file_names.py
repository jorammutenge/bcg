import os

def main():
    folder_path = 'data'
    filenames = get_csv_filenames(folder_path)
    print(filenames)

def get_csv_filenames(folder_path):
    csv_filenames = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.csv'):
            name = os.path.splitext(filename)[0]  # Remove the file extension
            csv_filenames.append(name)
    return csv_filenames

if __name__ == '__main__':
    main()
