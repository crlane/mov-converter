# mov-converter

This is a very simple proof of concept web service for converting short `*.mov` files to `*.mp4` files. 

## Requirements

- docker
- a heroku account to deploy


## Getting Started

If you have make installed: 

### Build


`make build`

### Run

`make run`

If you don't have make, see the command line invocations you need to run to complete these steps in the [Makefile](Makefile)

## Deploying

For this very simple project, I chose to deploy to [heroku](https://heroku.com). It's pretty much zero configuration, though it does require your Dockerfile to be written in a certain way. It also requires the `heroku-cli`. Once you have that though, it's very simple to deploy.

If you have an authenicated heroku account and have already run `heroku apps:create <your application name goes here>`:

`heroku container:push <your application name goes here>`, 

Thats it!


