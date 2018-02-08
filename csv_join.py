"""
Test the join of two csv files
"""

import csv

def csv_table(file_name):
    """.

    Input: file in csv format
    Output: csv table in a list of lists, each element of the row is in a list [[r1_c1,r1_c2,...],[r2_c1,r2_c2,...]..]
    """

    f_handler = open(file_name)
    csv_table = []
    csv_reader = csv.reader(f_handler, delimiter=',')

    for row in csv_reader:
        csv_table.append(row)

    return csv_table

def make_dict(table, key_col):
    """.

    Create a dictionary that has as key the value of the column 'key_col' and as value
    the row without the value of the key
    """

    dic = { row[key_col] : row1[0:key_col]+row1[key_col+1:] for (row,row1) in zip(table,table) }

    return dic

def join_dict(dic1,dic2):
    """.

    Given two dictionaries, search for the key in both of them and in that case perform the join
    """
    print(type(dic1))
    l_row = []
    l_tab = []
    for key in dic1.keys():
        if dic2.has_key(key):
            l_row.append(key)
            l_row = l_row + dic1[key]+dic2[key]
            l_tab.append(l_row)
            l_row = []

    return(l_tab)

def save_csv_file(csv_list,	filename):
    """.

    Save the given list in a csv file
    """

    # f_handler = open(filename,'w',newline='')  # python 3 remove blank lines
    f_handler = open(filename, 'wb') # python 2 remove blank lines
    csv_file = csv.writer(f_handler, delimiter=',')
    csv_file.writerows(csv_list)

    return 1


csv_list_1 = csv_table('cancer_risk_trimmed_solution.csv')
csv_list_2 = csv_table('USA_Counties_with_FIPS_and_centers.csv')

csv_key_1 = 2
csv_key_2 = 0

csv_dict_1 = make_dict(csv_list_1,csv_key_1)
csv_dict_2 = make_dict(csv_list_2,csv_key_2)

# print(csv_dict_1)
# print(csv_dict_2)

csv_list3 = join_dict(csv_dict_1,csv_dict_2)

save_csv_file(csv_list3,'joined.csv')
