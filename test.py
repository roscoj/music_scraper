def make_list(*items):
    return list(items)

def run(page, rows = []):
    if page <= 10:
        rows += make_list(page, page, page)
        print(rows)
        run(page + 1, rows)
    else:
        print('loop has ended')
run(1)



'''
pseudocode

Main function
1. Set if condition

Within if block
1. Call function to create list from input
2. Concatenate this with any previous lists
3. Call main function again with increment

Within else block
1. Call function to create csv file
2. Print message saying csv is complete






'''
