import urllib.request
import pandas as pd

path = "C://Users//Jannik/PycharmProjects/test/drehgestell/data/train/"
filenames = ["KLB KRB", "KLB VRB RBSQ", "KLB VRB RBGQ", "VLB LBSQ KRB","VLB LBGQ KRB", "VLB LBSQ VRB RBSQ",  "VLB LBSQ VRB RBGQ", "VLB LBGQ VRB RBSQ", "VLB LBGQ VRB RBGQ"]

i = 0
dataframes = []

for filename in filenames:
    # open file to read
    with open("{0}.csv".format(path + filename), 'r') as csvfile:
        # iterate on all lines
        for line in csvfile:
            splitted_line = line.split(';')
            if splitted_line[0] != '':
                try:
                    data = urllib.request.urlretrieve(splitted_line[0], "train_" + str(i) + ".webp")
                    #df = pd.DataFrame({'image_name': fnames, 'tags': labelled_preds}, columns=['image_name', 'tags'])
                    df = pd.DataFrame({"train_" + str(i) + ',' + filename})
                    dataframes.append(df)
                    print("Image saved for {0}".format(splitted_line[0]))
                    i += 1
                except:
                    print('error')
            else:
                print("No result for {0}".format(splitted_line[0]))

        # create train.csv
        df = pd.concat(dataframes)
        df.to_csv(path + 'train.csv', index=False)
