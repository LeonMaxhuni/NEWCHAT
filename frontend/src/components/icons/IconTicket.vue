<script setup>
defineProps({
    "owner_id": String,"id": String
})
</script>

<template>
    <div>
        <p>{{ owner_id }}</p>
        <p>{{ id }}</p>
    </div>
</template>