# BorisQunat
[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)

![png](assets/teaser.jpg)


## About
This repo aims to reproduce the __[repo](https://github.com/borisbanushev/stockpredictionai)__ authored by __[Boris Banushev](https://www.linkedin.com/in/borisbanushev/)__ 

### Dependencies 

#### yfinance
This repo currently relies on `yfinance` which is the most recent active fin data retrieving API.

    pip install yfinance --upgrade --no-cache-dir

#### git-lfs 
This repo also relies on git-lfs tracking to track `*.png` file extensions. It's not mandatory for you to install/use `git-lfs` but it's recommended.

#### simple reproduce
    conda env create -f env.yml

    


### Goldman Sachs NYSE

The __[repo](https://github.com/borisbanushev/stockpredictionai)__ uses the `NYSE:GS` data. Please run `plots/Goldman_Sachs_stock_price.py` to reroduce the following __[result](https://github.com/borisbanushev/stockpredictionai/blob/master/output_21_0.png)__
![png](assets/Goldman_Sachs_stock_price.png)


### Techinical Indicator 
Please run `plots/Techinical_indicators_for_Goldman_Sachs_last_400_days.py` to reproduce the __[result](https://github.com/borisbanushev/stockpredictionai/blob/master/output_32_0.png)__
![png](assets/Techinical_indicators_for_Goldman_Sachs_last_400_days.png)


### Simple Import of __[BERT](https://github.com/google-research/bert)__

The __[repo](https://github.com/borisbanushev/stockpredictionai)__ uses `MXNet/Gluon API` to leverage __[BERT](https://github.com/google-research/bert)__ which is available after installation using following command 

    pip install --upgrade mxnet>=1.4.1
    pip install gluonnlp


### Fourier Transforms
Please run `plots/Goldman_Sachs_(close)_stock_prices_&_Fourier_Transforms.py` to reproduce the __[result](https://github.com/borisbanushev/stockpredictionai/blob/master/output_45_0.png)__ 
![png](assets/Goldman_Sachs_(close)_stock_prices_&_Fourier_Transforms.png)


### Components of Fourier Transforms
Please run `plots/Components_of_Fourier_transforms.py` to reproduce the __[result](https://github.com/borisbanushev/stockpredictionai/blob/master/output_47_0.png)__ 
![png](assets/Components_of_Fourier_transforms.png)


### ARIMA as a Feature
Please run `plots/ARIMA_as_a_feature.py`to reproduce the __[result](https://github.com/borisbanushev/stockpredictionai/blob/master/output_51_0.png)__ 
![png](assets/ARIMA_as_a_feature.png)
    
                                 ARIMA Model Results                              
    ==============================================================================
    Dep. Variable:                D.price   No. Observations:                 2402
    Model:                 ARIMA(5, 1, 0)   Log Likelihood               -5675.514
    Method:                       css-mle   S.D. of innovations              2.570
    Date:                Sun, 21 Jul 2019   AIC                          11365.027
    Time:                        10:45:03   BIC                          11405.516
    Sample:                             1   HQIC                         11379.756
                                                                                  
    =================================================================================
                        coef    std err          z      P>|z|      [0.025      0.975]
    ---------------------------------------------------------------------------------
    const             0.0269      0.050      0.537      0.591      -0.071       0.125
    ar.L1.D.price    -0.0171      0.020     -0.839      0.401      -0.057       0.023
    ar.L2.D.price     0.0145      0.020      0.711      0.477      -0.025       0.054
    ar.L3.D.price     0.0019      0.020      0.092      0.927      -0.038       0.042
    ar.L4.D.price    -0.0005      0.020     -0.024      0.981      -0.040       0.040
    ar.L5.D.price    -0.0454      0.020     -2.225      0.026      -0.085      -0.005
                                        Roots                                    
    =============================================================================
                      Real          Imaginary           Modulus         Frequency
    -----------------------------------------------------------------------------
    AR.1           -1.8320           -0.0000j            1.8320           -0.5000
    AR.2           -0.6016           -1.7650j            1.8647           -0.3023
    AR.3           -0.6016           +1.7650j            1.8647            0.3023
    AR.4            1.5123           -1.0819j            1.8594           -0.0988
    AR.5            1.5123           +1.0819j            1.8594            0.0988
![png](assets/ARIMA_model_on_GS_stock.png)
