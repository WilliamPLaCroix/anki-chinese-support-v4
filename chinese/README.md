# Chinese Support v4


## Credit:

Chinese Support:

* V1. [chinese-support-addon](https://github.com/ttempe/chinese-support-addon)
  * Author: [Thomas TEMPÉ](https://github.com/ttempe)
  * Wiki: [Chinese Support Wiki](https://github.com/ttempe/chinese-support-addon/wiki)
* V2. [Chinese Support Redux v0.14.2](https://github.com/luoliyan/chinese-support-redux)
  * AnkiWeb: [AddonPage](https://ankiweb.net/shared/info/1128979221)
  * Author: [JD Lorimer](https://github.com/jdlorimer)
* V3. [Chinese Support 3](https://github.com/jdlorimer/chinese-support-redux)
  * AnkiWeb: [AddonPage](https://ankiweb.net/shared/info/1752008591)
  * Author: [Gustaf-C](https://github.com/Gustaf-C)
  * Contributors: [Kieran Black](ttps://github.com/kieranlblack)

Related addon:<br>
  *  [Korean Support](https://github.com/scottgigante/korean-support)
     * AnkiWeb: [AddonPage](https://ankiweb.net/shared/info/1336389630)
     * Author: [Scott Gigante](https://github.com/scottgigante)


## How to use

- The templates can be found under 'Choose Note Type' -> 'Manage' -> 'Add'
- If you find that a field is not filling at all, please check [config.json](https://github.com/luoliyan/chinese-support-redux/blob/master/chinese/config.json) for the complete list of valid field names. For those migrating from an older version of the add-on, you will need to rename any definition fields to `English`, `German` or `French`, depending on what you want.


## Features

- Automatic field filling
  - Translation (from built-in dictionary; supports English, German and French)
  - Romanisation (supports [Pīnyīn (拼音)](https://en.wikipedia.org/wiki/Pinyin) and Cantonese [Jyutping (粵拼)](https://en.wikipedia.org/wiki/Jyutping))
  - Mandarin Audio (fetched from Google or Baidu)
  - Traditional (繁體字) and simplified (簡體字) characters
  - [Bopomofo (ㄅㄆㄇㄈ)](https://en.wikipedia.org/wiki/Bopomofo), also known as Zhuyin (注音)
  - [Rubies](https://www.w3schools.com/tags/tag_ruby.asp) (small-print transcription placed above characters)
  - Frequency (from “very basic” to “obscure”) - based on [anki-chinese-word-frequency](https://github.com/ernop/anki-chinese-word-frequency)
  - Usage Sentence Examples - Chinese/English sentence pairs from [Tatoeba](https://tatoeba.org/)
- Automatic tone change of auto filled pinyin (hanzi field must be populated)
  - E.g. fen1kai1 -> *Tab* -> fēnkāi (won't replace existing tones)
- Tone colours (applied to characters, romanisation and Bopomofo)
- Built-in note types (Basic and Advanced)


## Usage

The core feature of the add-on is the automatic field filling. To take advantage of this, you need to have an Anki note type with the appropriate fields (e.g., `Hanzi`, `English`, `Pinyin`, `Sound`). See `config.json` for a list of valid field names.

If you don't already have such a note type, the easiest approach is to use one of the built-in models. Two types are installed automatically: Basic and Advanced. The only important difference is that the Advanced model shows more information.

To use the field-filling features:

1. Add a new note to Anki (press *a*)
2. Create (manage -> add) and select `Chinese (Basic)` or `Chinese (Advanced)` as the note type
3. Enable Chinese Support 3 for this note type (click `汉字`)
4. Enter a word (e.g., 電話) into the `Hanzi` field (sentences will also work)
5. Press *Tab*
6. The remaining fields should then be populated automatically



