import os,webbrowser
#webbrowser.register('chromium',None,webbrowser.BackgroundBrowser("C:\\ProgramFiles\\chrome-win\\chrome.exe"),preferred=True)
#r=''
def owb(r):
    for p,ds,fs in os.walk(r):
        for f in fs:
            if f.endswith('.html'):
                webbrowser.get('chromium').open_new_tab(os.path.join(p,f))
