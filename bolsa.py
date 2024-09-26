# -*- coding: utf-8 -*-
"""
import yfinance as yf
import time

def mostrar_preco(tickers):
    
    while True:
        
        for ticker in tickers:
            
            acao = yf.Ticker(ticker)
            preco_atual = acao.history(period='1d')['Close'].iloc[-1]
            
            print(f"O preco atual de {ticker} e R$ {preco_atual:.2f}")

        print("-" * 30)
        time.sleep(10) # Atualiza a cada 10 segundos

def main():

    # Liste os tickers das ações que você quer acompanhar 
    tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'PETR4.SA'] # Exemplo com ações da NASDAQ e B3
    mostrar_preco(tickers)

if __name__ == "__main__":
    main()


import yfinance as yf
import streamlit as st
import time

def mostrar_preco(tickers):
    while True:
        for ticker in tickers:
            acao = yf.Ticker(ticker)
            preco_atual = acao.history(period='1d')['Close'].iloc[-1]
            st.write(f"O preço atual de {ticker} é R$ {preco_atual:.2f}")
        st.write("-" * 30)
        time.sleep(10) # Atualiza a cada 10 segundos

def main():
    st.title("Monitor de Preços de Ações")
    tickers = st.text_input("Digite os tickers das ações separados por vírgula", 'AAPL, MSFT, GOOGL, AMZN, PETR4.SA')
    tickers = [ticker.strip() for ticker in tickers.split(',')]
    
    if st.button('Mostrar Preços'):
        placeholder = st.empty()
        while True:
            with placeholder.container():
                mostrar_preco(tickers)
                time.sleep(10) # Atualiza a cada 10 segundos

if __name__ == "__main__":
    main()

"""


import yfinance as yf
import streamlit as st
import time

def mostrar_preco(tickers):
    for ticker in tickers:
        acao = yf.Ticker(ticker)
        preco_atual = acao.history(period='1d')['Close'].iloc[-1]
        st.write(f"O preço atual de {ticker} é R$ {preco_atual:.2f}")
    st.write("-" * 30)

def main():
    st.title("Monitor de Preços de Ações")
    tickers = st.text_input("Digite os tickers das ações separados por vírgula", 'AAPL, MSFT, GOOGL, AMZN, PETR4.SA')
    tickers = [ticker.strip() for ticker in tickers.split(',')]
    
    if st.button('Mostrar Preços'):
        placeholder_preco = st.empty()
        while True:
            with placeholder_preco.container():
                mostrar_preco(tickers)
                time.sleep(10) # Atualiza a cada 10 segundos

if __name__ == "__main__":
    main()
