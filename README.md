# Exchange Notebook

- 過去の為替推移をもとに15分後の為替価格を予測する

----------------------------------------------------------------------------------------------------------------------------------------------------------

## データセット

- [GAIN Capital](http://ratedata.gaincapital.com/)
	- 2000年からの世界各国の為替データを保存

### ダウンロード方法

```bash
cd tools
python download.py
python make_dataset.py
```

----------------------------------------------------------------------------------------------------------------------------------------------------------

## ライブラリ


----------------------------------------------------------------------------------------------------------------------------------------------------------

## 関連サービス

-----------------------------------------------------------------------------------------------------------------------------------------------------------

## References

### 参考記事

- ryo_grid. [Twitter感情分析で株価予測の論文を検証したら約70%の精度で上下予測できた](https://qiita.com/ryo_grid/items/5a5ecc602186a3381c87), Qiita, 2017.
- hayatoy. [トランプ氏のツイートを機械学習し、為替の予測をしてみた。〜GCP ML系使い倒し〜](http://qiita.com/hayatoy/items/708aa3fced2d37bc026c), Qiita, 2017.
- Maho Nakata. [為替のTickdataをDukascopyからダウンロードする](https://www.slideshare.net/NakataMaho/tickdata), SlideShare, 2015.
- [株価指数に対するヘッジ](https://imoz.jp/fund/correlation.html)
- [仮想通貨チャート分析 〜テクニカル指標の有効性をデータで検証する〜](http://www.metaps.com/press/ja/blog-jp/367-2017-06-19-05-41-41), metaps, 2017-06-19.
- Trading Studio. [深層強化学習をベースとしたAIトレードの検討〈準備編〉](http://www.metaps.com/press/ja/blog-jp/373-ai), metaps, 2017-08-10.
- [【入門編】機械学習で仮想通貨の価格予測！KerasでLSTMモデルを構築してビットコインとイーサリアムの翌日の価格を予測する方法](https://www.codexa.net/keras-lstm-cryptos-forecast/), codexa, 2018-02-23.

### 類似コンペ

- [TalkingData AdTracking Fraud Detection Challenge](https://www.kaggle.com/c/talkingdata-adtracking-fraud-detection)
	- 広告のクリック予測
- [House Prices: Advanced Regression Techniques](https://www.kaggle.com/c/house-prices-advanced-regression-techniques)
	- 家の価格予測
- [Toxic Comment Classification Challenge](https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge)
	- 有害コメントの検出
	- 為替の動きそうなコメント検出に使えるかも?
- [Recruit Restaurant Visitor Forecasting](https://www.kaggle.com/c/recruit-restaurant-visitor-forecasting)
	- レストランへの来客数予測
- [Corporación Favorita Grocery Sales Forecasting](https://www.kaggle.com/c/favorita-grocery-sales-forecasting)
	- スーパーの売上予測
- [Zillow Prize: Zillow’s Home Value Prediction (Zestimate)](https://www.kaggle.com/c/zillow-prize-1)
	- 家の価格予測 
- [Web Traffic Time Series Forecasting](https://www.kaggle.com/c/web-traffic-time-series-forecasting)
	- Wikipediaのページ閲覧数予測
- [Instacart Market Basket Analysis](https://www.kaggle.com/c/instacart-market-basket-analysis)
	- 次に買う商品の予測
- [Outbrain Click Prediction](https://www.kaggle.com/c/outbrain-click-prediction)

## 関連論文

