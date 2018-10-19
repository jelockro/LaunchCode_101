const autoprefixer = require('autoprefixer');
const path = require('path');

module.exports = [{
  entry: ['./src/sass/app.scss', './src/js/app.js'],
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: 'bundle.js'
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        loader: 'babel-loader',
        query: {
          presets: ['@babel/env'],
          plugins: ['transform-object-assign']
        }
      },
      {
        test: /\.scss$/,
        use: [
          {
            loader: 'file-loader',
            options: {
             name: 'bundle.css',
            },
          },
          { loader: 'extract-loader' },
          { loader: 'css-loader'  },
          {
            loader: 'postcss-loader',
            options: {
              plugins: () => [autoprefixer()]
            }
          },
          { loader: 'sass-loader',
            options: {
              includePaths: ['./node_modules']
            }
          }

        ]
      }
    ]
  },

}];
