var path = require('path')

var ExtractTextPlugin = require('extract-text-webpack-plugin')
var webpack = require('webpack')

var env = process.env.NODE_ENV || 'development'

var config = {
  context: path.join(__dirname, 'web/static/js'),
  entry: {
    app: './app.js'
  },
  output: {
    path: path.join(__dirname, 'web/static/build'),
    filename: '[name].js',
  },
  module: {
    loaders: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        loader: 'babel'
      },
      {
        test: /\.scss$/i,
        loader: ExtractTextPlugin.extract(['css', 'sass'])
      }
    ]
  },
  sassLoader: {
    outputStyle: 'compressed',
    includePaths: ['node_modules']
  },
  plugins: [
    new ExtractTextPlugin('app.css'),
    new webpack.DefinePlugin({
      'process.env': {
        'NODE_ENV': JSON.stringify(env)
      }
    })
  ]
}

if (env === 'production') {
  config.plugins.push(new webpack.optimize.UglifyJsPlugin())
}

module.exports = config
