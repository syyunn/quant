# BorisQunat

## About
This repo aims to reproduce the __[repo](https://github.com/borisbanushev/stockpredictionai)__ authored by __[Boris Banushev](https://www.linkedin.com/in/borisbanushev/)__ 

### Dependencies 

#### yfinance
This repo currently relies on `yfinance` which is the most recent active fin data retrieving API.

    pip install yfinance --upgrade --no-cache-dir

#### git-lfs 
This repo also relies on git-lfs tracking to track `*.png` file extensions. It's not mandatory for you to install/use `git-lfs` but it's recommended.

### Goldman Sachs NYSE

The __[repo](https://github.com/borisbanushev/stockpredictionai)__ uses the `NYSE:GS` data. Please refer to `plots/Goldman_Sachs_stock_price.py` to reroduce the following __[result](https://github.com/borisbanushev/stockpredictionai/blob/master/output_21_0.png)__
![png](assets/Goldman_Sachs_stock_price.png)

### Techinical Indicator 
Please refer to `plots/Techinical_indicators_for_Goldman_Sachs_last_400_days.py` to reproduce the __[result](https://github.com/borisbanushev/stockpredictionai/blob/master/output_32_0.png)__
![png](assets/Techinical_indicators_for_Goldman_Sachs_last_400_days.png)

### Simple Import of __[BERT](https://github.com/google-research/bert)__

The __[repo](https://github.com/borisbanushev/stockpredictionai)__ uses `MXNet/Gluon API` to leverage __[BERT](https://github.com/google-research/bert)__ which is available after installation using following command 

    pip install --upgrade mxnet>=1.4.1
    pip install gluonnlp

### Fourier Transforms
Please refer to `plots/Goldman_Sachs_(close)_stock_prices_&_Fourier_Transforms.py` to reproduce the __[result](https://github.com/borisbanushev/stockpredictionai/blob/master/output_45_0.png)__ 
![png](assets/Goldman_Sachs_(close)_stock_prices_&_Fourier_Transforms.png)
