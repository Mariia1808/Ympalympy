import Vue from 'vue'
import App from './App.vue'
import firebase from "firebase";
import router from "./router";
import vuetify from './plugins/vuetify';
import store from './store'



// Your web app's Firebase configuration
var firebaseConfig = {
  apiKey: "AIzaSyCTJ4kio8dSo-hGrlCNMYqvEdLTpw7UjpQ",
  authDomain: "rnaul-750a3.firebaseapp.com",
  projectId: "rnaul-750a3",
  storageBucket: "rnaul-750a3.appspot.com",
  messagingSenderId: "971033599324",
  appId: "1:971033599324:web:55d20bffe0de664b25b599"
  };
// Initialize Firebase
firebase.initializeApp(firebaseConfig);

Vue.config.productionTip = false

new Vue({
  router,
  vuetify,
  store,
  render: h => h(App)
}).$mount('#app')
