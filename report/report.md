# Analysis of top contributors for ICML 2022

This repository analyzes recent icml contributions. If you want to play around with the dataset yourself, you can try it out in the releases section of this repo.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/TobiasJacob/icml-crawler)


```python
import pandas as pd
import matplotlib.pyplot as plt
```


```python
df = pd.read_csv("../data/records.csv")
df = df.dropna()
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>paperid</th>
      <th>title</th>
      <th>author</th>
      <th>authorid</th>
      <th>abstract</th>
      <th>year</th>
      <th>institution</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>11</th>
      <td>17199</td>
      <td>DynaMixer: A Vision MLP Architecture with Dyna...</td>
      <td>Ziyu Wang</td>
      <td>72871-17199</td>
      <td>Recently, MLP-like vision models have achieved...</td>
      <td>2022</td>
      <td>Tencent</td>
    </tr>
    <tr>
      <th>12</th>
      <td>17199</td>
      <td>DynaMixer: A Vision MLP Architecture with Dyna...</td>
      <td>Wenhao Jiang</td>
      <td>72872-17199</td>
      <td>Recently, MLP-like vision models have achieved...</td>
      <td>2022</td>
      <td>Tencent</td>
    </tr>
    <tr>
      <th>13</th>
      <td>17199</td>
      <td>DynaMixer: A Vision MLP Architecture with Dyna...</td>
      <td>Yiming Zhu</td>
      <td>72873-17199</td>
      <td>Recently, MLP-like vision models have achieved...</td>
      <td>2022</td>
      <td>Graduate school at ShenZhen，Tsinghua university</td>
    </tr>
    <tr>
      <th>14</th>
      <td>17199</td>
      <td>DynaMixer: A Vision MLP Architecture with Dyna...</td>
      <td>Li Yuan</td>
      <td>72874-17199</td>
      <td>Recently, MLP-like vision models have achieved...</td>
      <td>2022</td>
      <td>Peking University</td>
    </tr>
    <tr>
      <th>15</th>
      <td>17199</td>
      <td>DynaMixer: A Vision MLP Architecture with Dyna...</td>
      <td>Yibing Song</td>
      <td>50012-17199</td>
      <td>Recently, MLP-like vision models have achieved...</td>
      <td>2022</td>
      <td>Tencent AI Lab</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>21230</th>
      <td>595</td>
      <td>Nyström Method with Kernel K-means++ Samples a...</td>
      <td>Dino Oglic</td>
      <td>7757-595</td>
      <td>We investigate, theoretically and empirically,...</td>
      <td>2017</td>
      <td>University of Bonn</td>
    </tr>
    <tr>
      <th>21231</th>
      <td>595</td>
      <td>Nyström Method with Kernel K-means++ Samples a...</td>
      <td>Thomas Gaertner</td>
      <td>8571-595</td>
      <td>We investigate, theoretically and empirically,...</td>
      <td>2017</td>
      <td>The University of Nottingham</td>
    </tr>
    <tr>
      <th>21232</th>
      <td>708</td>
      <td>Scalable Generative Models for Multi-label Lea...</td>
      <td>Vikas Jain</td>
      <td>6772-708</td>
      <td>We present a scalable, generative framework fo...</td>
      <td>2017</td>
      <td>Indian Institute of Technology Kanpur</td>
    </tr>
    <tr>
      <th>21233</th>
      <td>708</td>
      <td>Scalable Generative Models for Multi-label Lea...</td>
      <td>Nirbhay Modhe</td>
      <td>8843-708</td>
      <td>We present a scalable, generative framework fo...</td>
      <td>2017</td>
      <td>Georgia Tech</td>
    </tr>
    <tr>
      <th>21234</th>
      <td>708</td>
      <td>Scalable Generative Models for Multi-label Lea...</td>
      <td>Piyush Rai</td>
      <td>8844-708</td>
      <td>We present a scalable, generative framework fo...</td>
      <td>2017</td>
      <td>IIT Kanpur</td>
    </tr>
  </tbody>
</table>
<p>17876 rows × 7 columns</p>
</div>



Number of individual papers


```python
df["paperid"].nunique()
```




    4415



We can see how the conference grew over time


```python
df.groupby("year")["paperid"].nunique().plot()
plt.ylabel("papers")
pass
```


    
![png](report_files/report_6_0.png)
    


These are the Authors with most contributions


```python
df.groupby("author")["paperid"].nunique().sort_values(ascending=False).head(20)
```




    author
    Sergey Levine             40
    Masashi Sugiyama          36
    Pieter Abbeel             30
    Gang Niu                  26
    Mihaela van der Schaar    24
    Stefano Ermon             24
    Michael Jordan            22
    Andreas Krause            22
    Shimon Whiteson           21
    Tong Zhang                21
    Bernhard Schölkopf        21
    Chelsea Finn              21
    Bo Han                    21
    Jun Zhu                   20
    Percy Liang               20
    Yoshua Bengio             19
    Steven Wu                 19
    Zhaoran Wang              19
    Zhuoran Yang              19
    Tommi Jaakkola            18
    Name: paperid, dtype: int64



These are the institutions contributing most


```python
df_leads = df.groupby(["institution", "year"])["paperid"].nunique().unstack().sort_values(2022, ascending=False)
df_leads.to_csv("Leading Institutions.csv")
df_leads.head(30)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>year</th>
      <th>2017</th>
      <th>2018</th>
      <th>2019</th>
      <th>2020</th>
      <th>2021</th>
      <th>2022</th>
    </tr>
    <tr>
      <th>institution</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Carnegie Mellon University</th>
      <td>28.0</td>
      <td>22.0</td>
      <td>23.0</td>
      <td>30.0</td>
      <td>38.0</td>
      <td>50.0</td>
    </tr>
    <tr>
      <th>Google</th>
      <td>14.0</td>
      <td>30.0</td>
      <td>44.0</td>
      <td>61.0</td>
      <td>54.0</td>
      <td>49.0</td>
    </tr>
    <tr>
      <th>Tsinghua University</th>
      <td>4.0</td>
      <td>10.0</td>
      <td>12.0</td>
      <td>18.0</td>
      <td>19.0</td>
      <td>44.0</td>
    </tr>
    <tr>
      <th>Stanford University</th>
      <td>15.0</td>
      <td>27.0</td>
      <td>24.0</td>
      <td>47.0</td>
      <td>47.0</td>
      <td>41.0</td>
    </tr>
    <tr>
      <th>UC Berkeley</th>
      <td>18.0</td>
      <td>27.0</td>
      <td>30.0</td>
      <td>41.0</td>
      <td>45.0</td>
      <td>38.0</td>
    </tr>
    <tr>
      <th>MIT</th>
      <td>15.0</td>
      <td>21.0</td>
      <td>29.0</td>
      <td>52.0</td>
      <td>46.0</td>
      <td>36.0</td>
    </tr>
    <tr>
      <th>Peking University</th>
      <td>5.0</td>
      <td>8.0</td>
      <td>11.0</td>
      <td>10.0</td>
      <td>22.0</td>
      <td>32.0</td>
    </tr>
    <tr>
      <th>University of Oxford</th>
      <td>10.0</td>
      <td>15.0</td>
      <td>18.0</td>
      <td>25.0</td>
      <td>33.0</td>
      <td>30.0</td>
    </tr>
    <tr>
      <th>DeepMind</th>
      <td>18.0</td>
      <td>27.0</td>
      <td>21.0</td>
      <td>42.0</td>
      <td>30.0</td>
      <td>26.0</td>
    </tr>
    <tr>
      <th>ETH Zurich</th>
      <td>8.0</td>
      <td>7.0</td>
      <td>14.0</td>
      <td>16.0</td>
      <td>19.0</td>
      <td>26.0</td>
    </tr>
    <tr>
      <th>Google Brain</th>
      <td>17.0</td>
      <td>21.0</td>
      <td>28.0</td>
      <td>36.0</td>
      <td>31.0</td>
      <td>26.0</td>
    </tr>
    <tr>
      <th>Google Research</th>
      <td>5.0</td>
      <td>4.0</td>
      <td>19.0</td>
      <td>32.0</td>
      <td>41.0</td>
      <td>25.0</td>
    </tr>
    <tr>
      <th>University of Texas at Austin</th>
      <td>7.0</td>
      <td>6.0</td>
      <td>8.0</td>
      <td>21.0</td>
      <td>15.0</td>
      <td>23.0</td>
    </tr>
    <tr>
      <th>Microsoft Research</th>
      <td>26.0</td>
      <td>14.0</td>
      <td>19.0</td>
      <td>32.0</td>
      <td>38.0</td>
      <td>21.0</td>
    </tr>
    <tr>
      <th>Stanford</th>
      <td>6.0</td>
      <td>7.0</td>
      <td>6.0</td>
      <td>22.0</td>
      <td>18.0</td>
      <td>20.0</td>
    </tr>
    <tr>
      <th>University of Cambridge</th>
      <td>11.0</td>
      <td>9.0</td>
      <td>10.0</td>
      <td>13.0</td>
      <td>16.0</td>
      <td>19.0</td>
    </tr>
    <tr>
      <th>Massachusetts Institute of Technology</th>
      <td>5.0</td>
      <td>7.0</td>
      <td>9.0</td>
      <td>22.0</td>
      <td>13.0</td>
      <td>18.0</td>
    </tr>
    <tr>
      <th>KAIST</th>
      <td>2.0</td>
      <td>3.0</td>
      <td>13.0</td>
      <td>13.0</td>
      <td>13.0</td>
      <td>18.0</td>
    </tr>
    <tr>
      <th>Amazon</th>
      <td>5.0</td>
      <td>5.0</td>
      <td>3.0</td>
      <td>9.0</td>
      <td>14.0</td>
      <td>17.0</td>
    </tr>
    <tr>
      <th>University of Washington</th>
      <td>5.0</td>
      <td>6.0</td>
      <td>10.0</td>
      <td>16.0</td>
      <td>21.0</td>
      <td>17.0</td>
    </tr>
    <tr>
      <th>Microsoft</th>
      <td>8.0</td>
      <td>4.0</td>
      <td>7.0</td>
      <td>9.0</td>
      <td>23.0</td>
      <td>17.0</td>
    </tr>
    <tr>
      <th>University of California, Berkeley</th>
      <td>NaN</td>
      <td>6.0</td>
      <td>10.0</td>
      <td>21.0</td>
      <td>15.0</td>
      <td>17.0</td>
    </tr>
    <tr>
      <th>National University of Singapore</th>
      <td>2.0</td>
      <td>3.0</td>
      <td>4.0</td>
      <td>15.0</td>
      <td>14.0</td>
      <td>15.0</td>
    </tr>
    <tr>
      <th>University of Wisconsin-Madison</th>
      <td>3.0</td>
      <td>4.0</td>
      <td>4.0</td>
      <td>6.0</td>
      <td>10.0</td>
      <td>15.0</td>
    </tr>
    <tr>
      <th>Princeton University</th>
      <td>10.0</td>
      <td>13.0</td>
      <td>15.0</td>
      <td>25.0</td>
      <td>25.0</td>
      <td>15.0</td>
    </tr>
    <tr>
      <th>Seoul National University</th>
      <td>1.0</td>
      <td>2.0</td>
      <td>8.0</td>
      <td>5.0</td>
      <td>7.0</td>
      <td>15.0</td>
    </tr>
    <tr>
      <th>Purdue University</th>
      <td>2.0</td>
      <td>9.0</td>
      <td>5.0</td>
      <td>5.0</td>
      <td>7.0</td>
      <td>15.0</td>
    </tr>
    <tr>
      <th>Columbia University</th>
      <td>6.0</td>
      <td>10.0</td>
      <td>9.0</td>
      <td>14.0</td>
      <td>11.0</td>
      <td>14.0</td>
    </tr>
    <tr>
      <th>New York University</th>
      <td>4.0</td>
      <td>7.0</td>
      <td>9.0</td>
      <td>8.0</td>
      <td>17.0</td>
      <td>14.0</td>
    </tr>
    <tr>
      <th>EPFL</th>
      <td>5.0</td>
      <td>12.0</td>
      <td>12.0</td>
      <td>14.0</td>
      <td>14.0</td>
      <td>14.0</td>
    </tr>
  </tbody>
