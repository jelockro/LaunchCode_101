const autoprefixer = require('autoprefixer');

module.exports = [{
  entry: ['./app.scss', './app.js'],
  output: {
    filename: 'bundle.js',
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        loader: 'babel-loader',
        query: {
          presets: ['preset-env'],
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
