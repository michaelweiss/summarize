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
	sentences = c.cleanWithScore(text)
	return render_template('clean.html', text=text, cleaned=sentences)

class Cleaner:
	def __init__(self):
		self.parser = Parser()
		self.initDict()

	def initDict(self):
		self.words = set()
		self.addWordsFromList('data/20k.txt')
		self.addWordsFromList('data/wordnet.txt')
		self.addWordsFromList('data/mydict.txt')

	def addWordsFromList(self, list):
		with open(list) as file:
			words = file.readlines()
		for word in words:
			self.words.add(word.strip())

	def clean(self, text):
		sentences = self.parser.splitSentences(text)
		cleaned = []
		return [sentence for sentence in sentences 
			if self.sentenceScore(sentence) >= THRESHOLD]

	def cleanWithScore(self, text):
		sentences = self.parser.splitSentences(text)
		cleaned = []
		# return [sentence for sentence in sentences 
		#	if self.sentenceScore(sentence) >= THRESHOLD]
		for sentence in sentences:
			score = self.sentenceScore(sentence)
			if (score >= THRESHOLD):
				cleaned.append("{:1.3f}".format(score))
				cleaned.append(sentence)
			# cleaned.append(self.cleanSentence(sentence))
		return cleaned

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