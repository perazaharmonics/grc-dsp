#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# Author: perazaharmonics
# GNU Radio version: 3.10.1.1

from packaging.version import Version as StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import analog
from gnuradio import blocks
from gnuradio import filter
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio.qtgui import Range, RangeWidget
from PyQt5 import QtCore
import numpy as np



from gnuradio import qtgui

class WaveletDecDb6Flowgraph(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "WaveletDecDb6Flowgraph")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 256000
        self.h = h = [-0.001077301085308, 0.0047772575109455,  0.0005538422011614, -0.031582039318486, 0.027522865530305, 0.097501605587322, -0.129766867567262, -0.226264693965440,  0.315250351709198, 0.751133908021095, 0.494623890398453, 0.111540743350109]
        self.h_inv = h_inv = h[::-1]
        self.g_inv = g_inv = [-0.0010773011, -0.0047772575, 0.0005538422, 0.0315820393, 0.0275228655, -0.0975016056, -0.1297668676, 0.2262646940, 0.3152503517, -0.7511339080, 0.4946238904, -0.1115407434 ]
        self.g = g = [h[11], -h[10], h[9], -h[8], h[7], -h[6], h[5], -h[4], h[3], -h[2], h[1], -h[0]]
        self.frequency = frequency = samp_rate / 64

        ##################################################
        # Blocks
        ##################################################
        self._frequency_range = Range(-samp_rate/2, samp_rate/2, 1, samp_rate / 64, 200)
        self._frequency_win = RangeWidget(self._frequency_range, self.set_frequency, "'frequency'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._frequency_win)
        self.qtgui_time_sink_x_7 = qtgui.time_sink_c(
            2048, #size
            samp_rate, #samp_rate
            "Details 3", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_7.set_update_time(0.10)
        self.qtgui_time_sink_x_7.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_7.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_7.enable_tags(True)
        self.qtgui_time_sink_x_7.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_7.enable_autoscale(True)
        self.qtgui_time_sink_x_7.enable_grid(False)
        self.qtgui_time_sink_x_7.enable_axis_labels(True)
        self.qtgui_time_sink_x_7.enable_control_panel(False)
        self.qtgui_time_sink_x_7.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(2):
            if len(labels[i]) == 0:
                if (i % 2 == 0):
                    self.qtgui_time_sink_x_7.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_7.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_7.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_7.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_7.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_7.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_7.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_7.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_7_win = sip.wrapinstance(self.qtgui_time_sink_x_7.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_7_win)
        self.qtgui_time_sink_x_6 = qtgui.time_sink_c(
            2048, #size
            samp_rate, #samp_rate
            "Approximations 3", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_6.set_update_time(0.10)
        self.qtgui_time_sink_x_6.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_6.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_6.enable_tags(True)
        self.qtgui_time_sink_x_6.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_6.enable_autoscale(True)
        self.qtgui_time_sink_x_6.enable_grid(False)
        self.qtgui_time_sink_x_6.enable_axis_labels(True)
        self.qtgui_time_sink_x_6.enable_control_panel(False)
        self.qtgui_time_sink_x_6.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(2):
            if len(labels[i]) == 0:
                if (i % 2 == 0):
                    self.qtgui_time_sink_x_6.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_6.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_6.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_6.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_6.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_6.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_6.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_6.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_6_win = sip.wrapinstance(self.qtgui_time_sink_x_6.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_6_win)
        self.qtgui_time_sink_x_5 = qtgui.time_sink_c(
            2048, #size
            samp_rate, #samp_rate
            "Details 2", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_5.set_update_time(0.10)
        self.qtgui_time_sink_x_5.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_5.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_5.enable_tags(True)
        self.qtgui_time_sink_x_5.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_5.enable_autoscale(False)
        self.qtgui_time_sink_x_5.enable_grid(False)
        self.qtgui_time_sink_x_5.enable_axis_labels(True)
        self.qtgui_time_sink_x_5.enable_control_panel(False)
        self.qtgui_time_sink_x_5.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(2):
            if len(labels[i]) == 0:
                if (i % 2 == 0):
                    self.qtgui_time_sink_x_5.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_5.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_5.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_5.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_5.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_5.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_5.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_5.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_5_win = sip.wrapinstance(self.qtgui_time_sink_x_5.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_5_win)
        self.qtgui_time_sink_x_4 = qtgui.time_sink_c(
            2048, #size
            samp_rate, #samp_rate
            "Approximations 2", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_4.set_update_time(0.10)
        self.qtgui_time_sink_x_4.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_4.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_4.enable_tags(True)
        self.qtgui_time_sink_x_4.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_4.enable_autoscale(False)
        self.qtgui_time_sink_x_4.enable_grid(False)
        self.qtgui_time_sink_x_4.enable_axis_labels(True)
        self.qtgui_time_sink_x_4.enable_control_panel(False)
        self.qtgui_time_sink_x_4.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(2):
            if len(labels[i]) == 0:
                if (i % 2 == 0):
                    self.qtgui_time_sink_x_4.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_4.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_4.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_4.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_4.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_4.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_4.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_4.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_4_win = sip.wrapinstance(self.qtgui_time_sink_x_4.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_4_win)
        self.qtgui_time_sink_x_3 = qtgui.time_sink_c(
            2048, #size
            samp_rate, #samp_rate
            "Details 1", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_3.set_update_time(0.10)
        self.qtgui_time_sink_x_3.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_3.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_3.enable_tags(True)
        self.qtgui_time_sink_x_3.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_3.enable_autoscale(False)
        self.qtgui_time_sink_x_3.enable_grid(False)
        self.qtgui_time_sink_x_3.enable_axis_labels(True)
        self.qtgui_time_sink_x_3.enable_control_panel(False)
        self.qtgui_time_sink_x_3.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(2):
            if len(labels[i]) == 0:
                if (i % 2 == 0):
                    self.qtgui_time_sink_x_3.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_3.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_3.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_3.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_3.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_3.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_3.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_3.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_3_win = sip.wrapinstance(self.qtgui_time_sink_x_3.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_3_win)
        self.qtgui_time_sink_x_2 = qtgui.time_sink_c(
            2048, #size
            samp_rate, #samp_rate
            "Approximation 1", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_2.set_update_time(0.10)
        self.qtgui_time_sink_x_2.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_2.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_2.enable_tags(True)
        self.qtgui_time_sink_x_2.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_2.enable_autoscale(False)
        self.qtgui_time_sink_x_2.enable_grid(False)
        self.qtgui_time_sink_x_2.enable_axis_labels(True)
        self.qtgui_time_sink_x_2.enable_control_panel(False)
        self.qtgui_time_sink_x_2.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(2):
            if len(labels[i]) == 0:
                if (i % 2 == 0):
                    self.qtgui_time_sink_x_2.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_2.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_2.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_2.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_2.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_2.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_2.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_2.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_2_win = sip.wrapinstance(self.qtgui_time_sink_x_2.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_2_win)
        self.qtgui_time_sink_x_1 = qtgui.time_sink_c(
            2048, #size
            samp_rate, #samp_rate
            "Perfect Reconstruction", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_1.set_update_time(0.10)
        self.qtgui_time_sink_x_1.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_1.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_1.enable_tags(True)
        self.qtgui_time_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1.enable_autoscale(True)
        self.qtgui_time_sink_x_1.enable_grid(False)
        self.qtgui_time_sink_x_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_1.enable_control_panel(False)
        self.qtgui_time_sink_x_1.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(2):
            if len(labels[i]) == 0:
                if (i % 2 == 0):
                    self.qtgui_time_sink_x_1.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_1.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_1_win = sip.wrapinstance(self.qtgui_time_sink_x_1.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_1_win)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_c(
            2048, #size
            samp_rate, #samp_rate
            "Input Signal", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(2):
            if len(labels[i]) == 0:
                if (i % 2 == 0):
                    self.qtgui_time_sink_x_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
            2048, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "Approx 1 Spectral Contribution", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_0.set_fft_window_normalized(False)



        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.interp_fir_filter_xxx_0_2 = filter.interp_fir_filter_ccc(2, h_inv)
        self.interp_fir_filter_xxx_0_2.declare_sample_delay(0)
        self.interp_fir_filter_xxx_0_1 = filter.interp_fir_filter_ccc(2, h_inv)
        self.interp_fir_filter_xxx_0_1.declare_sample_delay(0)
        self.interp_fir_filter_xxx_0_0_1 = filter.interp_fir_filter_ccc(2, g_inv)
        self.interp_fir_filter_xxx_0_0_1.declare_sample_delay(0)
        self.interp_fir_filter_xxx_0_0_0 = filter.interp_fir_filter_ccc(2, g_inv)
        self.interp_fir_filter_xxx_0_0_0.declare_sample_delay(0)
        self.interp_fir_filter_xxx_0_0 = filter.interp_fir_filter_ccc(2, g_inv)
        self.interp_fir_filter_xxx_0_0.declare_sample_delay(0)
        self.interp_fir_filter_xxx_0 = filter.interp_fir_filter_ccc(2, h_inv)
        self.interp_fir_filter_xxx_0.declare_sample_delay(0)
        self.fir_filter_xxx_0_1_0_0 = filter.fir_filter_ccc(2, g)
        self.fir_filter_xxx_0_1_0_0.declare_sample_delay(0)
        self.fir_filter_xxx_0_1_0 = filter.fir_filter_ccc(2, h)
        self.fir_filter_xxx_0_1_0.declare_sample_delay(0)
        self.fir_filter_xxx_0_1 = filter.fir_filter_ccc(2, h)
        self.fir_filter_xxx_0_1.declare_sample_delay(0)
        self.fir_filter_xxx_0_0_0 = filter.fir_filter_ccc(2, g)
        self.fir_filter_xxx_0_0_0.declare_sample_delay(0)
        self.fir_filter_xxx_0_0 = filter.fir_filter_ccc(2, g)
        self.fir_filter_xxx_0_0.declare_sample_delay(0)
        self.fir_filter_xxx_0 = filter.fir_filter_ccc(2, h)
        self.fir_filter_xxx_0.declare_sample_delay(0)
        self.blocks_throttle_0_0_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_add_xx_0_0_0 = blocks.add_vcc(1)
        self.blocks_add_xx_0_0 = blocks.add_vcc(1)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.analog_sig_source_x_0 = analog.sig_source_c(4*samp_rate, analog.GR_SIN_WAVE, frequency, 1, 0, 0)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_throttle_0_0_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.interp_fir_filter_xxx_0_2, 0))
        self.connect((self.blocks_add_xx_0_0, 0), (self.interp_fir_filter_xxx_0_1, 0))
        self.connect((self.blocks_add_xx_0_0_0, 0), (self.qtgui_time_sink_x_1, 0))
        self.connect((self.blocks_throttle_0_0_0, 0), (self.fir_filter_xxx_0, 0))
        self.connect((self.blocks_throttle_0_0_0, 0), (self.fir_filter_xxx_0_0, 0))
        self.connect((self.blocks_throttle_0_0_0, 0), (self.fir_filter_xxx_0_0_0, 0))
        self.connect((self.fir_filter_xxx_0, 0), (self.fir_filter_xxx_0_1, 0))
        self.connect((self.fir_filter_xxx_0_0, 0), (self.interp_fir_filter_xxx_0_0_0, 0))
        self.connect((self.fir_filter_xxx_0_0_0, 0), (self.interp_fir_filter_xxx_0_0_1, 0))
        self.connect((self.fir_filter_xxx_0_1, 0), (self.fir_filter_xxx_0_1_0, 0))
        self.connect((self.fir_filter_xxx_0_1, 0), (self.fir_filter_xxx_0_1_0_0, 0))
        self.connect((self.fir_filter_xxx_0_1_0, 0), (self.interp_fir_filter_xxx_0, 0))
        self.connect((self.fir_filter_xxx_0_1_0_0, 0), (self.interp_fir_filter_xxx_0_0, 0))
        self.connect((self.interp_fir_filter_xxx_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.interp_fir_filter_xxx_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.interp_fir_filter_xxx_0, 0), (self.qtgui_time_sink_x_2, 0))
        self.connect((self.interp_fir_filter_xxx_0_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.interp_fir_filter_xxx_0_0, 0), (self.qtgui_time_sink_x_3, 0))
        self.connect((self.interp_fir_filter_xxx_0_0_0, 0), (self.blocks_add_xx_0_0, 1))
        self.connect((self.interp_fir_filter_xxx_0_0_0, 0), (self.qtgui_time_sink_x_5, 0))
        self.connect((self.interp_fir_filter_xxx_0_0_1, 0), (self.blocks_add_xx_0_0_0, 1))
        self.connect((self.interp_fir_filter_xxx_0_0_1, 0), (self.qtgui_time_sink_x_7, 0))
        self.connect((self.interp_fir_filter_xxx_0_1, 0), (self.blocks_add_xx_0_0_0, 0))
        self.connect((self.interp_fir_filter_xxx_0_1, 0), (self.qtgui_time_sink_x_6, 0))
        self.connect((self.interp_fir_filter_xxx_0_2, 0), (self.blocks_add_xx_0_0, 0))
        self.connect((self.interp_fir_filter_xxx_0_2, 0), (self.qtgui_time_sink_x_4, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "WaveletDecDb6Flowgraph")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_frequency(self.samp_rate / 64)
        self.analog_sig_source_x_0.set_sampling_freq(4*self.samp_rate)
        self.blocks_throttle_0_0_0.set_sample_rate(self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_1.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_2.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_3.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_4.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_5.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_6.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_7.set_samp_rate(self.samp_rate)

    def get_h(self):
        return self.h

    def set_h(self, h):
        self.h = h
        self.set_g([self.h[11], -self.h[10], self.h[9], -self.h[8], self.h[7], -self.h[6], self.h[5], -self.h[4], self.h[3], -self.h[2], self.h[1], -self.h[0]])
        self.set_h_inv(self.h[::-1])
        self.fir_filter_xxx_0.set_taps(self.h)
        self.fir_filter_xxx_0_1.set_taps(self.h)
        self.fir_filter_xxx_0_1_0.set_taps(self.h)

    def get_h_inv(self):
        return self.h_inv

    def set_h_inv(self, h_inv):
        self.h_inv = h_inv
        self.interp_fir_filter_xxx_0.set_taps(self.h_inv)
        self.interp_fir_filter_xxx_0_1.set_taps(self.h_inv)
        self.interp_fir_filter_xxx_0_2.set_taps(self.h_inv)

    def get_g_inv(self):
        return self.g_inv

    def set_g_inv(self, g_inv):
        self.g_inv = g_inv
        self.interp_fir_filter_xxx_0_0.set_taps(self.g_inv)
        self.interp_fir_filter_xxx_0_0_0.set_taps(self.g_inv)
        self.interp_fir_filter_xxx_0_0_1.set_taps(self.g_inv)

    def get_g(self):
        return self.g

    def set_g(self, g):
        self.g = g
        self.fir_filter_xxx_0_0.set_taps(self.g)
        self.fir_filter_xxx_0_0_0.set_taps(self.g)
        self.fir_filter_xxx_0_1_0_0.set_taps(self.g)

    def get_frequency(self):
        return self.frequency

    def set_frequency(self, frequency):
        self.frequency = frequency
        self.analog_sig_source_x_0.set_frequency(self.frequency)




def main(top_block_cls=WaveletDecDb6Flowgraph, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
