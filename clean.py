#!/usr/bin/env python
# -*- coding: utf-8 -*-

from textteaser.parser import Parser

from flask import Flask
from flask import render_template
from flask import send_from_directory
from flask import request

THRESHOLD = 0.5

app = Flask(__name__)
text = ''

@app.route('/css/<path:path>')
def sendCss(path):
	return send_from_directory('css', path)

@app.route("/")
def index():
	return render_template('clean.html', text=text, cleaned=[])

@app.route("/clean", methods=['POST'])
def clean():
	text = request.form['text']
	c = Cleaner()
	sentences = c.clean(text)
	return render_template('clean.html', text=text, cleaned=sentences)

class Cleaner:
	def __init__(self):
		self.parser = Parser()
		self.initDict()

	def initDict(self):
		self.words = set()
		with open('data/20k.txt') as file:
			words = file.readlines()
		for word in words:
			self.words.add(word.strip())

	def clean(self, text):
		sentences = text.splitlines()
		print "sentences: {}".format(len(sentences))
		cleaned = []
		return [sentence for sentence in sentences 
			if self.sentenceScore(sentence) >= THRESHOLD]
			# score = self.sentenceScore(sentence)
			# cleaned.append("{:1.3f}".format(score))
			# cleaned.append(self.cleanSentence(sentence))
		# return cleaned

	def cleanSentence(self, sentence):
		sentence = self.parser.removePunctations(sentence)
		words = self.parser.splitWords(sentence)
		cleaned = []
		for word in words:
			cleaned.append('[' + word + ']')
		return " ".join(cleaned)

	def sentenceScore(self, sentence):
		sentence = self.parser.removePunctations(sentence)
		words = self.parser.splitWords(sentence)
		count = 0.0
		for word in words:
			if word in self.words and len(word) > 1:
				count = count + 1
		if len(words) == 0:
			return 0.0
		return count / len(words)