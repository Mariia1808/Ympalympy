<template>
<div>   
  <form @submit.prevent="login">     
    <h3>Login</h3>
    <br>
    <br>
    <input
      style="margin-right: 20px; margin-top: 10px"       
      type="email"       
      placeholder="Email address..."       
      v-model="email"     
    />     
    <input
      style="margin-right: 20px; margin-top: 10px"       
      type="password"       
      placeholder="password..."       
      v-model="password"     
    />     
    <button type="submit">
       Login
    </button>   
  </form> 
</div>

</template>

<script>
import firebase from 'firebase';
export default {
    name: 'Home',
    data() {
        return {
            email: '',
            password: '',
        };
    },
    methods: {
        login() {
            firebase
                .auth()
                .signInWithEmailAndPassword(this.email, this.password)
                .then(() => {
                    alert('Successfully logged in');
                    this.$router.push('/dashboard');
                })
                .catch(error => {
                    alert(error.message);
                });
        },
    },
};

</script>
