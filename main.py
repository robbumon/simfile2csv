import os
import csv
import simfile
import tkinter as tk
from tkinter import filedialog
from pathlib import Path
from simfile.notes import NoteData
from simfile.notes.count import *


class ChartData:
    def __init__(self):
        self.b = '-'
        self.bn = 0
        self.e = '-'
        self.en = 0
        self.m = '-'
        self.mn = 0
        self.h = '-'
        self.hn = 0
        self.c = '-'
        self.cn = 0

    def AddChartMeter(self, chart, meter):
        self.c = meter


def get_folder_dialog():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askdirectory()
    return file_path


if __name__ == '__main__':
    _path = get_folder_dialog()
    with open('songlist.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Pack', 'Song', 'Artist', 'StepArtist',
                      'BPM', 'Challenge', 'C-Steps', 'Hard', 'H-Steps',
                      'Medium', 'M-Steps', 'Easy', 'E-Steps', 'Beginner', 'B-Steps']
        output = csv.DictWriter(csvfile, delimiter='\t', fieldnames=fieldnames)
        output.writeheader()
        for (dirpath, dirnames, filenames) in os.walk(_path):
            for f in filenames:
                smPath = os.path.join(dirpath, f)
                FileExtension = os.path.splitext(smPath)[1]
                if FileExtension == '.sm':
                    sim = simfile.open(os.path.join(dirpath, f))
                    Pack = os.path.basename(Path(smPath).parents[1])

                    cb = ChartData()
                    for (chart) in sim.charts:
                        if chart.difficulty == 'Beginner':
                            cb.b = chart.meter
                            cb.bn = count_steps(NoteData(chart))
                        if chart.difficulty == 'Easy':
                            cb.e = chart.meter
                            cb.en = count_steps(NoteData(chart))
                        if chart.difficulty == 'Medium':
                            cb.m = chart.meter
                            cb.mn = count_steps(NoteData(chart))
                        if chart.difficulty == 'Hard':
                            cb.h = chart.meter
                            cb.hn = count_steps(NoteData(chart))
                        if chart.difficulty == 'Challenge':
                            cb.c = chart.meter
                            cb.cn = count_steps(NoteData(chart))

                    output.writerow({
                        'Pack': Pack,
                        'Song': sim.title,
                        'Artist': sim.artist,
                        'StepArtist': sim.credit,
                        'BPM': sim.displaybpm,
                        'Challenge': cb.c,
                        'C-Steps': cb.cn,
                        'Hard': cb.h,
                        'H-Steps': cb.hn,
                        'Medium': cb.m,
                        'M-Steps': cb.mn,
                        'Easy': cb.e,
                        'E-Steps': cb.en,
                        'Beginner': cb.b,
                        'B-Steps': cb.bn
                    })

