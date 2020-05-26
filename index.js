const Discord = require('discord.js');
const bot = new Discord.Client();

const token = 'NzE0NzY4Mzc0MjI3NDAyNzcy.Xszg3g.bVtnJaMk3mDyYNKDCJjJ3B1iMXk';

const PREFIX = '!';

var version = '1.0.1';

bot.on('ready', () =>{
    console.log('This bot is online!');
})

bot.on('message', message=>{

    let args = message.content.substring(PREFIX.length).split(" ");

    switch(args[0]){
        case 'ping':
            message.channel.send('pong!')
        break;
        
        case 'website':
            message.channel.send('youtube.com/PF-Videos')
        break;
        
        case 'info':
            if(args[1] === 'version'){
                message.channel.send('Version ' + version);
            }else{
                message.channel.send('Invalid command :(')
            }
        break;
    }
})

bot.login(token);