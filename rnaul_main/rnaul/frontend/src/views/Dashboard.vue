<template>
    <div>
        <h2>Dashboard</h2>
        <br><br>
        <p>Test toxicity of any vk page!</p>
        <br>
        <form @submit.prevent="checkToxicity">
            <input type="text" placeholder="Link vk page" v-model="vkLink"/>
            <button type="submit" >Test!</button>
        </form>
        <br>
        <p v-if="isCounterVisible" > Токсичность этой страницы: {{score}} </p>
    </div>

</template>

<script>
import DataService from '../services/dataService';
export default {
    name: 'Dashboard',
    data() {
        return {
            vkLink: '',
            score: 0,
            isCounterVisible: false
        }
    },
    methods: {
        checkToxicity() {
            // eslint-disable-next-line no-control-regex
            const vk_regex = new RegExp('(https?:\\/\\/)?(www\\.)?(vk.com\\/)(id\\d|[a-zA-z][a-zA-Z0-9_.]{2,})');
            if (vk_regex.test(this.vkLink)) {
                const reqData = {
                    vk_link: this.vkLink
                }
                DataService.getToxicScore(reqData).then(response => {
                    this.score = response.data.score;
                    this.isCounterVisible = true;
                })
            }
            else alert("Введите действительную ссылку на страницу вк!")
        }
    }
};

</script>

<style lang="scss" scoped></style>
