/**
 * Created by geoolekom on 26.03.17.
 */

const webpack = require('webpack');
const BundleTracker = require('webpack-bundle-tracker');

const NODE_ENV = process.env.NODE_ENV || 'development';

module.exports = {
    entry: {
        app: './App.jsx'
    },
    context: `${__dirname}/static_src/`,
    output: {
        path: `${__dirname}/static/build/`,
        filename: '[name].js',
        publicPath: '/static/build/'
    },
    watch: NODE_ENV === 'development',
    devtool: NODE_ENV === 'development' ? 'cheap-module-inline-source-map' : false,
    module: {
        rules: [
            {
                test: /\.(js|jsx)$/,
                include: `${__dirname}/static_src/`,
                loader: 'babel-loader?presets[]=es2015&presets[]=react&presets[]=stage-1',
            },
            {
                test: /\.css$/,
                loader: 'style-loader!css-loader',
            },
            {
                test: /\.scss$/,
                loader: 'style-loader!css-loader!sass-loader&outputStyle=expanded'
            },
            {
                test: /\.(png|jpg|gif|svg|ttf|eot|woff|woff2)$/,
                loader: 'url-loader/limit=4096&name=[path]/[name].[ext]'
            }
        ]
    },
    plugins: [
        new webpack.NoEmitOnErrorsPlugin(),
        // new webpack.optimize.UglifyJsPlugin({
        //     compress: {
        //         warnings: false,
        //         drop_console: NODE_ENV !== 'development'
        //     }
        // }),
        new BundleTracker({filename: './webpack-stats.json'}),
    ],
    resolve: {
        modules: [`${__dirname}/static_src/`, 'node_modules'],
        extensions: ['.js', '.jsx']
    },
    resolveLoader: {
        modules: ['node_modules'],
        extensions: ['.loader.js', '.js']
    }

};