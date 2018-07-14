BinaryNativeBot
======================

This is a Reddit bot, designed to sweep the site for comments written in binary. As soon as it finds one, it responds with:

> The comment says:
> <decoded-binary-text>
> ^I ^am ^a ^bot. ^PM ^my ^[creator](https://reddit.com/user/orangeFluu) ^if ^I ^did ^something ^wrong.

## Instalation

If you always wanted to make your own bot, you are more than happy to use my code and modify it to your needs. Essentially, what you need to do is go to Reddit and authorize your bot, as to get a public script id and a secret id. Keep those secret and put them into the config.py file like so:

```python
username = "example_username" #The username and password for the account you are about to use
password = "my_password"      #Optional if you use the bot for rread-only actions
user_agent = "Bot_name v1.0" 
public_id = 'Cf1yGbWC255M4Q'
secret_id = '91VJNuAAcuVhEAGhUjxaP_bqtP8'
```

Then run the script from the command line like so:

     python source.py

And you are good to go!