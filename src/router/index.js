import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue';
import Recommendations from '../views/Recommendations.vue';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/recommendations',
    name: 'Recommendations',
    component: Recommendations,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
