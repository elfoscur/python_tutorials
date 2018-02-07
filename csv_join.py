""".

PLay with csv files and join them
"""

import csv


def csv_table(csv_file_name):
    """.

    Given in input a csv file and return a dictionary of rows
    """
    csv_table = {}
    f_handler = open(csv_file_name)
    csv_reader = csv.reader(f_handler, delimiter=',')
    i = 0
    for row in csv_reader:
        csv_table[i] = row
        i += 1  # increment i by 1
    return csv_table


csv1 = csv_table('USA_Counties_with_FIPS_and_centers.csv')
# print(csv1)
#
# csv1_len = len(csv1)
# idx = range(0, csv1_len)
#
# csv_dict = {idx: row for (idx, row) in zip(idx, csv1)}  # from list to dict

print(csv1)
