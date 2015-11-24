# -*- coding: utf-8 -*-

#from sys import argv


in_txt = open('diary.txt', 'a')
text = raw_input('What do you want to write today?'
	'\n''Hit RETURN if you want to review your diary.')
	
if text == '':
	print 'Here`s your diary:'
	in_txt = open('diary.txt')
	print in_txt.read()
else:
	in_txt.write('\n' + text)
	in_txt.close()