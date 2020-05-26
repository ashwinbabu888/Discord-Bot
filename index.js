const Discord = require('discord.js');
const bot = new Discord.Client();

const token = 'NzE0NzY4Mzc0MjI3NDAyNzcy.Xszg3g.bVtnJaMk3mDyYNKDCJjJ3B1iMXk';

bot.on('ready', () =>{
    console.log('This bot is online!');
})

bot.on('message', msg=>{
    if(msg.content === "we in?"){
        msg.reply('We\'re in!');
    }
})

bot.login(token);