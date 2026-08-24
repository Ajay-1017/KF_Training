import http from 'http';
const PORT = 8000;

const  server = http.createServer((req,res) => {

    // res.setHeader('Content-Type','text/html')
    // res.statusCode = 404;

    res.writeHead(500,{'Content-Type':'application/json'})
    res.write('<h1>Hello World!</h1>');
    res.end();
});

server.listen(PORT, () => {
    console.log(`server running on Port ${PORT}`);
});

