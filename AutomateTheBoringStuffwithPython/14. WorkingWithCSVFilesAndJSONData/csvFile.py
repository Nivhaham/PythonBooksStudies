import csv


def csvReadExample():
    with open('username.csv') as usernameFile:
        data = csv.reader(usernameFile)
        data_list = list(data)
        print(data_list)
        for i, row in enumerate(data_list):
            print(f"Row# {i+1} {row}")

def csvWriteExample():
    with open('output.csv', 'w', newline='') as outputFile:
        outputWriter = csv.writer(outputFile)
        outputWriter.writerow(['some','data','is','written'])
