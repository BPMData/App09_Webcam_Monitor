import requests as rq
from datetime import datetime
from send_email_HTML import send_email_html, ord

key = "wup2WWLkgYPB9IC0XTmxwnRvNpapa2ffafGISs4H"

url = f"https://api.nasa.gov/planetary/apod?api_key={key}"

request = rq.get(url)
headers = request.headers
print(headers)

content = request.json()

text = content["explanation"]
img_url = content["url"]
hdimg_url = content["hdurl"]
img_date = content["date"]
date_obj = datetime.strptime(img_date, "%Y-%m-%d")
month = date_obj.strftime("%B")
year = date_obj.strftime("%Y")
day = ord(int(img_date[8:]))
title = content["title"]
email_date = content["date"].replace("-","")[2:]
media_type = content["media_type"]

email_content = f"""<style>
    .NASABlue {{
        color: #0B3D91;
    }}
</style>
<style>.center {{ 
display: block; margin-left: auto; margin-right: auto; 
}}
</style>
    <p style="font-family: Minion Pro; font-size: 14pt;">
    <span style="font-size: 18pt;" class="bold center">
    <a href="https://apod.nasa.gov/apod/ap{email_date}.html">{title}</a></span><br>
    <img src='{hdimg_url}' alt='{title}' class='center' style='max-width: 800px;'><br>
    <span class='center'>NASA's Astronomy Picture of the Day for {month} {day}, {year}.</span><br><br>
    <span style='font-size: 12pt' class='NASABlue'>{text}</span><br><br>
    </p>
    """


email_content_take_two = f"""
    <p style="font-family: Minion Pro; font-size: 14pt;">
    <h1 style='display: block; text-align: center;'>
    <a href="https://apod.nasa.gov/apod/ap{email_date}.html">{title}</a></h1><br>
    <img src='{hdimg_url}' alt='{title}' style='max-width: 800px; display: block; margin-left: auto; margin-right: auto;'><br>
    <h2 style='display: block; text-align: center;'>NASA's Astronomy Picture of the Day for {month} {day}, {year}.</h2><br>
    <span style='font-size: 12pt; color: #0B3D91; font-weight: bold;'>&nbsp;&nbsp;&nbsp;&nbsp;{text}</span><br><br>
    </p>
"""

subject = f"{title}: NASA Astronomy Picture of the Day for {month} {day}, {year}."

send_email_html(subject, email_content_take_two)
print("Modified NASA E-Mail Sent!")



