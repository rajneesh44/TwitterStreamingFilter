# TwitterStreamingFilter

>What I am doing is simply creating a twitter filter using sentiment analysis.
 The tweets are fetched using the twitter api, stored in redis database, sentiment analysis is done and then top 15 tweete are displayed using flask and HTML and Jinja.
Green, Red and Grey borders are used to show the positive, negative and neutral tweets. 


## Data Pipeline
![Data Pipeline](/dataPipeline.png)

## Usage

>1. Install [Redis](https://redis.io/)
>2. Make a twitter account at [Twitter](https://twitter.com/home).
>3. Make a [twitter developer](https://developer.twitter.com/) account, make an app and copy the public and private keys.
>4. Clone the repo by doing  git clone https://github.com/rajneesh44/TwitterStreamingFilter.git
>5. Install the requirements.txt : #pip install requirements.txt
 
 ```python
 #run main.py and then application.py
 python main.py
 python application.py
 ```


