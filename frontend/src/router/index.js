import { createRouter, createWebHistory } from 'vue-router'

import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'
import LiveChat from '@/components/LiveChat.vue'
import RandomInfo from '@/components/RandomInfo.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', component: LoginView },
    {
      path: '/home', component: HomeView, children: [
        { path: 'chat', component: LiveChat },
        { path: 'welcome', component: RandomInfo },
      ]
    },
  ]
})

export default router
