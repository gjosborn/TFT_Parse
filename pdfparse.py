import camelot


# This is reading in the table 'Approximate Losses in Muzzle Velocity
# Due to the formatting of the tables, each one will have to be dealt with individually,
# but it should carry over between different TFTs


# tables[0].to_csv('testCSV.csv')

def read_approx_loss(filename):
    approx_loss = camelot.read_pdf(filename, pages='28', flavor='stream')
    print(approx_loss[0])
    table_df = approx_loss[0].df[2:]
    for index, value in enumerate(table_df):
        print()
    # print(table_df.to_string(index=True))


if __name__ == '__main__':
    tft_file = 'FT 155-AM-3 w.changes1,2.pdf'
    read_approx_loss(tft_file)
