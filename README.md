# IMDB Review Grabber
The IMDB Review Grabber was made to help you get reviews from [IMDB](https://imdb.com). <br/>
Hopefully this tool can aid in the search of good movies. <br/>

## Installation
IMDB Review Grabber uses selenium to complete its task. <br>
Selenium can easily be installed using **pip**. <br>
Make sure to add `src/files/chromedriver.exe` to `PATH` on your computer. <br/>

### Pip
To make sure you have pip installed, do the following: <br> 
* Open command prompt
* Run `pip -V`
* The result should look something like this: `pip 20.3.3 from c:\users\INSERT_PATH`

If you **do not have** pip, 
the latest version can be found [here](https://pypi.org/project/pip/#files) <br>
If you do have pip, but need to **update**, simply run `py -m pip install -U pip`

### Modules
If you already have pip installed, open command prompt and do the following: <br>

```shell script
foo@bar> pip install selenium
```
(Don't forget to check out the [Selenium](https://www.selenium.dev/) module)

## Run
Running the program is **easy**. <br>
Open command prompt and `cd` to `imdbreviewgrabber/src`. <br>
Then simply do: `py imdbreviewgrabber.py`.