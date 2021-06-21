module.exports = {
  "publicPath": "/static/vue/",
  "outputDir": "./build/static/vue/",
  "indexPath": "../../templates/vue_index.html",
  "pages": {
    "index": "src/main.js"
  },
  "transpileDependencies": [
    "vuetify"
  ],
  devServer: {
    port: 8080
  }
}
