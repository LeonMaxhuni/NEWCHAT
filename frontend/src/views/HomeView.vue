<script setup>
import NewChat from "../components/LiveChat.vue"
import TicketList from "../components/TicketList.vue"
</script>

<template>
  
  <div class="left-panel">
    <h1>Home view</h1>
    <RouterLink to="/">LOGIN VIEW</RouterLink>
    <TicketList />
  </div>

  <div class="mid-panel">
    <NewChat />
  </div>

</template>

<style>
.left-panel{
  width: 25%;
  display: inline-block;
  vertical-align: top;
}
.mid-panel{
  width: 75%;
  display: inline-block;
}
</style>