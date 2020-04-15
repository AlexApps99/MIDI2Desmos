#!/usr/bin/env python3
from math import log

def mid_to_hz(d):
	# Formula from Wikipedia
	return (2 ** ((d - 69) / 12)) * 440

def hz_to_des(h):
	# Rough constants, may need recalculation
	# https://www.desmos.com/calculator/iscqllyj4w
	return log(0.002 * h, 1.00708)

def mid_to_des(d):
	return hz_to_des(mid_to_hz(d))

# python3 graph.py | xclip -selection c
if __name__ == "__main__":
	from sys import argv, stderr
	from mido import MidiFile

	# Transpose
	if len(argv) > 4:
		tp = int(argv[4])
	else:
		tp = 22

	# Length
	if len(argv) > 3:
		lth = int(argv[3])
	else:
		lth = 125

	# Channel
	if len(argv) > 2:
		ch = int(argv[2])
	else:
		ch = 1

	# Filename
	if len(argv) > 1:
		filename = argv[1]
	else:
		print("Usage: "+argv[0]+" [file] [midi channel] [# of midi events] [semitones to transpose, + or -]")

	mid = MidiFile(filename, clip=True)

	notes = []

	time = 0

	note = 0
	start = 0

	note_on = False

	for msg in mid.tracks[ch][:lth]:
		time += msg.time
		if not note_on:
			if msg.type == "note_on" and msg.velocity > 0:
				note_on = True
				note = msg.note
				start = time
		elif note_on:
			if msg.type == "note_off" or (msg.type == "note_on" and msg.velocity == 0):
				if msg.note == note:
					note_on = False
					notes.append((start, time, note))

	s_t = notes[0][0]
	time = notes[-1][1]
	time -= s_t
	time /= 100
	#time = 1

	# Transposed to fit to scale
	#notes = [((a-s_t)/time, (b-s_t)/time, mid_to_des(((n + tp) % 12) + 72)) for a, b, n in notes]
	# As-is
	notes = [((a-s_t)/time, (b-s_t)/time, mid_to_des(n + tp)) for a, b, n in notes]

	formula = "y=\\left\\{" + ",".join([f"{a:.2f}\\le x\\le{b:.2f}:{n:.2f}" for a, b, n in notes]) + "\\right\\}"

	print(formula)
