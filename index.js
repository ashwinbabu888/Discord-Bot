const Discord = require('discord.js');
const bot = new Discord.Client();

const token = 'NzE0NzY4Mzc0MjI3NDAyNzcy.Xszg3g.bVtnJaMk3mDyYNKDCJjJ3B1iMXk';

const PREFIX = '!';

bot.on('ready', () =>{
    console.log('This bot is online!');
})

bot.on('message', message=>{

    let args = message.content.substring(PREFIX.length).split(" ");

    switch(args[0]){
        case 'ping':
            message.reply('pong!');
        break;
    }
})

bot.login(token);