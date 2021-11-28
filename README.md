# FoodRecipeGenerator

<img src="https://liive.org/wp-content/uploads/2021/04/openai-logo-horizontal-gradient.jpg" height=200px>

# Table of contents
1. [Problem Statement](#problem) <br>
1.pre [Why did i do it?](#why)<br>
1.1 [Solving the problem steps](#solving) <br>
2. [Installation](#install) <br>
2.pre [OpenAI SuperSecret](#super) <br>
2.1 [Deployment on Heroku](#heroku) <br>
2.2. [Localhost deployment](#local)<br>
3. [Original Application](#orig)<br>
4. [Acknowlegements](#ack)<br>

## Problem Statement
<p><a name="problem"></a>
Find a solution to generate instructions on how to prepare a meal with any given ingredients. 

## Introduction
<a name="why"></a>

Given *nth* food products and *yth* type of food products this produces instructions on how to prepare a meal with the following items <br>
It is an interesting project to work on that encompasses skills in Full Stack Development. Dynamic generations of reactive components real time in JavaScript. Natural Language Processing within an OpenAI trained model to process the text and accomplish our Problem Statement above. Basically in summary my dummy project was just made so i can recycle assets and codebases into my commercial software - ADGSTUDIOS website is an engine in progress which will be out in the public in the future.</p>

## Solving the problem steps
<p>
<a name="solving"></a><br>

###### These are the steps i took to build this application.

1. I used my engine, to render a application page on my website - All components form part of the bootstrap package installed on my container.
2. Backend development pt1- First worked on a scrapper to extract the nth amount of food products and yth type of food products. You can refer to notebook https://github.com/adgsenpai/PickNPayScrapping
3. Backend development pt2 - Developing OpenAI method/Function - POST/GET API endpoint on my server adgstudios.co.za
4. Frontend development pt1 - Drew wireframe on Adobe XD, Created HTML5 components and translated some into JavaScript dynamic DOM generation.
5. Backend development pt3 - used Django templating to inject Data Dictionary into .js file. Data Structures to insert into HTML table onload and other functions.
6. Backend development pt4 - Using HTML DOM components made web application send basket information into Python backend for processing (POST/GET request handle)
7. Quality Control
8.  UI optimization/Clean up/Monitor Progress
9. Public Testing
 
</p>

### OpenAI Super Secret
<a name="super"></a>

In app.py

![image](https://user-images.githubusercontent.com/45560312/143789696-5f3ad0ed-4b7a-4aa5-a76d-fea7a9f06f36.png)

just replace mysupersecret with the key from OpenAI you can find it here <a href="https://beta.openai.com/account/api-keys">OpenAI Secret Key</a>

## Heroku Deployment
<a name="heroku"></a>

**Make sure you put your OpenAI super secret in app.py!**

Well everything is given - **Procfile** - **Requirements.txt** just fork my repo under GitHub and just deploy that repo on Heroku.  Thats how easy it is.
</p>

## Localhost Deployment

<p><a name="local"></a>

well just run **app.py!** but make sure you do

```
pip install -r requirements.txt
```
 
## Original Application
<p><a name="orig"></a>
You can view original application @ <a href="https://adgstudios.co.za/apps/foodapp" >OriginalApp</a>

## Acknowlegements
<p><a name="ack"></a>

#### (c) ADGSTUDIOS 2021

###### Data is mined from **Pick n Pay Group** legally by scrapping items/products using a script made by ADGSTUDIOS which can be found Open Source (GitHub Repo) on the internet for others to do the same and create a database. Images and products copyright to respected owners.
