#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "allicebiyon"

import xml.etree.ElementTree as ET
import codecs, sys, argparse

parser = argparse.ArgumentParser(description='Macのユーザ辞書をAndroid用に変換します。')
parser.add_argument('-i', metavar='入力ファイル', nargs = 1, required=True, type=argparse.FileType('r'))

fin = ""

try:
    results = parser.parse_args()
    fin = results.i[0]
except IOError, msg:
    parser.error(str(msg))

try:
    tree = ET.parse(fin)
    root = tree.getroot()
except ET.ParseError:
    print "入力ファイルを正しくパースできませんでした。XMLファイルではない可能性があります。"
    sys.exit(2)

try:
    fout_name = fin.name.replace(".plist", "") + '_android.txt'
    fout = codecs.open(fout_name, 'w', 'utf-8')
    for array in root:
        for dict_entry in array:
            phrase_flag = False
            shortcut_flag = False
            phrase = ""
            shortcut = ""
            
            for child in dict_entry:

                if child.tag == "key" and child.text == "phrase":
                    phrase_flag = True
                    shortcut_flag = False
                    continue
                
                if phrase_flag:
                    phrase_flag = False
                    phrase = child.text

                if child.tag == "key" and child.text == "shortcut":
                    shortcut_flag = True
                    phrase_flag = False
                    continue

                if shortcut_flag:
                    shortcut_flag = False
                    shortcut = child.text

            #print shortcut + "\t" + phrase + "\t" + "asdf"
            fout.write(shortcut + "\t" + phrase + "\t" + u"名詞" + "\n")

    fout.close()
    print fout_name + " が書き出されました。"

except:
    print "なんかよく分からないけど失敗しました！"
    sys.exit(1)
