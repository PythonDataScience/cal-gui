import tkinter as tk
import argparse
from calendar import monthrange


def cal(year,month):
        root = tk.Tk()
        daynames = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

        firstday, totaldays = monthrange(year,month)

        r = 0
        for c in range(7):
             # font: (family, size, style)
             label = tk.Label(master = root, text = daynames[c], font = ('',30,''), padx = 10, relief = tk.RAISED)
             label.grid(row = r, column = c)

        for d in range(totaldays):
             c = (firstday + d) % 7
             r = (firstday + d) // 7 + 1
             label = tk.Label(master = root, text = str(d+1), font = ('',30,''))
             label.grid(row = r, column = c)
        root.mainloop()

if __name__ == '__main__':
        parser = argparse.ArgumentParser(description = 'GUI monthly calendar(cal.py)')
        parser.add_argument('-y','--year', help = 'year, e.g. 2000', required = True)
        parser.add_argument('-m','--month', help = 'month, e.g 12, for December', required = True)
        args = parser.parse_args()
        year = int(args.year)
        month = int(args.month)
        cal(year,month)
