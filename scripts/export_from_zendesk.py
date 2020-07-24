#this might need to be ported to python3

import requests
import shutil
import os
import re
from markdownify import markdownify

from urlparse import urlparse

url="https://support.bigstep.com//api/v2/help_center/en-gb/articles.json"

#retrieve articles
content = requests.get(url).json()


#create output dir
outputdir="output"
if not os.path.isdir(outputdir):
    os.mkdir(outputdir)

relative_imgdir=os.path.join('assets',"guides")
imgdir=os.path.join(outputdir, relative_imgdir)
if not os.path.isdir(imgdir):
    os.mkdir(imgdir)


#take each article and convert it to markdown
for article in content['articles']:
    title=article["title"]
    
    fname=os.path.join(outputdir, title.lower().replace(" ","_")+".md")
    
    body = article['body']
    with open(fname, 'w') as f:
        #convert to ascii as there are a lot of issues with converting unicode encoded files
        abody=body.encode("ascii", errors='ignore')
        markdown = markdownify(abody)

        #look for images and download them
        matches = re.finditer("\!\[.*\]\((.*)\)", markdown)

        for match in matches:
            image_url = match.group(1)
            
            #prepare an image file name that is prefixed by the article name and the rest the last part of the path
            img_name = os.path.basename(urlparse(image_url).path)
            img_name_with_title = title.lower().replace(" ","_")+"_"+img_name
            img_file_path = os.path.join(imgdir, img_name_with_title)
           
            #download the image
            r = requests.get(image_url, stream=True)
            with open(img_file_path, 'wb') as out_file:
                shutil.copyfileobj(r.raw, out_file)
           
            #replace the original url with the assets one
            new_image_path=os.path.join("/",relative_imgdir, img_name_with_title)
            orig="!["+img_name+"]("+image_url+")"
            new="![]("+new_image_path+")"
            markdown = markdown.replace(orig,new)

        #write article title as first string
        f.write("# "+title+"\n")
        f.write(markdown)

        

