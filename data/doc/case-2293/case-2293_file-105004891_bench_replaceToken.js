var Benchmark = require('benchmark');
var suite = new Benchmark.Suite();
var token = require('../lib/text-processing/token');
var tokens = require('./fixtures/tokens.json');

var replacers = token.createSimpleReplacer(tokens);

module.exports = benchmark;

function benchmark(cb) {
    if (!cb) cb = function(){};
    console.log('# token.replaceToken');

    suite.add('token replace', function() {
        var res = token.replaceToken(replacers, 'kanye west').query;
    })
    .on('cycle', function(event) {
        console.log(String(event.target));
    })
    .on('complete', function() {
      console.log('Fastest is ' + this.filter('fastest').map('name'), '\n');
      cb(null, suite);
    })
    .run();
}

if (!process.env.runSuite) benchmark();
