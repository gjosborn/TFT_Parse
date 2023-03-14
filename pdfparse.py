import camelot

# This is reading in the table 'Approximate Losses in Muzzle Velocity
# Due to the formatting of the tables, each one will have to be dealt with individually,
# but it should carry over between different TFTs


import pandas as pd
import matplotlib.pyplot as plt



def read_approx_loss(filename):
    approx_loss = camelot.read_pdf(filename, pages='28', flavor='stream')
    # print(approx_loss[0])
    table_df = approx_loss[0].df[2:9]
    # print(table_df.to_string(index=True))
    # add the headers by grabbing the column headers from the first few rows of the dataframe
    headers = pd.DataFrame
    print(table_df[0:5])


def text_edge_graph(filename):
    approx_loss = camelot.read_pdf(filename, pages='28', flavor='stream')
    table_df = approx_loss[0].df
    camelot.plot(approx_loss[0], kind='textedge')
    plt.show(block=True)


if __name__ == '__main__':
    tft_file = 'FT 155-AM-3 w.changes1,2.pdf'
    read_approx_loss(tft_file)
    text_edge_graph(tft_file)

    # The next step is to use the text_edge graph to more accurately choose table locations by choosing table areas and,
    # column separators.
