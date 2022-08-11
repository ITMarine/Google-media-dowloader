"""Полезный скрипт для поиска и скачивания медийки с гугла"""
from icrawler.builtin import GoogleImageCrawler


def google_image_downloader():
    filters = dict(
        type='photo',
        # color='blackandwhite',
        size='large',
        date=((2020, 1, 1), (2022, 9, 1))
    )
    crawler = GoogleImageCrawler(storage={'root_dir': './img'})
    # crawler.crawl(keyword='mr. robot', max_num=10)
    crawler.crawl(keyword='bali',
                  max_num=5,
                  min_size=(1000, 1000),
                  overwrite=True,
                  filters=filters,
                  file_idx_offset='auto')


def main():
    google_image_downloader()


if __name__ == '__main__':
    main()
