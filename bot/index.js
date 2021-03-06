const Discord = require("discord.js");
require('dotenv').config()

const client = new Discord.Client();

console.log(process.env.BOT_TOKEN)

client.login(process.env.BOT_TOKEN);