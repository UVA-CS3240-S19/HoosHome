import crawler
import utility

# a quick demo.

websites = "https://livewithmsc.com/featured/"
reg_for_strings = """style="text-align: center;">([A-Za-z0-9|$ ,.]*)<\/p>"""
reg_for_pics = """src="(\S*\.jpg)"""

data = utility.search(websites, "log.txt")
print(utility.lookForPatterns(data, reg_for_pics))
print(utility.lookForPatterns(data, reg_for_strings))
