import re
import time

import click
from loguru import logger
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'd2coding'
plt.rcParams['axes.grid'] = True


class KatokBackupParser:
    def __init__(self, fname: str):
        self.fname = fname
        self.title = ''
        self.save_date = ''
        self.df = pd.DataFrame() # empty dataframe
        # [으름] [오후 3:33] 5/31자로 구글 버트 새로 내놨던데요 ㅋㅋ
        self.re_msg = re.compile(r'^\[([^\]]*)\] \[오([전후]) (\d{1,2}):(\d{2})\] (.*)')
        # --------------- 2019년 6월 15일 토요일 ---------------
        self.re_day = re.compile(r'^-* (\d{4})년 (\d{1,2})월 (\d{1,2})일 [월화수목금토일]요일 -*')
        self.re_inout = re.compile(r'^(.*)님이 (들어왔습니다.|나갔습니다.)')
        self.t_last_log = time.time()
        # self.parse()

    def log_too_frequent(self):
        if time.time() - self.t_last_log < 5:
            return True
        self.t_last_log = time.time()
        return False
    
    def parse(self):
        rows = self.rows = []
        year, month, day = 0, 0, 0
        logger.info('start parsing `%s`...'%(self.fname))
        with open(self.fname, 'rt', encoding='utf-8') as f:
            for i, line in enumerate(f):
                if i%1000 == 0:
                    if not self.log_too_frequent():
                        logger.info('%d lines parsed.'%i)
                if i == 0:
                    self.title = line
                    continue
                if i == 1:
                    idx = line.find(':') + 1
                    datetime = line[idx:]
                    self.save_date = datetime.strip()
                    continue
                line = line.strip()
                # [으름] [오후 3:33] 5/31자로 구글 버트 새로 내놨던데요 ㅋㅋ
                p = self.re_msg.search(line)
                if p:
                    uid, msg = p.group(1), p.group(5)
                    hour, mi = ({'전':0, '후':12}[p.group(2)] + int(p.group(3)))%24, int(p.group(4))
                    datetime = '%04d-%02d-%02d %02d:%02d:00'%(year, month, day, hour, mi)
                    rows.append([datetime, uid, msg, "M", line])
                    continue
                # --------------- 2019년 6월 15일 토요일 ---------------
                p = self.re_day.search(line)
                if p:
                    year, month, day = int(p.group(1)), int(p.group(2)), int(p.group(3))
                    datetime = '%04d-%02d-%02d 00:00:00'%(year, month, day)
                    continue
                p = self.re_inout.search(line)
                if p:
                    uid, inout = p.group(1), p.group(2)
                    rows.append([datetime, uid, inout, "IO", line])
                    continue
                if rows:
                    rows[-1][2] += '\n' + line      # row.msg
                    rows[-1][-1] += '\n' + line     # row.line
        logger.info('parsing completed! (%d lines of text'%(i))
        logger.info('creating dataframe...')
        df = self.df = pd.DataFrame(self.rows, columns=[ 'datetime', 'user', 'msg', 'type', 'original'])
        logger.info(df.info())
        logger.info(df.head(3))
        logger.info(df.tail(3))
        logger.info('saving dataframe to csv...')
        self.df.to_csv(self.fname + '.csv')
        logger.info('saving done.')

    def plot(self):
        df = self.df
        logger.info(df.user.value_counts(normalize=True)[:12])
        talkative_users = set(df.user.value_counts()[:12].index)
        logger.info(talkative_users)
        df = df[df['user'].isin(talkative_users)]
        df.datetime = pd.to_datetime(df.datetime)
        grouped = df.set_index('datetime').groupby('user')
        #for k, group in grouped:
        #    group.resample('15min').user.count()
        df_ = pd.DataFrame({k:group.resample('1H').user.count() for k, group in grouped})
        logger.info(df_.head(10))
        df_.plot()
        plt.show()


@click.command()
@click.option('-f', '--fname', default='', help='Exported Kakao-talk backup txt file to parse.')
def main(fname: str):
    parser = KatokBackupParser(fname)
    parser.parse()
    #parser.plot()
                

if __name__ == '__main__':
    main() # pylint: disable=no-value-for-parameter