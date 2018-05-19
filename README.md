# Exchange Notebook

- 過去の為替推移をもとに15分後の為替価格を予測する

## データセット

- [GAIN Capital](http://ratedata.gaincapital.com/)
	- 2000年からの世界各国の為替データを保存

### ダウンロード方法

```
cd tools
python download.py
python make_dataset.py
```

## 役立ちそうなライブラリ



## References

### 関連研究

#### 為替関連

- [Twitter感情分析で株価予測の論文を検証したら約70%の精度で上下予測できた](https://qiita.com/ryo_grid/items/5a5ecc602186a3381c87)
- [トランプ氏のツイートを機械学習し、為替の予測をしてみた。〜GCP ML系使い倒し〜](http://qiita.com/hayatoy/items/708aa3fced2d37bc026c)
- Maho Nakata. [為替のTickdataをDukascopyからダウンロードする](https://www.slideshare.net/NakataMaho/tickdata), 2015.


### 類似コンペ

