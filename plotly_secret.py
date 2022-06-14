import yfinance as yf
import plotly.graph_objects as go
from scipy.signal import argrelextrema
import numpy as np

# https://raposa.trade/blog/higher-highs-lower-lows-and-calculating-price-trends-in-python/

# https://plotly.com/python/marker-style/

ticker = 'NQ=F'

df = yf.download(tickers=ticker, period='6mo', interval='1d')
#df = yf.download(tickers = ticker, start='2013-01-01', end='2014-12-31')

df = df.reset_index()

Order = 5

max_idx = argrelextrema(df['Close'].values, np.greater, order=Order)[0]
min_idx = argrelextrema(df['Close'].values, np.less, order=Order)[0]


fig1 = go.Figure(data=[go.Candlestick(x=df['Date'],
                                      open=df['Open'],
                                      high=df['High'],
                                      low=df['Low'],
                                      close=df['Close'], showlegend=False)])
Size = 15
Width = 1

fig1.add_trace(
    go.Scatter(
        name='sell here',
        mode='markers',
        x=df.iloc[max_idx]['Date'],
        y=df.iloc[max_idx]['High'],
        marker=dict(
            symbol=46,
            color='darkred',
            size=Size,
            line=dict(
                color='MediumPurple',
                width=Width
            )
        ),
        showlegend=True
    )
)

fig1.add_trace(
    go.Scatter(
        name='buy here',
        mode='markers',
        x=df.iloc[min_idx]['Date'],
        y=df.iloc[min_idx]['Low'],
        marker=dict(
            symbol=45,
            color='forestgreen',
            size=Size,
            line=dict(
                color='MediumPurple',
                width=Width
            )
        ),
        showlegend=True
    )
)

# fig1.show()

fig1.update_layout(
    title=ticker, xaxis_rangeslider_visible=False
)

fig1.write_html( 'output_file_name.html',
                   auto_open=True )
