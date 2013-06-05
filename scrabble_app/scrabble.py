# This is whre you can start you python file for your week1 web app
# Name: Brian Yee

import flask, flask.views
import os
app = flask.Flask(__name__)

app.secret_key = "bacon"

class View(flask.views.MethodView):
    def get(self):
        return flask.render_template('index.html')

    def post(self):
        letters = self.signature(flask.request.form['letters'])
        wordlist = open('words.txt')
        minimum = int(flask.request.form['min'])
        maximum = int(flask.request.form['max'])
        result = self.all_possibilities('words.txt', letters, minimum, maximum)
        flask.flash(result)
        return self.get()

    def make_word_dict(self, l):
        scrabble_dict = {}
        for letter in l:
            if letter in scrabble_dict:
                scrabble_dict[letter] = scrabble_dict[letter] + 1
            else:
                scrabble_dict[letter] = 1
        return scrabble_dict

    def signature(self, s):
        t = list(s)
        scrabble_dict = self.make_word_dict(t)
        return scrabble_dict


    def all_possibilities(self, filename, scrabble_letters, min_num_letters, total_word_length):
        """
        Takes in a filename, the letters you have in your tray, the minimum number of 
        letters in your tray that you need to include in your word, and the maximum length
        of word you want.
        """
        d = []
        for line in open(filename):
            word = line.strip().lower()
            list_word = list(word)
            word_dict = self.make_word_dict(list_word)
            for i in scrabble_letters.keys():
                if i in word_dict:
                    if word_dict[i] > 1:
                        word_dict[i] = word_dict[i]-1
                    else:
                        word_dict.pop(i)
            nums_list = word_dict.values()
            ct = 0
            for x in nums_list:
                ct = ct + x + 1
            if (len(list_word) - ct) >= min_num_letters and len(list_word) <= total_word_length:
                d.append(word)
        return d

app.add_url_rule('/', view_func=View.as_view('main'), methods=['GET','POST'])

app.debug = True
app.run()