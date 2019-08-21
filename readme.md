# Lazy Academy 
Here is a short script for automatic sign-in using Python, selenium, and an STP library. IMPORTANT: Please use this responsibly and on your own computers. It's not meant to cheat the system, it's just meant to make a/A a little less stressful. 


## Getting Started

Please read the directions carefully. I’ve tried my best to streamline these things for you. However- and this is important- if after reading this if you still have any questions please please do not find me. If I have to stop whatever I’m doing at the moment to help you I will be annoyed. Justin Han would be happy to answer your questions though. 

## Prerequisites

Python and related programs,  Chromewebdriver, and about 30 min to an hour. 

## Installing

Install python, pip, and virtual env. In the terminal type the following

```
sudo brew install python
sudo curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
sudo python get-pip.py”
sudo pip install --upgrade virtualenv

```

Get Chromewebdriver

* Download and install chrome webdriver for your computer. For simplicity, I recommend installing it in the same file as where you are storing the python web driver

## Configuring to your system

Open up they python script, and enter you github email and github
username and password. Now you have a working script.

## Configuring Automatic Text updates and Password

This part can be a bit tricky, since you have to configure your email settings to allow remote logins. If you're using gmail just use this guide and it should work. 

https://support.google.com/accounts/answer/6009563 

Also FYI you can send a text through email.
* if you are using verizion it's YOURPHONENUMBER@vtext.com
* if you are using tmobile it's  YOURPHONENUMBER@@tmomail.net
* if you are using at&t it's "YOURPHONENUMBER@txt.att.net"

## Scheduling the task

For automatic running of the script I would recommend utilizing Cron. It comes preloaded with all linux and macs.  In the crontab type: 

```
 Crontab -e
 Select "nano" option
```

Enter the following strings in crontab. Don't forget to edit the absolute path!

```
 50 8   *   *   1-5    bash -c "python absolutepath/webdriver.py
 0  13  *   *   1-5    bash -c "python absolutepath/webdriver.py
 55 15  *   *   1-5    bash -c "python absolutepath/webdriver.py
```

Enjoy! There are also a dozen other ways to schedule task if you find cron confusing.

## Author

* TheLastSultan
* Long live Telegraph Hill



