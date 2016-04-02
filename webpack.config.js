var ExtractTextPlugin = require('extract-text-webpack-plugin');


var env = process.env.NODE_ENV == 'prod' ? 'prod' : 'dev';


module.exports = {
  context: __dirname + "/web/static/js",

  entry: {
    app: './app.js',
    suggest: './suggest.js',
  },

  output: {
    filename: '[name].js',
    path: __dirname + "/web/static/build"
  },

  resolve: {
      extensions: ['', '.js', '.jsx']
  },

  module: {
    loaders: [
      {
        test: /(\.js$|\.jsx$)/,
        loader: 'babel-loader',
        exclude: /node_modules/,
        query: {
          presets: ['es2015', 'react']
        }
      },
      { test: /\.scss$/, loader: ExtractTextPlugin.extract('css!sass') }
    ]
  },

  sassLoader: {
    outputStyle: (env == 'prod' ? 'compressed' : 'expanded')
  },

  plugins: [
    new ExtractTextPlugin("app.css")
  ]
};