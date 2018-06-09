# !/usr/bin/python
# -*- coding: utf-8 -*-

from summarizer import Summarizer


class TextTeaser(object):

    def __init__(self):
        self.summarizer = Summarizer()

    def summarize(self, title, text, count=5, category="Undefined", source="Undefined"):
        result = self.summarizer.summarize(text, title, source, category)
        result = self.summarizer.sortSentences(result[:count])
        result = ["[{:1.3f}] ".format(res['totalScore']) + res['sentence'] for res in result]

        return result
