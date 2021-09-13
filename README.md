# Workshop_3

## Prerequisites

First of all, you need to install MongoDB and get it running. How to do that depends on your operating system. 

### Installing MongoDB - MacOS

[Official Instructions](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/)

It's easiest to install MongoDB Community Edition using [brew](https://brew.sh/).

### Installing MongoDB - Windows

It takes some extra work to get MongoDB running on Windows. If you have trouble using this official method, check out Docker below.

[Official Instructions](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-windows/)

### Installing Using Docker

If you have trouble installing MongoDB Community Edition with the above instructions, I recommend you try using [Docker](https://docs.docker.com/get-docker/) + [Kitematic](https://kitematic.com/).

Docker allows you to create "containers" that can run instances of programs. You can download a MongoDB image and run/manage it through Docker. Kitematic is a user interface for Docker. This setup requires a few more steps, but if you're not comfortable using the Terminal, then this is the optimal situation.

Steps

1) Install Docker
2) Install Kitematic
3) Run Docker, run Kitematic
4) Install the MongoDB image using Kitematic
5) Run MongoDB by clicking 'start'

## Database Tab - PyCharm

The Database tab is near the right hand side corner. The text is flipped vertically; it's right under the 'search' icon.

![](https://i.imgur.com/thIG6HX.png)

We can use this interface to examine what data is in our database.

Once you have it installed, you can view your MongoDB databases by clicking the plus sign and selecting MongoDB as the data source.

![](https://imgur.com/pVy5pFT.png)

Once you've added MongoDB, right click on 'MongoDB' to select your databases. You should get an interface like this.

NOTE: ONLY DATABASES WITH SAVED ITEMS WILL SHOW. Just connecting will not create a database, you also need to save an item to the database.

![](https://imgur.com/vx91y8f.png)

Double-clicking on a collection will bring up the center panel, which displays all the saved items in that collection. 

## MongoEngine

In this application, we will be using [MongoEngine](https://docs.mongoengine.org/) to connect to MongoDB through Python. MongoEngine also provides us with a library to save and query data to the database.

