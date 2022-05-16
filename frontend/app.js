/**
 * create by Sibo 2022/4/28
 */
const express = require('express');
const bodyParser = require('body-parser');
const path = require('path');
const NodeCouchDB = require('node-couchdb');

const couch = new NodeCouchDB({
    host: '172.26.129.242',
    protocol: 'http',
    port: 5984,
    auth:{
        user:'admin',
        password: 'admin'
    }
});

const app = express();
const port = 8080;

// to get the static files in 'public'
app.use(express.static(__dirname + '/public'));

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: false}));

const databaseArr = ['new_twitter'];
const viewArr = ['scenario1', 'scenario2.1', 'scenario2.2', 'scenario3', 'scenario4', 'scenario5'];
const groupLevel = '10';
async function getData(dbArr, vArr, groupLevel) {
    var resultArr= {};
    for (let i=0; i<dbArr.length; i++){
        for (let j=0; j<vArr.length; j++){
            // use await to guranttee the right sequence of the execution 
            const data = await couch.get(dbArr[i], '_design/BackendPreprocessing/_view/' + vArr[j] + '/?group_level=' + groupLevel);
            if (vArr[j] === 'scenario2.1'){
                resultArr['scenario21'] = data.data.rows;
            }else if (vArr[j] ==='scenario2.2'){
                resultArr['scenario22'] = data.data.rows;
            }else {
                resultArr[vArr[j]] = data.data.rows;
            }
        }
    }
   
    const dataSurb = await couch.get('old_old_twitter', '_design/BackendPreprocessing/_view/scenario4/?group_level=' + groupLevel);
    resultArr['oot_scenario4'] = dataSurb.data.rows;
    return resultArr;
}



app.get('/', async function(req, res){
    const resultData = await getData(databaseArr,viewArr, groupLevel);
    res.render('index', {
        result: resultData
    });
});

app.listen(port, function(){
    console.log('Listening On Port 8080...');
});