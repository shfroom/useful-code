#!/usr/bin/env python3
import threading
import sys
from time import sleep

class anim:
	def __init__(self, frames):
		self.frames = frames
		self.running = False

	def animate(self):
		self.running = True
		self.animation_thread = threading.Thread(target=self._run_animation)
		self.animation_thread.start()

	def _run_animation(self):
		while self.running:
			for frame in self.frames:
				if not self.running:
					break
				sys.stdout.write(f"\r{frame} ")
				sys.stdout.flush()
				sleep(0.2)

	def stop_animation(self):
		self.running = False
		self.animation_thread.join()

a = anim(["\\ Working...", "| Working...", "/ Working...", "- Working..."])
a.animate() ; sleep(3) ; a.stop_animation()