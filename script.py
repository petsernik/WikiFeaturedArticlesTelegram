from config import Config
from core import main

if __name__ == '__main__':
    cfg = Config(
        TELEGRAM_CHANNELS=['@wikifeat'],
        RULES_URL='https://t.me/wikifeat/4',
        WIKI_URL='https://ru.wikipedia.org/wiki/Заглавная_страница',
        LAST_ARTICLE_FILE='last_article.txt',
    )
    main(cfg)
