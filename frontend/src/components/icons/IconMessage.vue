<script setup>

defineProps({
    "message": String, "user_id": String
})

</script>

<template>
    <div>
        <p>{{ message }}</p>
        <p>{{ user_id }}</p>
    </div>
</template>