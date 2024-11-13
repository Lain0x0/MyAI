const express = require('express')
const app = express()

app.route('/', (res, req) => {
    res.send('Hello Developer')
})

app.listen(3007)

console.log('The app listening on port 3007...');
