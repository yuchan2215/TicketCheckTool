function getRandomInt(max) {
    return Math.floor(Math.random() * max);
  }
module.exports = (req,res,next) => {
    if(req.method === 'POST'){
        req.method = 'GET';
        req.url =  '/api' + getRandomInt(4)
        console.log("return :" + req.url)
    }
    next()
}