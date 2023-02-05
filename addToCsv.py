import extractAllData as ead
import csv

data_to_append=ead.all_data()

file = open('result.csv', 'a', newline='')
writer=csv.writer(file)

writer.writerows(data_to_append)
file.close()


