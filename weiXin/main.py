#this is main process of whole project
#encoding utf-8
# filename: main.py
import web
from handle import Handle
urls = (
    '/weixin', 'Handle',
)


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
