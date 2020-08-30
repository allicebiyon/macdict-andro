# macdict-andro
EN: Converts the Japanese user dictionary from a Mac so that it can be used with the Google Japanese Input on Android devices.
  
JP: macOSのユーザ辞書をandroidのGoogle日本語入力でも使えるようにするpythonプログラムです。

## Prerequisites
You will need:
* A Mac that runs python
* An Android device with Google 日本語入力

## Usage
1. Read ユーザ辞書を書き出す/読み込む at [Macの日本語ユーザ辞書を編集する/使用する](https://support.apple.com/ja-jp/guide/japanese-input-method/jpim10228/mac) to extract your Mac user dictionary to a file, e.g. 「ユーザ辞書.plist」
2. `$ python macdict-andro.py -i ユーザ辞書.plist`
3. Output file from step 2 is 「ユーザ辞書\_android.txt」
4. On your Android device, go to 設定 → 言語と入力 → Google 日本語入力 → 辞書ツール → ・・・ → 辞書をインポート to load your output file from step 3
5. (っ'ヮ'c)☕️ yeah

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
