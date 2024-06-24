<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'

const message = ref("");
const response = ref("");

let websocket = null;

const connectToSocket = () => {
    websocket = new WebSocket('ws://localhost:8000/ws');
    websocket.onmessage = (event) => {
        response.value = event.data;
        console.log(response.value)
    };
    websocket.onopen = () => {
        console.log('Websocket connection opened');
    };
    websocket.onclose = () => {
        console.log('Websocket connection closed');
    };
}

const sendMessage = () => {
    if (websocket && websocket.readyState === WebSocket.OPEN) {
        websocket.send(message.value);
        message.value = '';
    }
};
onMounted(() => {
    connectToSocket();
});
onBeforeUnmount(() => {
    if (websocket) {
        websocket.close();
    }
})
</script>

<template>
    <div>
        <h1>Webscokets</h1>
        <input v-model="message">
        <button @click="sendMessage">Send</button>
        <p>Response: {{ response }}</p>
        <!-- <ul>
            <li v-for="item in allMessages" :key="item.number">
                {{ item }}
            </li>
        </ul> -->
    </div>
</template>

<style>

</style>