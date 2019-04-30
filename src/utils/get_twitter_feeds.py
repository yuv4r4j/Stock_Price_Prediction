# importing modules
from __future__ import print_function
from __future__ import division
import csv
import logging
import os
import time

import GetOldTweets3 as got

# create and confifure logger
logging.basicConfig(
    level=logging.DEBUG,
    filename='app.log',
    filemode='w',
    format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

# creating an object
logger = logging.getLogger()


def get_twitter_feed(search_string, start_date, end_date):
    logging.info(f"getting data for '{search_string}' string from {start_date} to {end_date}")
    since = time.time()

    # get twitter feeds
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch(search_string)\
                                           .setSince(start_date)\
                                           .setUntil(end_date)
    all_tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    time_elapsed = time.time() - since
    logging.info('Download complete in {:.0f}m {:.0f}s'.format(
        time_elapsed // 60, time_elapsed % 60))

    # format and write the twitter feeds into a csv file
    lines = [[
        'id', 'permalink', 'username', 'to', 'text', 'date', 'retweets',
        'favorites', 'mentions', 'hashtags', 'geo'
    ]]
    for _ in all_tweets:
        lines.append([
            _.id, _.permalink, _.username, _.to, _.text, _.date, _.retweets,
            _.favorites, _.mentions, _.hashtags, _.geo
        ])

    # create the folder
    folder_path = os.path.join(os.path.join('src', 'data'), 'twitter_feeds')
    os.makedirs(folder_path, exist_ok=True)
    feed_file_path = os.path.join(
        folder_path, f'{search_string}_{start_date}_to_{end_date}.csv')

    # write the content to csv file
    with open(feed_file_path, 'w', encoding='utf-8') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(lines)


def main():
    logging.info('Downloading twitter feeds')
    get_twitter_feed('infy', '2014-01-01', '2014-01-01')
    get_twitter_feed('infy', '2014-01-02', '2014-01-02')
    logging.info('Download compeleted')


if __name__ == '__main__':
    main()
