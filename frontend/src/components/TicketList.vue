<script setup>

import { onMounted , ref } from "vue";
import IconTicket from "../components/icons/IconTicket.vue"
import axios from "axios";

const data = ref([
    {"owner_id": "Loading", "id": "Loading"},
    {"owner_id": "Loading2", "id": "Loading2"}
]);

onMounted(() => {
    axios.get("http://localhost:8000/users/3/ticket/")
    .then(response => {data.value = response.data; console.log(response)})
    .catch(error => {console.error("There was an error fetching the data:", error);});
});

</script>

<template>
    <div>
        <p>Owner ID</p>
        <p>Ticket Number</p>
    </div>
    <IconTicket v-for="item in data" v-bind:key="item.id" v-bind:owner_id="item.owner_id" v-bind:id="item.id" />
</template>