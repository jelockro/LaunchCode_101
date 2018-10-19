const path = require('path');
const autoprefixer = require('autoprefixer');
const CleanWebpackPlugin = require('clean-webpack-plugin');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
	entry: {
		app: './src/js/app.js'
	},
	plugins: [
		new CleanWebpackPlugin(['dist']),
		new HtmlWebpackPlugin({
	      template: './src/index.html',
	      filename: 'index.html'
		})
	],
	output: {
		filename: '[name].bundle.js',
		path: path.resolve(__dirname, 'dist')
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
	          { loader: 'postcss-loader',
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
     }
};
