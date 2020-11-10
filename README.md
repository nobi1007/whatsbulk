# whatsbulk

> A desktop app for sending messages (text/media) in **bulk** too.

### Requirements
1. System -> Mac (tested)
2. WebBrowser -> Mozilla Firefox (supported)


### Features
1. supports multiple recipients
2. supports emoji in the text message
3. supports sending images with caption


### Steps to setup (only mac for now), copy and paste the following code in terminal:
1. ``` 
       git clone https://github.com/nobi1007/whatsbulk.git && cd whatsbulk
    ```

2. ``` 
       echo -e ' \n ---- Installing python3.9 ---- \n'
       brew install python3
       echo -e '\n ---- Creating virtualenv and activating it ---- \n'
       virtualenv whatsbulk-venv 
       source ./whatsbulk-venv/bin/activate
       echo -e '\n ---- Installing dependencies ----\n'
       pip install -r ./requirements.txt
       cd app
       echo -e '\n ---- Success, now you can run start.sh ----\n'
    ```


---------------------

### After setup, for running the app, copy and paste the following code in terminal:
> `python main.py`
