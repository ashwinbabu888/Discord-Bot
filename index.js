const Discord = require('discord.js');
const bot = new Discord.Client();

const token = 'NzE0NzY4Mzc0MjI3NDAyNzcy.Xszg3g.bVtnJaMk3mDyYNKDCJjJ3B1iMXk';

const PREFIX = '!';

var version = '1.0.1';

var servers = {};


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

        case 'clear':
            if(!args[1]) return message.reply('Error: Please define a second argument')
            message.channel.bulkDelete(args[1]);
        break;

        case 'play':
            if(!args[1]){
                message.channel.send("you need to provide a link!");
                return;
            }

            if(!message.member.voiceChannel){
                message.channel.send("you must be in a voice channel to play the bot!");
                return;
            }            

        break;
    }
})

bot.login(token);