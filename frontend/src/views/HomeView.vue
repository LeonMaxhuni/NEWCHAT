<script setup>
// import NewChat from "../components/LiveChat.vue"
import { RouterView } from "vue-router";
import TicketList from "../components/TicketList.vue"
// import RandomText from "../components/RandomInfo.vue"
</script>

<template>
  
  <div class="left-panel">
    <h1>Home view</h1>
    <RouterLink to="/">LOGIN VIEW</RouterLink>
    <TicketList />
  </div>

  <div class="mid-panel">
    <!-- <NewChat /> -->
    <!-- <RandomText /> -->
     <nav>
      <RouterLink to="/home/chat">CHAT VIEW </RouterLink>
      <RouterLink to="/home/welcome">LOGIN VIEW</RouterLink>
     </nav>
     <RouterView></RouterView>
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