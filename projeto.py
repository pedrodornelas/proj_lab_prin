#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# Author: lucas
# GNU Radio version: v3.10-compat-xxx-xunknown

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio.qtgui import Range, RangeWidget
from PyQt5 import QtCore



from gnuradio import qtgui

class projeto(gr.top_block, Qt.QWidget):

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

        self.settings = Qt.QSettings("GNU Radio", "projeto")

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
        self.volume = volume = 1
        self.samp_rate = samp_rate = 240000
        self.radio = radio = 1
        self.pi = pi = 3.141592654
        self.freq = freq = 700
        self.cut = cut = 6000

        ##################################################
        # Blocks
        ##################################################
        self._volume_range = Range(0, 30, 1, 1, 200)
        self._volume_win = RangeWidget(self._volume_range, self.set_volume, 'volume', "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._volume_win)
        self._radio_range = Range(0, 4, 1, 1, 200)
        self._radio_win = RangeWidget(self._radio_range, self.set_radio, 'radio', "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._radio_win)
        self._freq_range = Range(0, 1000, 100, 700, 200)
        self._freq_win = RangeWidget(self._freq_range, self.set_freq, 'freq', "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._freq_win)
        self._cut_range = Range(0, 14000, 100, 6000, 200)
        self._cut_win = RangeWidget(self._cut_range, self.set_cut, 'cut', "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._cut_win)
        self.low_pass_filter_0_1_0_0 = filter.fir_filter_fff(
            1,
            firdes.low_pass(
                1,
                samp_rate,
                cut,
                100,
                window.WIN_HAMMING,
                6.76))
        self.low_pass_filter_0_0_1_0_1 = filter.fir_filter_fff(
            1,
            firdes.low_pass(
                1,
                samp_rate,
                7000,
                100,
                window.WIN_HAMMING,
                6.76))
        self.low_pass_filter_0_0_1_0_0_0 = filter.fir_filter_fff(
            1,
            firdes.low_pass(
                1,
                samp_rate,
                7000,
                100,
                window.WIN_HAMMING,
                6.76))
        self.low_pass_filter_0_0_1_0_0 = filter.fir_filter_fff(
            1,
            firdes.low_pass(
                1,
                samp_rate,
                7000,
                100,
                window.WIN_HAMMING,
                6.76))
        self.low_pass_filter_0_0_1_0 = filter.fir_filter_fff(
            1,
            firdes.low_pass(
                1,
                samp_rate,
                7000,
                100,
                window.WIN_HAMMING,
                6.76))
        self.blocks_wavfile_source_0_1_0 = blocks.wavfile_source('/home/lucas/Documentos/unb/labprincom/proj_lab_prin/RondoAllaTurca.wav', True)
        self.blocks_wavfile_source_0_1 = blocks.wavfile_source('/home/lucas/Documentos/unb/labprincom/proj_lab_prin/5th_Symphony.wav', True)
        self.blocks_throttle_0_2_0_1 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_throttle_0_2_0_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_throttle_0_2_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_throttle_0_0_2_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_throttle_0_0_1_0_0_1 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_throttle_0_0_1_0_0_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_throttle_0_0_1_0_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_throttle_0_0_0_1_0_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_multiply_xx_0_2_0_0_1 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_2_0_0_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_2_0_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_2_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_0_0_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(volume)
        self.blocks_add_xx_0_0_0 = blocks.add_vff(1)
        self.audio_sink_1_0 = audio.sink(44100, '', True)
        self.analog_sig_source_x_0_3_0_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, freq, 2, -1, 0)
        self.analog_sig_source_x_0_1_3_0_1 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 90000000, 1, 0, 0)
        self.analog_sig_source_x_0_1_3_0_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 100000000, 5, 0, 0)
        self.analog_sig_source_x_0_1_2_0_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 85000000+(radio*5000000), 1, 0, 0)
        self.analog_sig_source_x_0_1_0_0_0_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 105000000, 5, 0, 0)
        self.analog_sig_source_x_0_1_0_0_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 95000000, 1, 0, 0)
        self.analog_sig_source_x_0_0_0_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, freq, 1, -1, 0)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0_0_0_0, 0), (self.blocks_throttle_0_0_2_0, 0))
        self.connect((self.analog_sig_source_x_0_1_0_0_0, 0), (self.blocks_throttle_0_0_1_0_0, 0))
        self.connect((self.analog_sig_source_x_0_1_0_0_0_0, 0), (self.blocks_throttle_0_0_1_0_0_0, 0))
        self.connect((self.analog_sig_source_x_0_1_2_0_0, 0), (self.blocks_multiply_xx_0_0_0_0_0, 1))
        self.connect((self.analog_sig_source_x_0_1_3_0_0, 0), (self.blocks_throttle_0_0_1_0_0_1, 0))
        self.connect((self.analog_sig_source_x_0_1_3_0_1, 0), (self.blocks_throttle_0_0_0_1_0_0, 0))
        self.connect((self.analog_sig_source_x_0_3_0_0, 0), (self.blocks_throttle_0_2_0_0, 0))
        self.connect((self.blocks_add_xx_0_0_0, 0), (self.blocks_multiply_xx_0_0_0_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.low_pass_filter_0_1_0_0, 0))
        self.connect((self.blocks_multiply_xx_0_0_0_0_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_multiply_xx_0_2_0_0, 0), (self.blocks_add_xx_0_0_0, 1))
        self.connect((self.blocks_multiply_xx_0_2_0_0_0, 0), (self.blocks_add_xx_0_0_0, 2))
        self.connect((self.blocks_multiply_xx_0_2_0_0_0_0, 0), (self.blocks_add_xx_0_0_0, 3))
        self.connect((self.blocks_multiply_xx_0_2_0_0_1, 0), (self.blocks_add_xx_0_0_0, 0))
        self.connect((self.blocks_throttle_0_0_0_1_0_0, 0), (self.blocks_multiply_xx_0_2_0_0_1, 1))
        self.connect((self.blocks_throttle_0_0_1_0_0, 0), (self.blocks_multiply_xx_0_2_0_0, 1))
        self.connect((self.blocks_throttle_0_0_1_0_0_0, 0), (self.blocks_multiply_xx_0_2_0_0_0_0, 1))
        self.connect((self.blocks_throttle_0_0_1_0_0_1, 0), (self.blocks_multiply_xx_0_2_0_0_0, 1))
        self.connect((self.blocks_throttle_0_0_2_0, 0), (self.low_pass_filter_0_0_1_0_0_0, 0))
        self.connect((self.blocks_throttle_0_2_0, 0), (self.low_pass_filter_0_0_1_0, 0))
        self.connect((self.blocks_throttle_0_2_0_0, 0), (self.low_pass_filter_0_0_1_0_0, 0))
        self.connect((self.blocks_throttle_0_2_0_1, 0), (self.low_pass_filter_0_0_1_0_1, 0))
        self.connect((self.blocks_wavfile_source_0_1, 0), (self.blocks_throttle_0_2_0, 0))
        self.connect((self.blocks_wavfile_source_0_1_0, 0), (self.blocks_throttle_0_2_0_1, 0))
        self.connect((self.low_pass_filter_0_0_1_0, 0), (self.blocks_multiply_xx_0_2_0_0_1, 0))
        self.connect((self.low_pass_filter_0_0_1_0_0, 0), (self.blocks_multiply_xx_0_2_0_0_0, 0))
        self.connect((self.low_pass_filter_0_0_1_0_0_0, 0), (self.blocks_multiply_xx_0_2_0_0, 0))
        self.connect((self.low_pass_filter_0_0_1_0_1, 0), (self.blocks_multiply_xx_0_2_0_0_0_0, 0))
        self.connect((self.low_pass_filter_0_1_0_0, 0), (self.audio_sink_1_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "projeto")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_volume(self):
        return self.volume

    def set_volume(self, volume):
        self.volume = volume
        self.blocks_multiply_const_vxx_0.set_k(self.volume)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0_0_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_1_0_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_1_0_0_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_1_2_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_1_3_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_1_3_0_1.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_3_0_0.set_sampling_freq(self.samp_rate)
        self.blocks_throttle_0_0_0_1_0_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0_0_1_0_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0_0_1_0_0_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0_0_1_0_0_1.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0_0_2_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0_2_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0_2_0_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0_2_0_1.set_sample_rate(self.samp_rate)
        self.low_pass_filter_0_0_1_0.set_taps(firdes.low_pass(1, self.samp_rate, 7000, 100, window.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0_1_0_0.set_taps(firdes.low_pass(1, self.samp_rate, 7000, 100, window.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0_1_0_0_0.set_taps(firdes.low_pass(1, self.samp_rate, 7000, 100, window.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0_1_0_1.set_taps(firdes.low_pass(1, self.samp_rate, 7000, 100, window.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_1_0_0.set_taps(firdes.low_pass(1, self.samp_rate, self.cut, 100, window.WIN_HAMMING, 6.76))

    def get_radio(self):
        return self.radio

    def set_radio(self, radio):
        self.radio = radio
        self.analog_sig_source_x_0_1_2_0_0.set_frequency(85000000+(self.radio*5000000))

    def get_pi(self):
        return self.pi

    def set_pi(self, pi):
        self.pi = pi

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.analog_sig_source_x_0_0_0_0.set_frequency(self.freq)
        self.analog_sig_source_x_0_3_0_0.set_frequency(self.freq)

    def get_cut(self):
        return self.cut

    def set_cut(self, cut):
        self.cut = cut
        self.low_pass_filter_0_1_0_0.set_taps(firdes.low_pass(1, self.samp_rate, self.cut, 100, window.WIN_HAMMING, 6.76))




def main(top_block_cls=projeto, options=None):

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
