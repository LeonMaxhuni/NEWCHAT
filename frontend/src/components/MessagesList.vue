<script setup>

import { onMounted , ref } from "vue";
import axios from "axios";

import IconMessage from "../components/icons/IconMessage.vue"

const data = ref([
    {
        "message": "Loading",
        "id": 0,
        "user_id": 0
    },
    {
        "message": "Loading",
        "id": 1,
        "user_id": 0
    },
]);

onMounted(async () => {
    // axios.get("http://localhost:8000/users/3/ticket/2")
    // .then(response => {data.value = response.data; console.log(response)})
    // .catch(error => {console.error("There was an error fetching the data:", error);});
    try {
        data.value = (await axios.get("http://localhost:8000/users/3/ticket/2")).data;
        console.log(data.value);
    }
    catch (error) {
        console.log(error);
    }
});

</script>

<template>
    <div>
        <IconMessage v-for="item of data" v-bind:key="item.id" v-bind:message="item.message" v-bind:user_id="item.user_id"/>
    </div>
</template>