</table>
</div>



I am particularily interested in Northeastern, KIT, Tübingen, Munich, Zürich, and RWTH


```python
print("Tübingen", df[df["institution"].str.contains("Tübingen")]["paperid"].nunique())
print("Northeastern", df[df["institution"].str.contains("Northeastern")]["paperid"].nunique())
print("Karlsruhe", df[df["institution"].str.contains("Karlsruhe")]["paperid"].nunique())
print("Munich", df[df["institution"].str.contains("Munich")]["paperid"].nunique())
print("RWTH", df[df["institution"].str.contains("RWTH")]["paperid"].nunique())
print("ETH Zürich", df[df["institution"].str.contains("ETH")]["paperid"].nunique())
```

    Tübingen 51
    Northeastern 24
    Karlsruhe 2
    Munich 32
    RWTH 1
    ETH Zürich 101



```python
df[df["institution"].str.contains("Northeastern")].groupby("author")["paperid"].nunique().sort_values(ascending=False).head(10)
```




    author
    Huy Nguyen                 3
    Robin Walters              3
    Hao Wu                     2
    Kaidi Xu                   2
    Jung Yeon Park             2
    Jonathan Ullman            2
    Jan-Willem van de Meent    2
    Hongyang Zhang             2
    Linfeng Zhao               2
    Xiaolong Ma                2
    Name: paperid, dtype: int64




