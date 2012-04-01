import sys, os, time
import json

config = {
'default_lang':'en_us',
'language_dir':'languages',
'languages':['en_us', 'pirate_speak']
}
strings = {}

def load():
	"""
	Load the config file must be run before getString
	or addString actions.
	"""
	global config
	if os.path.exists('lang.cfg'):
		config = json.load(open('lang.cfg'))
	else:
		with open('lang.cfg', 'w') as f:
			json.dump(config, f)
	if not os.path.exists(config['language_dir']): os.mkdir(config['language_dir'])
	for st in config['languages']:
		with open(os.path.join(config['language_dir'], st), 'r') as s:
			strings[st] = json.load(s)['strings']
			
def unload(save=True):
	"""
	Save any language changes to the disk.
	Don't run if you use lots of languages,
	or have extremly large string dicts.
	
	In either of those cases, customize your
	script to use dumpLang() on any language
	change.
	"""
	for lang in strings:
		dumpLang(lang, strings[lang])

def getString(string, lang, *args):
	"""
	Return a string for the given language
	string (str): String name
	lang (str): Language name
	*args: Any %s parsed args.
	"""
	lang = lang or config['default_lang']
	if lang in strings.keys():
		return strings[lang][string] % args
	else:
		raise Exception('Language %s is not localized yet!' % lang)

def addString(name, value, lang=config['default_lang']):
	"""
	Add a string to the given language. This
	/does/ not save when you add it, use either
	dumpLang or unload()
	name (str): string name
	value (str): localized string value
	lang (str): language name
	"""
	if lang in strings.keys():
		strings[lang][name] = unicode(value)
	else:
		raise Exception('Unknown language %s' % lang)
		
def dumpLang(lang, strings):
	"""
	Save or 'dump' a language to its
	language file (which will be created
	if it does not exsist)
	lang (str): language name
	strings (str): dictionary of language strings
	""" 
	with open(os.path.join(config['language_dir'], lang), 'w') as f:
		d = {
		'lang_key':lang,
		'dump_time':time.time(),
		'strings':strings
		}
		json.dump(d, f)
