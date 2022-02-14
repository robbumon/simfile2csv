import os
import csv
import simfile
import tkinter as tk
from tkinter import filedialog
from pathlib import Path


class chartdata:
    def __init__(self, b, e, m, h, c):
        self.b = b
        self.e = e
        self.m = m
        self.h = h
        self.c = c


def get_folder_dialog():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askdirectory()
    return file_path


if __name__ == '__main__':
    _path = get_folder_dialog()
    with open('songlist.csv','w',encoding='utf-8') as csvfile:
        output = csv.writer(csvfile, delimiter='\t')
        output.writerow(['Pack', 'Song', 'Artist', 'BPM', 'Challenge', 'Hard', 'Medium', 'Easy', 'Beginner'])
        for (dirpath, dirnames, filenames) in os.walk(_path):
            for f in filenames:
                smPath = os.path.join(dirpath, f)
                FileExtension = os.path.splitext(smPath)[1]
                if FileExtension == '.sm':
                    sim = simfile.open(os.path.join(dirpath, f))
                    Pack = os.path.basename(Path(smPath).parents[1])

                    cb = chartdata('-', '-', '-', '-', '-')
                    for (chart) in sim.charts:
                        if chart.difficulty == 'Beginner':
                            cb.b = chart.meter
                        if chart.difficulty == 'Easy':
                            cb.e = chart.meter
                        if chart.difficulty == 'Medium':
                            cb.m = chart.meter
                        if chart.difficulty == 'Hard':
                            cb.h = chart.meter
                        if chart.difficulty == 'Challenge':
                            cb.c = chart.meter

                    output.writerow([Pack, sim.title, sim.artist, sim.displaybpm, cb.c, cb.h, cb.m, cb.e, cb.b])