```python
df[df["institution"].str.contains("Tübingen")].groupby("author")["paperid"].nunique().sort_values(ascending=False).head(10)
```




    author
    Bernhard Schölkopf      19
    Matthias Hein            5
    Ulrike von Luxburg       3
    Philipp Hennig           3
    Nathanael Bosch          2
    Lars Mescheder           2
    Nicholas Krämer          2
    Erik Daxberger           2
    Niki Kilbertus           2
    Georgios Arvanitidis     2
    Name: paperid, dtype: int64




```python
df[df["institution"].str.contains("ETH")].groupby("author")["paperid"].nunique().sort_values(ascending=False).head(10)
```




    author
    Andreas Krause               22
    Martin Vechev                 9
    Ce Zhang                      6
    Aurelien Lucchi               6
    Thomas Hofmann                5
    Bastian Rieck                 4
    Karsten Borgwardt             4
    Francesco Locatello           4
    Timon Gehr                    3
    Giambattista Parascandolo     3
    Name: paperid, dtype: int64




```python
df[df["institution"].str.contains("Munich")].groupby("author")["paperid"].nunique().sort_values(ascending=False).head(10)
```




    author
    Stephan Günnemann        9
    Aleksandar Bojchevski    3
    Sandra Hirche            3
    Daniel Zügner            3
    Thomas Frerix            2
    Jonas Umlauft            2
    Johannes Gasteiger       2
    Stefan Feuerriegel       2
    Hinrich Schuetze         2
    Bertrand Charpentier     2
    Name: paperid, dtype: int64




```python
df[df["institution"].str.contains("RWTH")].groupby("author")["paperid"].nunique().sort_values(ascending=False).head(10)
```




    author
    Ciwan Ceylan    1
    Name: paperid, dtype: int64




```python
df[df["institution"].str.contains("Karlsruhe")].groupby("author")["paperid"].nunique().sort_values(ascending=False).head(10)
```




    author
    Johannes Fischer       1
    Martin Frank           1
    Steffen Schotthöfer    1
    Tianbai Xiao           1
    Name: paperid, dtype: int64




```python

```
