#Langy
_A simple to use localization library_
    
##About
Langy is an extremly lightweight (~80 lines incl. comments) and easy to
use language, built for large and small scale Python applications. It has
an extremely easy to use and understand API, with only 5 functions you need
to know.
    
##How-to
Getting Started:
1. Run `python langy.py` in your project directory to generate the default 
config file, and languages folder.    
2. Edit the (json) config file to match your desired usage    
 - Languages: List of supported languages    
 - Default_lang: The default language    
 - Language_dir: Directory where languages are stored. You can probablly    
just leave this alone
3. Add languages either by creating JSON language files, or using the idle
method:    
 - Create any language files you want (`cd ./languages/`, `touch en_us`)    
 - Bring up the Python IDLE    
 - `import langy`    
 - `langy.load()`    
 - `lang = {'stringa':'valuea', 'stringb':valueb'}`    
 - `langy.dumpLang('en_us', lang)`    
 OR    
 - `langy.addString('stringc', 'valuec', 'en_us')    
4. Add the following to your code base:   
 
```
import langy
langy.load()
```
    
5. And wherever you need to grab a localized string:     

```
print langy.getString('my_string', 'en_us')
```
    
Presto!
