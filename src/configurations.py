# Google translator language codes
translate_lang ={'English':'en','Chinese-Simplified':'zh-CN','Chinese-Traditional':'zh-TW','Malay':'ms','Filipino':'tl','Vietnamese':'vi','Tamil':'ta',
              'Thai':'th'}

# Construct the Tesseract configuration string with the specified languages
ocr_lang = ['eng', 'chi_sim', 'chi_tra', 'msa', 'tgl', 'vie', 'tam', 'tha']
custom_config = r'--psm 6 -l ' + '+'.join(ocr_lang)