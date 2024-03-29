#!/usr/bin/env python


#############################################################################
##
## Copyright (C) 2012 Riverbank Computing Limited
## Copyright (C) 2012 Digia Plc
## All rights reserved.
##
## This file is part of the PyQtChart examples.
##
## $QT_BEGIN_LICENSE$
## Licensees holding valid Qt Commercial licenses may use this file in
## accordance with the Qt Commercial License Agreement provided with the
## Software or, alternatively, in accordance with the terms contained in
## a written agreement between you and Digia.
## $QT_END_LICENSE$
##
#############################################################################


import sys

from PyQt4.QtChart import (QBarCategoriesAxis, QBarSet, QChart, QChartView,
        QPercentBarSeries)
from PyQt4.QtCore import Qt
from PyQt4.QtGui import QApplication, QMainWindow, QPainter


app = QApplication(sys.argv)

set0 = QBarSet("Jane")
set1 = QBarSet("John")
set2 = QBarSet("Axel")
set3 = QBarSet("Mary")
set4 = QBarSet("Samantha")

set0 << 1 << 2 << 3 << 4 << 5 << 6
set1 << 5 << 0 << 0 << 4 << 0 << 7
set2 << 3 << 5 << 8 << 13 << 8 << 5
set3 << 5 << 6 << 7 << 3 << 4 << 5
set4 << 9 << 7 << 5 << 3 << 1 << 2

series = QPercentBarSeries()
series.append(set0)
series.append(set1)
series.append(set2)
series.append(set3)
series.append(set4)

chart = QChart()
chart.addSeries(series)
chart.setTitle("Simple percentbarchart example")

categories = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
axis = QBarCategoriesAxis()
axis.append(categories)
chart.createDefaultAxes()
chart.setAxisX(axis, series)

chart.legend().setVisible(True)
chart.legend().setAlignment(Qt.AlignBottom)

chartView = QChartView(chart)
chartView.setRenderHint(QPainter.Antialiasing)

window = QMainWindow()
window.setCentralWidget(chartView)
window.resize(400, 300)
window.show()

sys.exit(app.exec_())
