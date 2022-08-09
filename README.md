# Lab 16 - Serverless Functions

## Introduction 
The purpose of this lab is to deploy a serverless function to the cloud.


## How to access to the database
> Enter query strings **country** and/or **capital** in the URL.
If both **country** and **capital** queries exist at the same time, the response will show if the capital matches with the country.

e.g. country=Japan, capital=Tokyo => Correct match

    https://capital-finder-yuwei.vercel.app/api/capital-finder?country=Japan&capital=Tokyo

The result is: ```Tokyo matches with Japan's capital.```


e.g. country=Japan, capiital=Washington => Incorrect match

    https://capital-finder-yuwei.vercel.app/api/capital-finder?country=Japan&capital=Washington

Since *Washington* is not the capital of Japan, the result is ```The capital of United States is NOT Washington```

<br/>
<br/>

> If only **country** is entered, it will send a response with results of capital name(s) and its currency.

e.g. country=South Africa

    https://capital-finder-yuwei.vercel.app/api/capital-finder?country=South%20Africa

Since South Africa has more than one capital cities, this will return multiple city names:

``The capital of south africa are Pretoria, Bloemfontein, Cape Town. Currency is ZAR``

<br/>
<br/>


> If only **capital** is entered, it will send a response with results of the country name and its currency.

e.g. capital=Paris
    
    https://capital-finder-yuwei.vercel.app/api/capital-finder?capital=Paris
    
The result is ```Paris is the capital of France. Currency is EUR```


