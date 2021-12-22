function getRandomInt(max) {
    return Math.floor(Math.random() * max);
  }
module.exports = (req,res,next) => {
    if(req.method === 'POST'){
        req.method = 'GET';
        const status = getRandomInt(4)
        switch(status){
            case 0:
                console.log("売り切れ\t売り切れ")
                break;
            case 1:
                console.log("販売中\t売り切れ")
                break;
            case 2:
                console.log("売り切れ\t販売中")
                break;
            case 3:
                console.log("販売中\t販売中")
                break;
        }
        req.url =  '/api' + status
    }
    next()
}