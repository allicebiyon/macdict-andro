# macdict-andro
Converts the Japanese user dictionary on a Mac so that it can be used with the Google Japanese Input on Android devices.

# Usage
1. Read [Mac でユーザ辞書を書き出す／読み込む方法]https://support.apple.com/ja-jp/HT204006 to extract your Macintosh user dictionary, e.g. 「ユーザ辞書.plist」
2. `$ python macdict-to-andro.py -i ユーザ辞書.plist`
3. Output file is 「ユーザ辞書\_android.txt」
4. Import the file on your Android device.
