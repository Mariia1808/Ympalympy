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
    </div>

</template>

<script>
import DataService from '../services/dataService';
export default {
    name: 'Dashboard',
    data() {
        return {
            vkLink: ''
        }
    },
    methods: {
        checkToxicity() {
            const reqData = {
                vk_link : this.vkLink
            }
            DataService.getToxicScore(reqData)
        }
    }
};

</script>

<style lang="scss" scoped></style>
