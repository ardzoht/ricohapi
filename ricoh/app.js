
var express = require('express');
var app = express();

var Client = require('node-xmpp-client')

var client = new Client({
    jid: 'user@example.com',
    password: 'password'
}):

client.on('online', function() {
    console.log('online')
});

client.on('stanza', function(stanza) {
    console.log('Incoming stanza: ', stanza.toString())
});


app.get('/', function (req, res) {
  res.send('Hello World!');
});

app.listen(3000, function () {
  console.log('Example app listening on port 3000!');
});


