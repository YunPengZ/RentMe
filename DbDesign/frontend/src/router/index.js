import Vue from 'vue'
import Router from 'vue-router'
import store from '../store'

Vue.use(Router)

import NotFound from '../components/NotFound.vue'
import Hello from '../components/Hello.vue'
import Login from '../components/Login.vue'

const router = new Router({
  routes: [
    {
      path: '*',
      name: '404',
      component: NotFound
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/hello',
      component: Hello,
      meta: { requiresAuth: true }
    }
  ]
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    // this route requires auth, check if logged in
    // if not, redirect to login page.
    if (store.state.user_ID.length === 0) {
      next({
        path: '/login',
        query: { redirect: to.path }
      })
    } else {
      next()
    }
  } else {
    next() // make sure to always call next()!
  }
})

export default router
