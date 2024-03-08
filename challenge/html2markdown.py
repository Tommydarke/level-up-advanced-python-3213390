
import re

def html2markdown(html):
    '''Take in html text as input and return markdown'''
    html=html.replace("<em>", "*")
    html=html.replace("</em>", "*")
    html=" ".join(html.split())
    html=html.replace("</p><p>", "\n\n")
    html=html.replace("<p>", "")
    html=html.replace("</p>", "")
    linktexts=[]
    for text in html.split("</a>"):
        if "<a href=" in text:
            linktext=text[text.rfind(">")+1:]
            text=text.replace("<a href=\"","["+linktext+"](")
            text=text.replace("\">"+linktext,")")
            linktexts.append(text)
        else:
            linktexts.append(text)
    html="".join(linktexts)

    return html

