var http = require('http');
const fs = require('fs');
var path = require('path');


function login(request,response)
{
    if(request.url == '/')
    {
        console.log(request.url);
        response.writeHeader(200,{'Context-Type':'text/html'});
        var index_ = fs.readFileSync("./index.html");
        response.write(index_)
        response.end();

    }
    else
    {
        response.writeHeader(200,{'Context-Type':'jpeg'});
        var content_ = fs.readFileSync(request.url);
        response.write(process.cwd()+content_);
        console.log(process.cwd()+request.url)
        response.end();
    }
    
}



function login2(req,res)
{
    var filePath = req.url;
    if (filePath == '/'){
        filePath = '/index.html';
    }

    filePath = __dirname+filePath;
    var extname = path.extname(filePath);
    var contentType = 'text/html';

    switch (extname) {
        case '.js':
            contentType = 'text/javascript';
            break;
        case '.css':
            contentType = 'text/css';
            break;
    }
    
    fs.exists(filePath, function(exists) {

    if (exists) {
        fs.readFile(filePath, function(error, content) {
            if (error) {
                res.writeHead(500);
                res.end();
            }
            else {
                res.writeHead(200, { 'Content-Type': contentType });
                res.end(content, 'utf-8');
            }
        });
    }
    });
}

http.createServer(login2).listen(8080);
console.log("baslatildi!")