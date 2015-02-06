######
###

import sys
from PySide.QtCore import *
from PySide.QtGui import *
from AudioPlayerUI import *

from PySide.phonon import Phonon

class AudioPlayer(QMainWindow, Ui_AudioPlayerDemo):

	def __init__(self, parent=None):

		super(AudioPlayer, self).__init__(parent)
		self.setupUi(self)
		self.actionOpen.triggered.connect(self.open)
		self.actionQuit.triggered.connect(self.quite)
		self.horizontalSlider.setValue(0)
		self.horizontalSlider.setEnabled(False)
		self.horizontalSlider.sliderReleased.connect(self.slider_value_change)
		self.button.clicked.connect(self.play_or_pause)
		self.button.setText("Play")
		self.button.setEnabled(False)
		self.media_obj = Phonon.MediaObject(self)
		self.current_time = 0

	def play_or_pause(self):
		if Phonon.State.PlayingState == self.media_obj.state():
			self.media_obj.pause()
			self.button.setText("Play")
		elif Phonon.State.PausedState == self.media_obj.state():
			self.media_obj.play()
			self.button.setText("Pause")

	def slider_value_change(self):
		value = self.horizontalSlider.value()
		print value
		self.media_obj.seek(value)

	def open(self):
		dialog = QFileDialog()
		dialog.setViewMode(QFileDialog.Detail)
		filename = dialog.getOpenFileName(self, 'Open audio file', '/home', "Audio Files (*.mp3 *.wav *.ogg)")[0]
		self.audio_output = Phonon.AudioOutput(Phonon.MusicCategory, self)
		Phonon.createPath(self.media_obj, self.audio_output)
		self.media_obj.setCurrentSource(Phonon.MediaSource(filename))
		self.media_obj.tick.connect(self.time_change)
		self.media_obj.totalTimeChanged.connect(self.total_time_change)
		self.media_obj.play()
		self.button.setEnabled(True)
		self.button.setText("Pause")
		self.horizontalSlider.setEnabled(True)

	def time_change(self, time):
		if not self.horizontalSlider.isSliderDown():
			self.horizontalSlider.setValue(time)

	def total_time_change(self, time):
		self.horizontalSlider.setRange(0, time)

	def quite(self):
		sys.exit()



if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = AudioPlayer()
	window.show()
	sys.exit(app.exec_())		
