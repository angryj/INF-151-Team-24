# https://programminghistorian.org/en/lessons/creating-and-viewing-html-files-with-python
# write-html-2-mac.py
import webbrowser
import mammoth

custom_styles = "b => i"


f = open('helloworld.html','w')

with open("test2.docx", "rb") as docx_file:
    result = mammoth.convert_to_html(docx_file, style_map = custom_styles)
    text = result.value
    with open('output.html', 'w') as html_file:
        f.write(text)

f.close()

filename = 'helloworld.html'
try:
    #this is for Jason
    cent_path = "C:/Program Files/CentBrowser/Application/chrome.exe %s"
    webbrowser.get(cent_path).open_new_tab(filename)
except:
    webbrowser.open_new_tab(filename)