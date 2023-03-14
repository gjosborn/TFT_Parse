import tkinter

import camelot


# This is reading in the table 'Approximate Losses in Muzzle Velocity
# Due to the formatting of the tables, each one will have to be dealt with individually,
# but it should carry over between different TFTs


# tables[0].to_csv('testCSV.csv')
import pandas
import matplotlib.pyplot as plt
from tkinter import *

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def read_approx_loss(filename):
    approx_loss = camelot.read_pdf(filename, pages='28', flavor='stream')
    # print(approx_loss[0])
    table_df = approx_loss[0].df[2:9]
    # print(table_df.to_string(index=True))
    headers = pandas.DataFrame
    print(table_df[0:5])

def read_exp(filename):
    approx_loss = camelot.read_pdf(filename, pages='28', flavor='stream')
    table_df = approx_loss[0].df
    print(table_df)
    camelot.plot(approx_loss[0], kind='textedge').show()

if __name__ == '__main__':

    filename = 'FT 155-AM-3 w.changes1,2.pdf'
    # read_exp(tft_file)
    # read_approx_loss(tft_file)


    # Creating a Tkinter window
    window = Tk()
    window.title('Plotting in Tkinter')
    window.geometry("500x500")

    approx_loss = camelot.read_pdf(filename, pages='28', flavor='stream')
    table_df = approx_loss[0].df
    camPlot = camelot.plot(approx_loss[0], kind='textedge')
    # plt.show(block=True)

    canvas = FigureCanvasTkAgg(camPlot, master=window)
    canvas.get_tk_widget().pack(side=tkinter.LEFT, fill=tkinter.BOTH)
    canvas.draw()
    window.mainloop()


# Next Step is to create a tkinter window that shows the textedge plot of the page and allows the user to pick the
# table, area and the column separators and allow the user to process the table and store it as a pkl with a name of
# their choosing
